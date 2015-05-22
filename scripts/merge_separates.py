# merge 2 separate files into one
in_ = []
out_ = []

with open("input.txt") as infile:
    for line in infile.readlines():
        in_.append(line.strip().replace('"', '\"'))

with open("input-translation.txt") as infile:
    for line in infile.readlines():
        out_.append(line.strip().replace('"', '\"'))

with open("output.po", "w") as outfile:
    for i, line in enumerate(in_):
        outfile.write('msgid "%s"\n' % line)
        outfile.write('msgstr "%s"\n\n' % out_[i])
