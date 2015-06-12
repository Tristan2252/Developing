from gi.repository import Gtk
import make
import themer


class ProgramWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window")

        box = Gtk.Box()
        self.button = Gtk.Button("Run Dialog")
        self.button.connect("clicked", self.on_button_clicked)
        self.config = themer.Config("gnome-shell.css")

        box.add(self.button)
        self.add(box)
        self.show_all()

    def on_button_clicked(self, widget):
        dialog = Dialog(self)
        dialog.run()
        dialog.destroy()


class Dialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Dialog", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        box = self.get_content_area()
        self.table = Gtk.Table(8, 5)

        # setting up scroll window
        scroll_box = Gtk.ScrolledWindow()
        scroll_box.set_min_content_height(600)
        scroll_box.set_min_content_width(600)

        self.set_border_width(5)
        self.panel = themer.get("PanelSettings")  # getting settings

        # for every method a settings table is made
        for i, method in enumerate(sorted(self.panel)):
            self.table.attach(make.SettingsTable(method, self.panel[method], parent), 0, 5, i, i+1)

        scroll_box.add(self.table)
        box.add(scroll_box)
        self.show_all()


if __name__ == '__main__':
    win = ProgramWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()