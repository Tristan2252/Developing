import subprocess
import os.path as ospath

DEBUG = True  # testing flag for development, Ex:activates print lines


class Config(object):
    def __init__(self, path):
        self._path = path
        self._config = self.open_file(self._path)
        self._editing = False
        self._setting_index = 0

        # self._default needs to be initialized after self.make_default
        # else default file doesnt exist
        self.make_default()
        self._default = self.open_file("{}.DEFAULT".format(self._path))

    @staticmethod
    def open_file(path):
        """
        opens file at self.path and returns contents
        :return: [] # contents of the file
        """
        with open(path) as f:
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

    def undo_setting(self, method, setting):
        """
        method iterates through each line in the config file and
        looks for the CSS method to be changed. Once found, editing
        mode is turned on. If in editing mode and the line is = to
        the setting to be changed then the index of the the old config file is loaded to it.
        :param method: str # the CSS method to be looked at. Ex. #panel {}
        :param setting: str # the setting with in the CSS method to be changed
        :return: None
        """
        print("\n{}".format(method)) if DEBUG else None
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
                    print("\nPrevious {}Changed back to {}"
                          "".format(self._config[self._setting_index],
                                    self._default[self._setting_index])) if DEBUG else None

                    # set index of config = to index of default file
                    self._config[self._setting_index] = self._default[self._setting_index]
                    self._editing = False
                    return True
            self._setting_index += 1

    def write_config(self):
        """
        wires self._config to new file and accounts for default
        file if self._path has it.
        :return: None
        """
        if self._path.endswith(".DEFAULT"):
            self._path = self._path[:-8]  # sets path to minos .DEFAULT so that it doesnt save to itself

        print(self._path) if DEBUG else None
        with open(self._path, 'w') as f:
            f.writelines(self._config)
            print("\n[FILE SAVED]") if DEBUG else None

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

    def make_default(self):
        """
        creates a default file for user to have as a backup if
        something goes wrong
        :return: None
        """
        if self._path.endswith(".DEFAULT"):  # if user restores from .DEFAULT a backup should not be made
            pass
            print(self._path) if DEBUG else None
        elif not ospath.isfile("{}.DEFAULT".format(self._path)):
            print("Default file made") if DEBUG else None
            text = self._config
            with open("{}.DEFAULT".format(self._path), "w") as new_file:
                new_file.writelines(text)


class HexColor(object):
    def __init__(self, rgb_color):
        self.red = rgb_color.red
        self.green = rgb_color.green
        self.blue = rgb_color.blue

    def convert(self):
        """
        converts RGB color to hex color value
        :return: str  # string representing hex value
        """
        red = (self.red * 255)
        green = (self.green * 255)
        blue = (self.blue * 255)

        return "#%02x%02x%02x" % (red, green, blue)


class About(object):
    def __init__(self):
        self.about_location = "README.md"
        self.contents = self.open_about()

    def open_about(self):
        """
        opens README.md file and returns contents
        :return: []  # lines in file
        """
        with open(self.about_location) as f:
            return f.readlines()

    def get_text(self):
        """
        joins list of README.md contents and returns
        the string
        :return: str  # joined contents of file
        """
        return "".join(self.contents)


CUSTOM_SETTINGS = {}


def get(item_settings):
    """
    returns requested settings or methods
    :param item_settings: str  # specifies what to return
    :return: {} # dictionary of methods and settings
    """
    if item_settings == "Panel":
        return {"#panel": ("color", "background-color"),
                "#panel:overview": ("border-color", "background-color"),
                ".panel-button:hover:overview": ("border-color", "background-color"),
                ".panel-button:focus": ("color", "background-color", "border-color")}

    if item_settings == "Popup":
        return {".popup-menu-item:active": ("color", "background-color", "border-color"),
                ".popup-sub-menu": "background-color",
                ".popup-submenu-menu-item:open": "background-color",
                ".candidate-popup-boxpointer": ("-arrow-background-color", "color", "-arrow-border-color",
                                                "background-color", "border-color")}

    if item_settings == "Button":
        return {".app-view-control": ("color", "background-color", "border", ),
                ".modal-dialog-button:hover": ("color", "background-color", "border"),
                ".app-view-control:focus": ("color", "background-color", "border"),
                ".app-view-control:focus:hover": ("color", "background-color", "border"),
                ".app-view-control:focus:active": ("color", "background-color", "border")}

    if item_settings == "Custom":
        if "" in CUSTOM_SETTINGS:  # removes blank key if it exists
            del CUSTOM_SETTINGS[""]
        return CUSTOM_SETTINGS


def update():
    """
    runs git pull to update program
    :return: None
    """
    if DEBUG:  # no need to update if being developed
        pass
    else:
        subprocess.call("git pull", shell=True)
