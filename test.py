#!/usr/bin/env python3

def css_edit():
    import cssutils

    # Parse the stylesheet, replace color
    parser = cssutils.parseFile('gnome-shell.css')
    for rule in parser.cssRules:
        try:
            if 'popup-menu-boxpointer' in rule.selectorText:
                print(rule.style)
                # rule.style.backgroundColor = 'blue'  # Replace background
        except AttributeError as e:
            pass  # Ignore error if the rule does not have background

    # Write to a new file
    with open('style_new.css', 'wb') as f:
        f.write(parser.cssText)


css_edit()

