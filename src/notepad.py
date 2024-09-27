from collections import UserDict
import os
from src.address_book import Field
import pickle

# Color text ON
# RED = "\033[91m"
# GREEN = "\033[92m"
# YELLOW = "\033[93m"
# RESET = "\033[0m"
# BLUE = "\033[94m"
# FLY_BLUE = "\033[38;5;117m"
# PURPURE = "\033[35m"

# Color text OFF
RED = ""
GREEN = ""
YELLOW = ""
RESET = ""
BLUE = ""
FLY_BLUE = ""
PURPURE = ""

#------------КЛАС ДЛЯ ОДНОГО ФАЙЛА З КОРОТКИМ ОПИСОМ--------------
#-----можна створити, викликати для редагування, додати опис----------------

def read_from_file(file):
    with open(file, 'rb') as fh:
        return pickle.load(fh)

class Notepad(Field):
    def __init__(self, name, describe="нотатки" ):
        self.topic = "notes"
        self.describe = describe
        self.name=name
        self.dir=os.path.join(path_different,"notes")
        self.file=os.path.join(self.dir,name)+'.txt'
        try:
            with open(self.file, 'x'):
                pass
        except Exception:
            pass

    def open_notepad(self):
        os.system(self.file)
    def add_description(self):
        print("add your description to this notebook, please")
        self.describe=input(">")


    def __str__(self):
        return (f"{BLUE} name:{YELLOW} {self.name}, {BLUE}description:{YELLOW} {self.describe}{RESET}")


#------------КЛАС ДЛЯ списку текстових файлів-------------
#----можна показати список, видалити зі списку, при правильному виході все зберігається, --------------
#----можливо терба зробити зберігання після кожної зміни списку(додавання видалення)
class Notepad_dict(UserDict):
    filename=os.path.join("..\\files", "save_notepad.bin")

    def add_notepad(self):
        print("Enter file name")
        while True:
            name=input("> ")
            if len(name)>0:
                notepad = Notepad(name)
                print("Enter a short description")
                notepad.describe = input("> ")
                notepad.open_notepad()
                self[notepad.name] = notepad
                break
            else:
                continue

    def get_all(self):
        for n in self:
            print(self[n])

    def delete_notepad(self, name):
        os.remove(self[name].file)
        del self[name]

    def save_to_file(self,filename):
        with open(filename, 'wb') as fh:
            pickle.dump(self, fh)

    def find(self, text):
        f=False
        for n in self:
            if text in self[n].name or text in self[n].describe:
                print(self[n])
                f=True
        if f==False:
            print(f"{YELLOW}{text}{BLUE} is not found{RESET}")



#----------відкриття або створення notepad_dict------

path_different= "..\\my_dir"


#-----------------ця частина робится один раз, створюються всі необхідні папки---


topics= ["video", "audio", "python", "photos","notes"]

if os.path.exists(path_different):
    pass
else:
    os.mkdir(path_different)
    [os.mkdir(os.path.join(path_different, d)) for d in  topics]
path_notes=os.path.join(path_different, "notes")

dir_notes = [os.path.splitext(p)[0] for p in os.listdir(path_notes)]


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



















