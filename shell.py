import os
import shutil

def ls(dr):
    mklist = os.listdir(dr)
    print(' '.join(mklist))
    
def pwd(dr):
    print(dr)
    
def cd(path):
    path = ' '.join(path)
    os.chdir(path)
    new_path = os.getcwd()
    print(new_path)
    
    
def copy(file):
    shutil.copy2(file[0], file[1])
    
def move(path):
    shutil.move(path[0], path[1])

def remove(file):
    path = os.path.join(os.getcwd(), file[0])
    os.remove(path)
    
def removedir(dr):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), dr[0])
    os.rmdir(path)
    
def mkdir(name):
    os.mkdir(' '.join(name))


def command(command):
    if not command:
        return 1
    
    elif(command[0] == "ls"):
        ls(os.getcwd())
        return 0
        
    elif (command[0] == "cd"):
        try:
            cd(command[1:])
            return 0
        except FileNotFoundError:
            return 3
        except OSError:
            return 3
    
    elif (command[0] == "pwd"):
        pwd(os.getcwd())
        return 0
    
    elif (command[0] == "cp"):
        try:
            copy(command[1:])
            return 0
        except FileNotFoundError:
            return 3
        except IndexError:
            return 5
    
    elif (command[0] == "mv"):
        try:
            move(command[1:])
            return 0
        except FileNotFoundError:
            return 3
        except IndexError:
            return 5
    
    elif (command[0] == "rm"):
        try:
            remove(command[1:])
            return 0
        except FileNotFoundError:
            return 4
        except IndexError:
            return 4
          
    elif (command[0] == "rmdir"):
        try:
            removedir(command[1:])
            return 0
        except FileNotFoundError:
            return 3
        except OSError:
            return 7
        except PermissionError:
            return 8
        except IndexError:
            return 3
    
    elif (command[0] == "mkdir"):
        try:
            mkdir(command[1:])
            return 0
        except FileExistsError:
            return 6
        except FileNotFoundError:
            return 3
    else:
        return 2

def err(num):
    if num == 0:
        print("[Process Completed]")
    if num == 1:
        print("[Error] unknown command")
    if num == 2:
        print("[Error] no command")
    if num == 3:
        print("[Error] path not found")
    if num == 4:
        print("[Error] file not found")
    if num == 5:
        print("[Error] no file destination")
    if num == 6:
        print("[Error] directory is already exists")
    if num == 7:
        print("[Error] directory is not empty")
    if num == 8:
        print("[Error] access denied")
        
        
while True:
    directory = os.getcwd()
    dir2 = directory + "> "
    com = input(dir2).split()
    error = command(com)
    err(error)
    
