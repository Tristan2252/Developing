from gi.repository import Gtk

class Menu(Gtk.MenuItem):
    def __init__(self, parent, menu_name):
        Gtk.MenuItem.__init__(parent)
        self.save = Gtk.MenuItem(label=menu_name)
        parent.menu_bar.append(self.save)
        self.menu = Gtk.Menu()
        self.save.set_submenu(self.menu)


class Selection(Gtk.ComboBoxText):
    def __init__(self, parent, methods_lst, settings_list):
        Gtk.ComboBoxText.__init__(parent)

        self.setting_combo = Gtk.ComboBoxText()
        self.method_combo = Gtk.ComboBoxText()
        self.color_sel = Gtk.ColorButton()

        self._methods = methods_lst
        self._settings = settings_list
        self.method = None
        self.setting = None

        for method in self._methods:
            self.method_combo.append_text(method)

        for setting in self._settings:
            self.setting_combo.append_text(setting)

        self.method_combo.connect("changed", self.set_item, "method")
        self.setting_combo.connect("changed", self.set_item, "setting")
        self.color_sel.connect("color-set", parent.on_button_clicked, self.color_sel,  self)

    def get_method(self):
        return self.method

    def get_setting(self):
        return self.setting

    def set_item(self, combo, item):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            text = model[tree_iter][0]
            if item == "method":
                self.method = text
            if item == "setting":
                self.setting = text

