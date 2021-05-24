# Objective : Create new case folder and analysis file if not existing already.
import sys, os
from datetime import datetime
from pathlib import Path


path = "/home/dinesh/test"

def createDir(path, newdir):
    lsdir=(os.listdir(path))
    if newdir in lsdir:
        pass
        print("Directory exists")
        newpath = path +"/"+ newdir
        return newpath
    else:
        newpath = path +"/"+ newdir
        os.mkdir(newpath)
        print(f"created new directory {newpath}")
        return newpath



# print(f"Number of arguments: {len(sys.argv)} 'arguments.")
# print(f"Argument List: {str(sys.argv)}")

casenumber = str(123456)
# try:
#    casenumber = int(sys.argv[1])
# except ValueError:
#     print("Oops! That was not valid case number. Try again...")

currentMonth = datetime.now().strftime('%h')
current_year_full = datetime.now().strftime('%Y')  

path = createDir(path, current_year_full)

path = createDir(path, casenumber)

analysis_file_path = newpath = path +"/"+ casenumber + "_" +"analysis.txt"

Path(analysis_file_path).touch()

