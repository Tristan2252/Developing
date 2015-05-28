#!/usr/bin/env python3
from themer import Config

test = Config("gnome-shell.css")

print()
test.change_setting("#panel", "background-color", "#90000")
print()
test.change_setting(".candidate-popup-boxpointer", "-arrow-background-color", "#2252")
test.write_config()
