from glob import glob
from sys import argv
from os import rename

script, directory = argv

output_file = open("extracted.csv","w")
exercise_files = glob(directory + "/*.py")
for f in exercise_files:
    new_file_name = f.replace("Exercise ","ex_").replace(" start.",".").replace("-","_").replace("chapter_","chapter-")
    rename(f,new_file_name)
