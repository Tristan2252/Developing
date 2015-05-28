from gi.repository import Gtk
import gnome_themed_dialig
import themer


class GnomeThemed(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Gnome Themed",)

        self.hex_color = None
        self.config = themer.Config("gnome-shell.css")

        self.set_default_size(600, 600)
        self.box_main = Gtk.Box(True)
        self.table = Gtk.Table(10, 7, True)
        self.box_main.add(self.table)
        self.add(self.box_main)

        self.panel_btn = Gtk.ColorButton()
        self.panel_btn.connect("color-set", self.on_button_clicked, self.panel_btn,
                               "#panel", "background-color")

        self.popup_btn = Gtk.ColorButton()
        self.popup_btn.connect("color-set", self.on_button_clicked, self.popup_btn,
                               ".candidate-popup-boxpointer", "-arrow-background-color")

        self.exit_btn = Gtk.Button("Exit")
        self.exit_btn.connect("clicked", self.on_exit_clicked)
        self.save_btn = Gtk.Button("Save")
        self.save_btn.connect("clicked", self.on_saved_clicked)

        self.panel_txt = Gtk.Label("Panel Color")
        self.popup_txt = Gtk.Label("Popup Menu")

        self.table.attach(self.panel_txt, 1, 2, 1, 2, xpadding=10)
        self.table.attach(self.panel_btn, 2, 3, 1, 2, ypadding=10)
        self.table.attach(self.popup_txt, 1, 2, 2, 3)
        self.table.attach(self.popup_btn, 2, 3, 2, 3)
        self.table.attach(self.exit_btn, 5, 6, 9, 10, xpadding=5, ypadding=10)
        self.table.attach(self.save_btn, 6, 7, 9, 10, xpadding=5, ypadding=10)

    def on_button_clicked(self, widget, button, method, setting):
        color = themer.HexColor(button.get_rgba())
        self.hex_color = color.convert()
        self.config.change_setting(method, setting, self.hex_color)

    def on_exit_clicked(self, widget):
        Gtk.main_quit(self)

    def on_saved_clicked(self, widget):
        save_dialog = gnome_themed_dialig.SaveDialog(self)
        response = save_dialog.run()

        if response == Gtk.ResponseType.YES:
            self.config.write_config()

        save_dialog.destroy()

gnome_themed = GnomeThemed()
gnome_themed.connect("delete-event", Gtk.main_quit)
gnome_themed.show_all()
Gtk.main()
