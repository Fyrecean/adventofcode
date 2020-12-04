'''
    Generate directories and files for each day 
'''

import os

for i in range(5, 26):
    if i < 10:
        folderName = "0" + str(i)
    else:
        folderName = str(i)
        
    os.system("mkdir " + folderName)
    os.chdir(folderName) 

    with open("1.py", "x") as f:
        f.write(
        "with open(\"" + folderName + "/in\") as f:\n" +
        "    input = f.readlines()\n")
    with open("2.py", "x") as f:
        f.write(
        "with open(\"" + folderName + "/in\") as f:\n" +
        "    input = f.readlines()\n")
    open("in", "x").close()
    os.chdir("..") 