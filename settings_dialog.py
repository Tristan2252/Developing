from gi.repository import Gtk
import gnome_themed_dialig
import themer

class SettingsDialog(Gtk.Dialog):
    def __init__(self, parent, methods, settings):
        Gtk.Dialog.__init__(self, "Settings", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        box = self.get_content_area()
        self.set_border_width(5)
        self.table = Gtk.Table(6, 6)
        self.table.set_col_spacings(5)

        self.hex_color = None
        self.parent = parent
        self.method_lst = []
        self.setting_lst = []
        self.method_dict = {}
        self.setting_dict = {}

        for method in methods:
            self.method_dict[method] = Gtk.CheckButton(method)  # dynamic variable!!
            self.method_dict[method].connect("clicked", self.on_method_checked, method)

        for setting in settings:
            self.setting_dict[setting] = Gtk.CheckButton(setting)
            self.setting_dict[setting].connect("clicked", self.on_setting_clicked, setting)

        for i, label in enumerate(self.method_dict):
            self.table.attach(self.method_dict[label], i+1, i+2, 1, 2)

        for i, label in enumerate(self.setting_dict):
            self.table.attach(self.setting_dict[label], i+1, i+2, 3, 4)

        self.color_btn = Gtk.ColorButton()
        self.color_btn.connect("color-set", self.on_button_clicked, self.color_btn)
        self.table.attach(self.color_btn, 1, 2, 4, 5)

        box.add(self.table)
        self.show_all()

    def on_method_checked(self, widget, method):
        if method in self.method_lst:
            self.method_lst.remove(method)
        else:
            self.method_lst.append(method)

        print(self.method_lst)

    def on_setting_clicked(self, widget, setting):
        if setting in self.setting_lst:
            self.setting_lst.remove(setting)
        else:
            self.setting_lst.append(setting)

        print(self.setting_lst)

    def on_button_clicked(self, widget, button):
        color = themer.HexColor(button.get_rgba())
        self.hex_color = color.convert()
        for method in self.method_lst:
            for setting in self.setting_lst:
                if self.parent.config.test_method(method, setting):
                    self.parent.config.change_setting(method, setting, self.hex_color)
                else:
                    error = gnome_themed_dialig.ErrorDialog(self, setting, method)
                    error.run()
                    error.destroy()
