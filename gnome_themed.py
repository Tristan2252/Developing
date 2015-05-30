from gi.repository import Gtk
import gnome_themed_dialig
import themer
import make

class GnomeThemed(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Gnome Themed")

        self.hex_color = None
        self.config = themer.Config("gnome-shell.css")

        # ______________________ Setting up Window _________________________
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.top = Gtk.Box()
        self.bottom = Gtk.Box(True, orientation=Gtk.Orientation.HORIZONTAL)
        self.vboxL = Gtk.Box()
        self.vboxR = Gtk.Box()
        self.bottom.pack_start(self.vboxL, True, True, 0)
        self.bottom.pack_end(self.vboxR, True, True, 0)

        self.table1L = Gtk.Table(10, 4, False)  # (y)row, column(x)
        self.table1R = Gtk.Table(10, 4, False)
        self.table1L.set_col_spacing(0, 10)
        self.table1R.set_col_spacing(0, 10)
        self.vboxL.add(self.table1L)
        self.vboxR.add(self.table1R)
        self.table2 = Gtk.Table(1, 8)
        self.top.add(self.table2)

        self.main_box.pack_start(self.top, False, True, 0)
        self.main_box.pack_end(self.bottom, True, True, 0)
        self.add(self.main_box)

        # ___________________________ Menu Setup __________________________
        self.menu_bar = Gtk.MenuBar()
        self.table2.attach(self.menu_bar, 0, 2, 0, 1)
        self.file = make.Menu(self, "File")
        self.help = make.Menu(self, "Help")

        self.file.save = Gtk.MenuItem(label="Save")
        self.file.menu.append(self.file.save)
        self.file.save.connect("activate", self.on_saved_clicked)
        self.file.exit = Gtk.MenuItem(label="Exit")
        self.file.menu.append(self.file.exit)
        self.file.exit.connect("activate", self.on_exit_clicked)

        self.help.about = Gtk.MenuItem(label="About")
        self.help.menu.append(self.help.about)
        self.help.about.connect("activate", self.on_about_clicked)

        # ____________________________ Buttons _____________________________
        all_methods = themer.get_methods()
        all_settings = themer.get_settings()

        self.selection1 = make.Selection(self, all_methods, all_settings)
        self.selection2 = make.Selection(self, all_methods, all_settings)
        self.selection3 = make.Selection(self, all_methods, all_settings)
        self.selection4 = make.Selection(self, all_methods, all_settings)

        self.exit_btn = Gtk.Button("Exit")
        self.exit_btn.connect("clicked", self.on_exit_clicked)

        # ________________________ Table Attachments ______________________
        self.table1L.attach(Gtk.Label("Setting 1"), 1, 2, 0, 1, ypadding=10)
        self.table1L.attach(self.selection1.method_combo, 1, 2, 1, 2)
        self.table1L.attach(self.selection1.setting_combo, 1, 2, 2, 3)
        self.table1L.attach(self.selection1.color_sel, 2, 3, 2, 3)
        self.table1L.attach(Gtk.Label("Setting 2"), 1, 2, 3, 4, ypadding=10)
        self.table1L.attach(self.selection2.method_combo, 1, 2, 4, 5)
        self.table1L.attach(self.selection2.setting_combo, 1, 2, 5, 6)
        self.table1L.attach(self.selection2.color_sel, 2, 3, 5, 6)

        self.table1R.attach(Gtk.Label("Setting 3"), 1, 2, 0, 1, ypadding=10)
        self.table1R.attach(self.selection3.method_combo, 1, 2, 1, 2)
        self.table1R.attach(self.selection3.setting_combo, 1, 2, 2, 3)
        self.table1R.attach(self.selection3.color_sel, 2, 3, 2, 3)
        self.table1R.attach(Gtk.Label("Setting 4"), 1, 2, 3, 4, ypadding=10)
        self.table1R.attach(self.selection4.method_combo, 1, 2, 4, 5)
        self.table1R.attach(self.selection4.setting_combo, 1, 2, 5, 6)
        self.table1R.attach(self.selection4.color_sel, 2, 3, 5, 6)

        # self.table1R.attach(self.exit_btn, 6, 7, 9, 10, xpadding=5, ypadding=10)

    def on_button_clicked(self, widget, button, selection):
        method = selection.get_method()
        setting = selection.get_setting()
        color = themer.HexColor(button.get_rgba())
        self.hex_color = color.convert()
        if self.config.test_method(method, setting):
            self.config.change_setting(method, setting, self.hex_color)
        else:
            error = gnome_themed_dialig.ErrorDialog(self, setting, method)
            error.run()
            error.destroy()

    def on_exit_clicked(self, widget):
        save_dialog = gnome_themed_dialig.SaveDialog(self)
        response = save_dialog.run()

        if response == Gtk.ResponseType.YES:
            self.config.write_config()

        save_dialog.destroy()
        Gtk.main_quit(self)

    def on_saved_clicked(self, widget):
        self.config.write_config()

    def on_about_clicked(self, widget):
        pass

gnome_themed = GnomeThemed()
gnome_themed.connect("delete-event", Gtk.main_quit)
gnome_themed.show_all()
Gtk.main()
