from gi.repository import Gtk

def hashtag_handler(label, uri):
    print('You clicked on the tag #%s' % uri)
    return True # to indicate that we handled the link request

window = Gtk.Window()
label = Gtk.Label()
label.set_markup('Unclickable line\nLine with a <a href="hashtag">#hashtag</a>\nLine with a <a href="different">#different</a> hashtag')
label.connect('activate-link', hashtag_handler)
window.add(label)
window.connect('destroy', Gtk.main_quit)
window.show_all()

Gtk.main()