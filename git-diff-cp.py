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

os.system('git diff --name-only >ttt.txt')
os.system('git submodule foreach git diff --name-only >>ttt.txt')

if os.path.exists(_dest):
    if not os.path.isdir(_dest):
        print("Exist "+_dest+" not a dir")
        quit()
    else:
        print("Exist "+_dest)
else:
    print("--mkdir "+_dest)
    os.mkdir(_dest)

pattern= re.compile(r"Entering \'(.+)\'")
with open('ttt.txt',"r") as ftxt:
    for line in ftxt.readlines():
        matched= re.match(pattern,line)
        if matched:
            _path=matched.group(1)+'/'
            #print("Find a path:"+_dir+_path)
        else:
            _file=line.rstrip()
            #print(_file)
            if os.path.isfile(_dir+_path+_file):
                _rpath = os.path.dirname(_dir+_path+_file)
                _name = os.path.basename(_dir+_path+_file)
                print("File: "+_dir+_path+_file)
                print("Dir : "+_rpath)
                os.system("cp --parents "+_dir+_path+_file+" ~/tmp/")
                #os.system("git diff "+_dir+_path+_file+"> ~/tmp/"+_rpath+'/'+_name+".diff")
            elif os.path.isdir(_dir+_path+_file):
                print("Folder: "+_dir+_path+_file)
            else:
                print("Not file: "+_dir+_path+_file)
#
print("------------")
