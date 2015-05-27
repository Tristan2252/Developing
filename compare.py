with open("gnome-shell.css") as f1:
    file1 = f1.readlines()

with open("style_new.css") as f2:
    file2 = f2.readlines()

for i, line in enumerate(file1):
    if file1[i] == file2[i]:
        print(True)

    else:
        print(line)