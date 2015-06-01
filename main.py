from gi.repository import Gtk
import settings_dialog
import themer

class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Main")

        # self.set_default_size(100, 100)
        self.box = Gtk.Box()
        self.table = Gtk.Table(6, 8)
        self.table.set_row_spacings(5)

        self.config = themer.Config("gnome-shell.css")

        self.panel_img = Gtk.Image()
        self.panel_img.set_from_file("icons/panel.png")

        self.panel_settings = Gtk.Button()
        self.panel_settings_txt = Gtk.Button("Panel Settings")
        self.panel_settings_txt.set_relief(Gtk.ReliefStyle.NONE)
        self.panel_settings.connect("clicked", self.on_button_clicked,
                                    themer.get("panel methods"),
                                    themer.get("panel settings"))
        self.panel_settings.set_image(self.panel_img)
        self.panel_settings.set_relief(Gtk.ReliefStyle.NONE)
        self.popup_settings = Gtk.Button("Popup Settings")
        self.popup_settings.connect("clicked", self.on_button_clicked,
                                    themer.get("popup methods"),
                                    themer.get("popup settings"))

        self.table.attach(self.panel_settings, 0, 1, 0, 1)
        self.table.attach(self.panel_settings_txt, 1, 2, 0, 1)
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