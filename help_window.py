from gi.repository import Gtk
import make

class HelpWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Help")
        self.connect("destroy", lambda x: Gtk.main_quit())
        self.set_default_size(600, 600)  # set custom window size
        self.set_border_width(20)
        self.add(make.TextBox("help"))
        self.show_all()

if __name__ == '__main__':
    win = HelpWindow()
    Gtk.main()
