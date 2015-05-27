import cssutils


# parser = cssutils.parseFile('gnome-shell.css')

def change_setting(setting, value):
    # Parse the stylesheet, replace color
    for rule in parser.cssRules:
        try:
            if rule.selectorText == setting:
                rule.style.backgroundColor = value  # Replace background
        except AttributeError as e:
            pass  # Ignore error if the rule does not have background


def write_config():
    with open('style_new.css', 'wb') as f:
        f.write(parser.cssText)


class HexColor(object):
    def __init__(self, rgb_color):
        self.red = rgb_color.red
        self.green = rgb_color.green
        self.blue = rgb_color.blue

    def convert(self):
        red = (self.red * 255)
        green = (self.green * 255)
        blue = (self.blue * 255)

        return "#%02x%02x%02x" % (red, green, blue)


