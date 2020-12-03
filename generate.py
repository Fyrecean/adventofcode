'''
    Generate directories and files for each day 
'''

import os

for i in range(1, 26):
    os.system("mkdir " + str(i))
    os.chdir(str(i)) 
    with open("1.py", "x") as f:
        f.write(
        "with open(\"" + str(i) + "3/in\") as f:\n" +
        "    input = f.readlines()\n")
    with open("2.py", "x") as f:
        f.write(
        "with open(\"" + str(i) + "3/in\") as f:\n" +
        "    input = f.readlines()\n")
    open("in", "x").close()
    os.chdir("..") 