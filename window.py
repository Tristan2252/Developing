from gi.repository import Gtk
import make

class ProgramWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window")

        box = Gtk.Box()
        self.button = Gtk.Button("Run Dialog")
        self.button.connect("clicked", self.on_button_clicked)

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
        box.add(make.SettingsBox(".window-caption", ["background-color", "color"]))
        box.add(make.SettingsBox("#panel", ["background-color", "color"]))
        self.show_all()


if __name__ == '__main__':
    win = ProgramWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()