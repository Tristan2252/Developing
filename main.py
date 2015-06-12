#!/usr/bin/env python3

from gi.repository import Gtk
import themer
import make


class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Main")

        self.box = Gtk.Box()
        self.set_default_size(300, 100)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.table = Gtk.Table(6, 5)
        self.table.set_row_spacings(5)
        self.config = None

        if themer.DEBUG:  # for convenience when in debug mode
            self.config = themer.Config("gnome-shell.css")

        self.menu_bar = Gtk.MenuBar()

        self.file_menu = make.Menu("File", self.menu_bar)
        self.file_menu.add_item("Custom Settings", self.make_custom_settings)
        self.file_menu.add_item("Open", self.open_file)
        self.file_menu.add_item("Save", self.save_file)
        self.file_menu.add_item("Exit", self.exit)

        self.about = make.Menu("About", self.menu_bar)
        self.about.add_item("About", self.run_about)
        self.about.add_item("Update", self.run_update)

        self.backup = make.Menu("Backup", self.menu_bar)
        self.backup.add_item("Restore Backup", self.backup_dialog)

        self.panel_img = make.Image("icons/panel.png")
        self.popup_img = make.Image("icons/popup.png")
        self.button_img = make.Image("icons/button.png")

        self.panel_settings = make.CustomButton(self, "Panel", self.panel_img)
        self.popup_settings = make.CustomButton(self, "Popup", self.popup_img)
        self.button_settings = make.CustomButton(self, "Button", self.button_img)
        self.custom_settings = make.CustomButton(self, "Custom")

        self.table.attach(self.menu_bar, 0, 3, 0, 1, xpadding=2, yoptions=Gtk.AttachOptions.SHRINK)
        self.table.attach(self.panel_settings, 1, 2, 1, 2)
        self.table.attach(self.popup_settings, 1, 2, 2, 3)
        self.table.attach(self.button_settings, 1, 2, 3, 4)
        self.table.attach(self.custom_settings, 3, 4, 1, 2)

        self.box.add(self.table)
        self.add(self.box)
        self.show_all()

    def get_file(self):
        """
        presents user with file error if setting button is clicked
        with no config loaded.
        :return: None
        """
        file_error = make.GenericError(self, "You need to open a gnome-shell CSS file to edit first")
        error_response = file_error.run()
        if error_response == Gtk.ResponseType.OK:
            self.open_file()
        file_error.destroy()

    def open_file(self, widget=None):  # widget = to None by default so that it can be called individually
        """
        presents user with file selection dialog and creates
        themer.Config() object
        :param widget: widget connection
        :return: None
        """
        dialog = make.FileDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.config = themer.Config(dialog.get_filename())
            # self.config.make_default()

        else:
            self.config = ""  # self.config needs to be set to something other than None else infinite loop
        dialog.destroy()

    def save_file(self, widget=None):
        """
        presents user with a save dialog and error dialogs
        if needed
        :param widget: widget connection
        :return: None
        """
        save = make.SaveDialog(self)
        response = save.run()
        if response == Gtk.ResponseType.YES:
            try:  # checks if config is writable
                self.config.write_config()
            except AttributeError:
                save.destroy()
                save_error = make.GenericError(self, "No file to save, Open a file and edit it.\n"
                                                     "Then save the Changes")
                save_error.run()
                save_error.destroy()
        save.destroy()

    def run_about(self, widget):
        """
        runs about dialog that presents user the about page
        :param widget: widget connection
        :return: None
        """
        about_dialog = make.AboutDialog(self)
        about_dialog.run()
        about_dialog.destroy()

    def backup_dialog(self, widget):
        """
        runs backup dialog for user to select a backup
        :param widget: widget connection
        :return: None
        """
        backup_prompt = make.BackupDialog(self)
        response = backup_prompt.run()
        if response == Gtk.ResponseType.CANCEL:
            backup_prompt.destroy()
        else:
            backup_prompt.destroy()
            self.config = themer.Config(backup_prompt.get_path())
            self.save_file()
            self.config = None

    def make_custom_settings(self, widget):
        """
        prompts user with dialog to add custom settings to app
        :param widget: widget connection
        :return: None
        """
        custom_dialog = make.EntryDialog(self)
        response = custom_dialog.run()
        if response == Gtk.ResponseType.OK:

            methods = custom_dialog.methods_entry.get_text()
            settings = custom_dialog.settings_entry.get_text()

            # makes lists of string passed through it
            do_split = lambda string: string.split("; ") if "; " in string else string.split(";")

            for method in do_split(methods):
                themer.CUSTOM_SETTINGS[method] = do_split(settings)

            print(themer.CUSTOM_SETTINGS) if themer.DEBUG else None

        custom_dialog.destroy()

    @staticmethod
    def run_update(widget):
        """
        Runs update (github pull) cmd
        :param widget: widget connection
        :return: None
        """
        themer.update()

    def exit(self, widget):
        """
        runs save function and exits application
        :param widget: widget connection
        :return: None
        """
        self.save_file()
        Gtk.main_quit()


if __name__ == '__main__':
    win = Main()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
