import json

with open ("sfx_RPM_install.md.html", "r") as myfile:
    data=myfile.read().replace('\r''\n', '')


file = open("string_htmlvalue", "w")
file.write(data)
file.close()
