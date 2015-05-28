
class Config(object):
    def __init__(self, path):
        self._path = path
        self._config = self.open_file()
        self._editing = False
        self._setting_index = 0

    def open_file(self):
        with open(self._path) as f:
            return f.readlines()

    def change_setting(self, method, setting, value):
        method += " {\n"
        setting += ": "
        value += ";"
        self.test_method(method)
        for line in self._config:
            if line == method:
                self._editing = True
                self._setting_index = self._config.index(method)
            if self._editing:
                self._setting_index += 1
                if setting in line:
                    print("Changed {}to {}{}".format(self._config[self._setting_index], setting, value))
                    self._config[self._setting_index] = "    {}{}\n".format(setting, value)
                    self._editing = False

    def write_config(self):
        with open('style_new.css', 'w') as f:
            f.writelines(self._config)

    def test_method(self, method):
        if method in self._config:
            return True
        else:
            print("ERROR: " + method + " not found")
            return False


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


