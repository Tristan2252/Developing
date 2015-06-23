from gi.repository import Gtk

class AnotherWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GCT")
        self.connect("destroy", lambda x: Gtk.main_quit())

        self.add(Gtk.Label("This is another window"))
        self.show_all()



class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GCT")
        self.connect("destroy", lambda x: Gtk.main_quit())

        self.box = Gtk.Box()
        self.set_default_size(300, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.table = Gtk.Table(6, 5)

        self.button = Gtk.Button("sub-window")
        self.button.connect("clicked", self.open_window)
        self.table.attach(self.button, 0, 2, 0, 1)

        self.box.add(self.table)
        self.add(self.box)
        self.show_all()

    def open_window(self, win):
        subw = AnotherWindow()


def main():
    m = Main()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()