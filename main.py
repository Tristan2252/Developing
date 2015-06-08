#!/usr/bin/env python3

from gi.repository import Gtk
import settings_dialog
import themer
import make

class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Main")

        self.box = Gtk.Box()
        self.set_default_size(300, 100)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.table = Gtk.Table(6, 8)
        self.table.set_row_spacings(5)
        self.config = None

        if themer.DEBUG:
            self.config = themer.Config("gnome-shell.css")

        self.menu_bar = Gtk.MenuBar()

        self.file_menu = make.Menu("File", self.menu_bar)
        self.file_menu.add_item("Open", self.open_file)
        self.file_menu.add_item("Save", self.save_file)
        self.file_menu.add_item("Exit", self.exit)

        self.about = make.Menu("About", self.menu_bar)
        self.about.add_item("About", self.run_about)
        self.about.add_item("Update", self.run_update)

        self.backup = make.Menu("Backup", self.menu_bar)
        self.backup.add_item("Restore Backup", self.run_update)

        self.panel_img = make.Image("icons/panel.png")
        self.popup_img = make.Image("icons/popup.png")

        self.panel_settings = make.CustomButton(self, "Panel", self.panel_img)
        self.popup_settings = make.CustomButton(self, "Popup", self.popup_img)
        self.button_settings = make.CustomButton(self, "Button")

        self.table.attach(self.menu_bar, 0, 3, 0, 1, xpadding=2)
        self.table.attach(self.panel_settings, 1, 2, 1, 2)
        self.table.attach(self.popup_settings, 1, 2, 2, 3)
        self.table.attach(self.button_settings, 1, 2, 3, 4)

        self.box.add(self.table)
        self.add(self.box)
        self.show_all()

    def on_button_clicked(self, widget, methods, settings):
        if self.config is None:
            self.get_file()
            self.on_button_clicked(widget, methods, settings)

        elif self.config == "":
            self.config = None  # set back to None so that user can be prompted for file again
        else:
            settings = settings_dialog.SettingsDialog(self, methods, settings)

            response = settings.run()

            if response == Gtk.ResponseType.OK:
                settings.destroy()
            settings.destroy()

    def get_file(self):
        file_error = make.GenericError(self, "You need to open a gnome-shell CSS file to edit first")
        error_response = file_error.run()
        if error_response == Gtk.ResponseType.OK:
            self.open_file()
        file_error.destroy()

    def open_file(self, widget=None):  # widget = to None by default so that it can be called individually
        dialog = make.FileDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.config = themer.Config(dialog.get_filename())

        else:
            self.config = ""  # self.config needs to be set to something other than None else infinite loop
        dialog.destroy()

    def save_file(self, widget=None):
        save = make.SaveDialog(self)
        response = save.run()
        if response == Gtk.ResponseType.YES:
            try:
                self.config.write_config()
            except AttributeError:
                save.destroy()
                save_error = make.GenericError(self, "No file to save, Open a file and edit it.\n"
                                                     "Then save the Changes")
                save_error.run()
                save_error.destroy()
        save.destroy()

    def run_about(self, widget):
        about_dialog = make.AboutDialog(self)
        about_dialog.run()
        about_dialog.destroy()

    @staticmethod
    def run_update(widget):
        themer.update()

    def exit(self, widget):
        self.config.write_config()
        Gtk.main_quit()

if __name__ == '__main__':
    win = Main()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()