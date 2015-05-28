
class Config(object):
    def __init__(self, path):
        self._path = path
        self._config = self.open_file()
        self._editing = False
        self._setting_index = 0

    def open_file(self):
        """
        opens file at self.path and returns contents
        :return: [] # contents of the file
        """
        with open(self._path) as f:
            return f.readlines()

    def change_setting(self, method, setting, value):
        """
        method iterates through each line in the config file and
        looks for the CSS method to be changed. Once found, editing
        mode is turned on. If in editing mode and the line is = to
        the setting to be changed then the index of the config file
        is set equal to the new setting.
        :param method: str # the CSS method to be looked at. Ex. #panel {}
        :param setting: str # the setting with in the CSS method to be changed
        :param value: str # string representing value to set the setting to
        :return: None
        """
        method += " {\n"
        setting = "    {}:".format(setting)
        value += ";"
        self.test_method(method)
        for line in self._config:
            if line == method:
                self._editing = True
                self._setting_index = self._config.index(method)
            if self._editing:
                if setting == line[:len(setting)]:
                    print("\nPrevious {}Changed {} {}".format(self._config[self._setting_index], setting, value))
                    self._config[self._setting_index] = "{} {}\n".format(setting, value)
                    self._editing = False
                    break
            self._setting_index += 1

    def write_config(self):
        """
        wires self._config to new file
        :return: None
        """
        with open('style_new.css', 'w') as f:
            f.writelines(self._config)

    def test_method(self, method):
        """
        method tests if the specified method exists
        within the config file.
        :param method: str # method to find
        :return: bool # if it is found or not
        """
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