import csv
import os
import shutil

try:
    path = './reorganization'
    if not(os.path.isdir(path)):
        os.mkdir(path)

    # open csv
    with open('pokemon.csv', newline='') as csvfile:
        # read
        rows = csv.reader(csvfile)
        for row in rows:
        # row[0]:主檔名、row[1]:分類
            type_folder_path=f'{path}/{row[1]}'
            if not(os.path.isdir(type_folder_path)):
               os.mkdir(type_folder_path)
            print(f'./images/{row[0]}.png', '--->', f'{type_folder_path}/{row[0]}.png')
            
            src=f'./images/{row[0]}.png'
            dst=f'{type_folder_path}/{row[0]}.png'
            if os.path.isfile(src):
                shutil.copyfile(src, dst)
            else:
                continue
            


except OSError:
    print(f'Failed')
else:
    print(f'Success')
