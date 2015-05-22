# remove dupe mesgids

in_ = {}
a = ''
b = ''
with open("input.po") as infile:
    for line in infile.readlines():
        if a and line.startswith("msgstr"):
            in_[a] = line.strip()
            a = ''
        if line.startswith("msgid"):
            if line not in in_:
                a = line.strip()
            else:
                a = ''
with open("removed_input.po", "w") as outfile:
    for id_, str_ in in_.items():
        outfile.write("%s\n%s\n\n" % (id_, str_))
