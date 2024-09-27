from collections import UserDict
import os
from src.address_book import Field
import pickle
#from address_book import read_from_file

# Color text ON
# RED = "\033[91m"
# GREEN = "\033[92m"
# YELLOW="\033[93m"
# RESET = "\033[0m"
# BLUE = "\033[94m"

# Color text OFF
RED = ""
GREEN = ""
YELLOW = ""
RESET = ""
BLUE = ""

class Different(Field):

    def __init__(self, name, topic, describe="опис" ):
        self.topic = topic
        self.describe = describe
        self.name=name
        self.dir=os.path.join(path_different, topic)
        self.file=os.path.join(self.dir,name)
        try:
            with open(self.file, 'x'):
                pass
        except Exception:
            pass

    def open_different(self):
        os.system(self.file)
    def add_description(self):
        print("add your description to this file, please")
        self.describe=input(">")

    def __str__(self):
        if self.describe=="del":
            return ""
        else:
            return (f"{BLUE} dir:{YELLOW} {self.topic},{BLUE} name:{YELLOW} {self.name}, {BLUE}description:{YELLOW} {self.describe}{RESET}")


class Different_dict(UserDict):
    base_path = os.path.dirname(__file__)
    filename = os.path.join(base_path, "..", "files", "save_different.bin")
    #filename=os.path.join("..\\files", "save_different.bin")

    
    def add_different(self, name, topic):
        a=Different(name,topic)
        #print(a)
        self[name]=a

    def get_all(self):
        for n in self:
            print(self[n])

    def get_all_type(self,type):
        for n in self:
            if self[n].topic==type:
                print(self[n])

    def get_found(self,txt):
        for n in self:
            if txt in self[n].name or txt in self[n].describe:
                print(self[n])

    def save_to_file(self, filename):
        with open(filename, 'wb') as fh:
            pickle.dump(self, fh)


def check_different_files():
    list_files=dict()
    for d in topics:
        list_files[d]=os.listdir((os.path.join(path_different, d)) )

        for fil in list_files[d]:
            if fil in different_dict:
                pass
            else:
                different_dict.add_different(fil,d)
    for fil in  different_dict:
        find=False
        if fil in list_files[different_dict[fil].topic]:
            find=True

        if not find:
            different_dict[fil].describe="del"

    for fil in different_dict:

        if different_dict[fil].describe !="del":
            different_dict_after[fil]=different_dict[fil]

base_path1 = os.path.dirname(__file__)
path_different = os.path.join(base_path1, "..", "my_dir")
#path_different= "..\\my_dir"

#-----------------ця частина робится один раз, створюються всі необхідні папки---

topics= ["video", "audio", "python", "photos","notes"]

if os.path.exists(path_different):
    pass
else:
    os.mkdir(path_different)
    [os.mkdir(os.path.join(path_different, d)) for d in  topics]
path_notes=os.path.join(path_different, "notes")

dir_notes = [os.path.splitext(p)[0] for p in os.listdir(path_notes)]

def read_from_file(file):
    with open(file, 'rb') as fh:
        return pickle.load(fh)

base_path = os.path.dirname(__file__)
filename = os.path.join(base_path, "..", "files", "save_different.bin")
#filename=os.path.join("..\\files", "save_different.bin")
try:
    different_dict = read_from_file(filename)
except Exception:
    different_dict=Different_dict()


topics= ["video", "audio", "python", "photos"]


# при запуску
different_dict_after = Different_dict()
check_different_files()
different_dict=different_dict_after
def get_dict():
    return different_dict













