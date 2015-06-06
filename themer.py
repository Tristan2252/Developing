import subprocess
DEBUG = True

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
        print("\n{}".format(method)) if DEBUG else None
        method += " {\n"
        setting = "    {}:".format(setting)
        value += ";"
        for line in self._config:
            if line == method:
                self._editing = True
                self._setting_index = self._config.index(method)
            if self._editing:
                if "}" in line:
                    print("{} NOT FOUND".format(setting)) if DEBUG else None
                    self._editing = False
                    return False
                elif setting == line[:len(setting)]:
                    print("\nPrevious {}Changed {} {}"
                          "".format(self._config[self._setting_index], setting, value)) if DEBUG else None
                    if "1px solid" in self._config[self._setting_index]:  # accounts for border with in value
                        self._config[self._setting_index] = "{} 1px solid {}\n".format(setting, value)
                    else:
                        self._config[self._setting_index] = "{} {}\n".format(setting, value)
                    self._editing = False
                    return True
            self._setting_index += 1

    def write_config(self):
        """
        wires self._config to new file
        :return: None
        """
        print("\n[FILE SAVED]") if DEBUG else None
        with open('style_new.css', 'w') as f:
            f.writelines(self._config)

    def test_method(self, method, setting):
        """
        method tests if the specified method exists
        within the config file.
        :param method: str # method to find
        :return: bool # if it is found or not
        """
        method += " {\n"
        setting = "    {}:".format(setting)
        for line in self._config:
            if line == method:
                self._editing = True
                self._setting_index = self._config.index(method)
            if self._editing:
                if "}" in line:
                    print("{} NOT FOUND".format(setting)) if DEBUG else None
                    self._editing = False
                    return False
                elif setting == line[:len(setting)]:
                    self._editing = False
                    return True
            self._setting_index += 1


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


class About(object):
    def __init__(self):
        self.about_location = "README.md"
        self.contents = self.open_about()

    def open_about(self):
        with open(self.about_location) as f:
            return f.readlines()

    def get_text(self):
        return "".join(self.contents)


def get(item):
    if item == "Panel methods":
        panel_methods = ("#panel", "#panel:overview", ".panel-button:hover:overview", ".panel-button:focus")
        return panel_methods
    if item == "Panel settings":
        panel_settings = ("background-color", "border-color")
        return panel_settings
    if item == "Popup methods":
        popup_methods = (".candidate-popup-boxpointer", ".popup-menu-item:active", ".popup-sub-menu",
                         ".popup-submenu-menu-item:open")
        return popup_methods
    if item == "Popup settings":
        popup_settings = ("background-color", "-arrow-background-color", "-arrow-border-color")
        return popup_settings
    if item == "Button methods":
        button_methods = (".app-view-control", ".modal-dialog-button:hover", ".app-view-control:focus",
                          ".app-view-control:focus:hover", ".app-view-control:focus:active")
        return button_methods
    if item == "Button settings":
        button_settings = ("border", "background-color", "color")
        return button_settings


def update():
    if DEBUG:
        pass
    else:
        subprocess.call("git pull", shell=True)
