#!/usr/bin/python

import re
import os
import os.path

#_dir= os.getcwd()+'/'
_dir= './'
_path=""
_home=os.path.expanduser('~')
_dest=_home+r"/tmp"
#_dest=r"~/tmp" #error in os.path.exists

os.system('git diff --name-status >ttt.txt')
os.system('git submodule foreach git diff --name-status >>ttt.txt')

if os.path.exists(_dest):
    if not os.path.isdir(_dest):
        print("Exist "+_dest+" not a dir")
        sys.exit()
    else:
        print("Exist "+_dest)
else:
    print("--mkdir "+_dest)
    os.mkdir(_dest)

pattern_dir = re.compile(r"Entering \'(.+)\'")
pattern_D_file= re.compile(r"D\s+(\S+)")
pattern_M_file= re.compile(r"M\s+(\S+)")

with open('ttt.txt',"r") as ftxt:
    for line in ftxt.readlines():
        line = line.rstrip()
        matched_dir= re.match(pattern_dir,line)
        matched_D_file= re.match(pattern_D_file,line)
        matched_M_file= re.match(pattern_M_file,line)
        if matched_dir:
            _path=matched_dir.group(1)+'/'
            #print("Find a path:"+_dir+_path)
        elif matched_D_file:
            _file=matched_D_file.group(1)
            print("--del file:"+_dir+_path+_file)
        elif matched_M_file:
            _file=matched_M_file.group(1)
            #print(_file)
            if os.path.isfile(_dir+_path+_file):
                _name = os.path.basename(_dir+_path+_file)
                print("-Modify File: "+_dir+_path+_file)
                os.system("cp --parents "+_dir+_path+_file+" ~/tmp/")
                #_rpath = os.path.dirname(_dir+_path+_file)
                #os.system("git diff "+_dir+_path+_file+"> ~/tmp/"+_rpath+'/'+_name+".diff")
            elif os.path.isdir(_dir+_path+_file):
                print("---Folder: "+_dir+_path+_file)
            else:
                print("----Not file: "+_dir+_path+_file)
#
print("------------")
