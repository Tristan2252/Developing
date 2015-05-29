from gi.repository import Gtk

class Menu(Gtk.MenuItem):
    def __init__(self, parent, menu_name):
        Gtk.MenuItem.__init__(parent)
        self.menu_item = Gtk.MenuItem(label=menu_name)
        parent.menu_bar.append(self.menu_item)
        self.menu = Gtk.Menu()
        self.menu_item.set_submenu(self.menu)

    def add_item(self, item_name):
        self.menu_item = Gtk.MenuItem(label=item_name)
        self.menu.append(self.menu_item)
