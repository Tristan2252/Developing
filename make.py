from gi.repository import Gtk
import themer


class SaveDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Gnome Themed", parent, 0,
                            (Gtk.STOCK_YES, Gtk.ResponseType.YES,
                             Gtk.STOCK_NO, Gtk.ResponseType.NO))

        box = self.get_content_area()
        self.text = Gtk.Label("  Save changes to config file?  ")

        box.add(self.text)
        self.show_all()


class SettingError(Gtk.Dialog):
    def __init__(self, parent, setting, method):
        Gtk.Dialog.__init__(self, "Error", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_border_width(10)
        box = self.get_content_area()
        self.error = Gtk.Label()
        self.error.set_markup("\n\tSorry, <i>{}</i>  \n"
                              "Does not exist for <i>{}</i>\n".format(setting, method))
        box.add(self.error)
        self.show_all()


class GenericError(Gtk.Dialog):
    def __init__(self, parent, error_text):
        Gtk.Dialog.__init__(self, "Error", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        box = self.get_content_area()
        self.error = Gtk.Label("\n{}\n".format(error_text))
        self.set_border_width(10)
        box.add(self.error)
        self.show_all()


class CustomButton(Gtk.Button):
    def __init__(self, parent, name, icon_image=None):
        super(CustomButton, self).__init__("  {} Settings".format(name))  # Set base class

        if icon_image is not None:
            self.set_image(icon_image)
            self.set_image_position(Gtk.PositionType.LEFT)

        self.set_relief(Gtk.ReliefStyle.NONE)
        self.connect("clicked", parent.on_button_clicked,
                     themer.get("{} methods".format(name)),
                     themer.get("{} settings".format(name)))


class Image(Gtk.Image):
    def __init__(self, path):
        super(Image, self).__init__()
        self.set_from_file(path)


class Menu(Gtk.MenuItem):
    def __init__(self, label, menu_bar):
        self.menu_item = Gtk.MenuItem(label=label)
        menu_bar.append(self.menu_item)
        self.menu = Gtk.Menu()

    def add_item(self, label, connection):
        """
        adds item to menu and set label and connection
        :param label: str # name of the item
        :param connection: def # function to connect item to
        :return: None
        """
        self.menu_item.set_submenu(self.menu)
        menu_item = Gtk.MenuItem(label=label)
        menu_item.connect("activate", connection)
        self.menu.append(menu_item)


class FileDialog(Gtk.FileChooserDialog):
    def __init__(self, parent):
        super(FileDialog, self).__init__("Please choose a file", parent, Gtk.FileChooserAction.OPEN,
                                         (Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
                                          Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        if not themer.DEBUG:  # if not in debug mode
                self.set_current_folder("/usr/share/themes/")


class AboutDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "About", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        box = self.get_content_area()
        scroll_box = Gtk.ScrolledWindow()
        scroll_box.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll_box.set_min_content_height(500)

        self.about_txt = themer.About()
        scroll_box.add(Gtk.Label(self.about_txt.get_text()))
        box.add(scroll_box)
        self.show_all()


class BackupDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Restore Backup", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()
        self.label = Gtk.Label("\nA '.DEFAULT' file was created before your first edit.\n"
                               "You can use it to restore to default settings.\n")
        self.backup_btn = Gtk.Button("Select Backup")
        self.backup_btn.connect("clicked", self.on_button_clicked)
        self.set_border_width(10)
        self.backup_path = None

        box.add(self.label)
        box.add(self.backup_btn)
        self.show_all()

    def on_button_clicked(self, widget):
        """
        prompts user with file chooser dialog when select
        backup button is selected.
        :param widget: function to connect to
        :return: None
        """
        choose_file = FileDialog(self)
        file_response = choose_file.run()
        if file_response == Gtk.ResponseType.OK:
            self.backup_path = choose_file.get_filename()
            self.destroy()
        choose_file.destroy()

    def get_path(self):
        """
        returns path of backup file
        :return: str # backup file path
        """
        return self.backup_path


class EntryDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Custom Settings", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK,
                             Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()
        self.set_border_width(10)
        self.table = Gtk.Table(4, 4)
        self.methods_entry = Gtk.Entry()
        self.settings_entry = Gtk.Entry()
        self.label = Gtk.Label("NOTE: Seperate each entry with ';' "
                               "For methods do not include '{' "
                               "And for settings do not include ':'\n")
        self.method_text = Gtk.Label('Methods')
        self.method_text.set_justify(Gtk.Justification.LEFT)
        self.setting_text = Gtk.Label('Settings')
        self.setting_text.set_justify(Gtk.Justification.LEFT)
        self.table.attach(self.label, 1, 4, 1, 2)
        self.table.attach(self.method_text, 0, 1, 2, 3, xpadding=5)
        self.table.attach(self.methods_entry, 1, 4, 2, 3)
        self.table.attach(self.setting_text, 0, 1, 3, 4, xpadding=5)
        self.table.attach(self.settings_entry, 1, 4, 3, 4)
        box.add(self.table)
        self.show_all()

