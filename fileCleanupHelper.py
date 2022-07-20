#Do you hate having your hard drive fill up unexpectedly?
#Do you wnat to ruthelessly uninstall the big program taking up all of your hard drive space? (This code does not remove ANY files just reads their size, don't worry)
#Look no further!
##Mark Gilliland 2019 for SEED Lab
#the following was created to help me clean up my PC. It iterates through ALL folders in a directory
#and recursively finds their size. The code written to dive into each folder was not written by me but the code
#in fileCleanupHelper (this one) is all my own
#A pie chart is then displayed with all of the subfolders and their relative size
#You must have matplotlib to use this script


import os
from getFileSize import *
from pathlib import Path
import matplotlib.pyplot as plt
#example: C:/Program Files (x86)/OpenOffice 4
#get good, cleaned user input
#prompt: the prompt given to the user
#default value: the default STRING that is assumed if the input is bad
#input type: 'string', 'int', 'float' will convert to the proper type
#retry: attempt if bad input, or use default value
def getUserInput(prompt = '', defaultVal = '', inputType = 'string', retry = True, requireValidPath = True):
    inputStr = input(prompt)
    if len(inputStr) != 0:
        if inputType == 'string':#if the function wants a string
            return inputStr
        elif inputType == 'float':#if a float is wanted
            try:#I realize try/catch is not the best here for performance, but that optimization is not neccessary
                return float(inputStr)
            except ValueError:
                if retry:
                    return getUserInput(prompt, defaultVal, inputType, retry)
                else:
                    return float(defaultVal)
        elif inputType == 'int':#if an int is wanted
            try:#I realize try/catch is not the best here for performance, but that optimization is not neccessary
                return int(inputStr)
            except ValueError:
                if retry:
                    return getUserInput(prompt, defaultVal, inputType, retry)
                else:
                    return int(defaultVal)
        elif inputType == 'path':#if an int is wanted
            try:
                newPath = Path(inputStr.replace('"',""))
            except OSError:
                print("Please try again, string could not be interpreted as a path")
                return getUserInput(prompt, defaultVal, inputType, retry, requireValidPath)
            if requireValidPath and (not newPath.is_dir() and not newPath.is_file()):#if required, check if it is valid
                if retry:
                    return getUserInput(prompt, defaultVal, inputType, retry, requireValidPath)
                else:
                    return Path(defaultVal)
            else:
                return newPath
            

pathToCheck = getUserInput(prompt = 'Please input a path to investigate: ', inputType = 'path')
print(str(pathToCheck))
subfolders = os.listdir(pathToCheck)
subfolderSizes = {}
for subfolder in subfolders:
    subpath = pathToCheck / Path(subfolder)
    try:
        subfolderSizes[subfolder] = int(get_size(subpath, useMB = True))
    except OSError:
        print(subpath, " failed due to OSError")
        subfolderSizes[subfolder] = 0


sortedDict = sorted(subfolderSizes.items(), key=lambda x: x[1], reverse = True)
subfolderList = []
subfolderSizeList = []
for item in sortedDict:
    print('{0:>40s} has {1:>6d}MB'.format(item[0], item[1]))
    subfolderList.append(item[0])
    subfolderSizeList.append(item[1])

#inspired by but not copy-pasted by https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
fig, ax = plt.subplots()
ax.pie(subfolderSizeList, labels = subfolderList, autopct='%1.1f%%')
ax.axis('equal')
ax.set_title(pathToCheck)
plt.show()

