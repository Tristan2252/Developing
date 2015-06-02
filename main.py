from gi.repository import Gtk
import settings_dialog
import themer
import make

class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Main")

        self.box = Gtk.Box()
        self.table = Gtk.Table(6, 8)
        self.table.set_row_spacings(5)

        self.config = themer.Config("gnome-shell.css")

        self.panel_img = make.Image("icons/panel.png")
        self.popup_img = make.Image("icons/popup.png")

        self.panel_settings = make.CustomButton(self, "Panel", self.panel_img)
        self.popup_settings = make.CustomButton(self, "Popup", self.popup_img)

        self.table.attach(self.panel_settings, 0, 1, 0, 1)
        self.table.attach(self.popup_settings, 0, 1, 1, 2)

        self.box.add(self.table)
        self.add(self.box)
        self.show_all()

    def on_button_clicked(self, widget, methods, settings):
        settings = settings_dialog.SettingsDialog(self, methods, settings)

        response = settings.run()

        if response == Gtk.ResponseType.OK:
            settings.destroy()
        settings.destroy()

win = Main()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()