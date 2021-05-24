# Objective : Create new case folder and analysis file if not existing already.
# Setting in bashrc : alias ddncase='/bin/python3 /home/dinesh/project/ddncase/newcase.py'
import sys, os
from datetime import datetime
from pathlib import Path


path = "/home/dinesh/cases"

subLog = {
"sss" : "SHOW SUB SUM",
"sssa" : "SHOW SUB SUM ALL",
"ssf" : "SHOW SUB SUM FAULT"
}

def createDir(path, newdir):
    lsdir=(os.listdir(path))
    if newdir in lsdir:
        pass
        # print("Directory exists")
        newpath = path +"/"+ newdir
        return newpath
    else:
        newpath = path +"/"+ newdir
        os.mkdir(newpath)
        # print(f"created new directory {newpath}")
        return newpath

def printer(casenumber, custname, log):
    mystring = subLog[log]
    newstring = mystring.replace(" ", "_")
    print(f"ssh user@[Controller 0 IP] {subLog[log]} > SR{casenumber}_{custname}_{newstring}_c0.txt")
    print(f"ssh user@[Controller 1 IP] {subLog[log]} > SR{casenumber}_{custname}_{newstring}_c1.txt")

def diagprinter(casenumber, custname):
    print(f"ssh user@[Controller 0 IP] diag > SR{casenumber}_{custname}_diag_c0.tgz")
    print(f"ssh user@[Controller 1 IP] diag > SR{casenumber}_{custname}_diag_c1.tgz")


try:
    casenumber = sys.argv[1]
except:
    casenumber = input("Plase provide case number: ")

if len(sys.argv) < 3:
    currentMonth = datetime.now().strftime('%h')
    current_year_full = datetime.now().strftime('%Y')  
    path = createDir(path, current_year_full)
    path = createDir(path,currentMonth)
    path = createDir(path, casenumber)
    analysis_file_path = path +"/"+ casenumber + "_" +"analysis.txt"
    Path(analysis_file_path).touch()

if len(sys.argv) > 2:
    try:
        custname = sys.argv[2]
    except:
        custname = input("Plase provide customer name: ")
    
    for key in subLog:
        if key in sys.argv[3:]:
            printer(casenumber, custname, key)
    if "diag" in sys.argv[3:] or "diags" in sys.argv[3:] :
         diagprinter(casenumber, custname)
    
