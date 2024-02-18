import os
import shutil

from_dir="C:/Users/malli/Downloads"
to_dir="C:/Users/malli/Documents"
list_of_file=os.listdir(from_dir)
print(list_of_file)
for file_name in list_of_file:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension=="":
        continue
    if extension in ['.pdf', '.txt', '.doc', '.docx','.pptx']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)


        


