import os


root_dir = 'D:/cooked_data/'
folder_dir_list = os.listdir(root_dir)
for f in folder_dir_list:
    file_list = os.listdir(root_dir + f)
    for file in file_list:
        newname = file[:-5] + '@eng' + file[-5:]
        print(root_dir + f + '/' + file, root_dir + f + '/' + newname)
        os.rename(root_dir + f + '/' + file, root_dir + f + '/' + newname)