from gi.repository import Gtk

class SaveDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Gnome Themed", parent, 0,
                            (Gtk.STOCK_YES, Gtk.ResponseType.YES,
                             Gtk.STOCK_NO, Gtk.ResponseType.NO))

        box = self.get_content_area()
        self.text = Gtk.Label("Save changes to config file?")

        box.add(self.text)
        self.show_all()
