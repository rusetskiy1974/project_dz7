import os
import sys
from pathlib import Path
import shutil
from  tools import normalize, make_dir_for_search_files, select_folder, del_empty_fold, extension_files, unknow_ext_files,search_files


def parse_folder(path, level = 1):   # обхід папок через модуль pathlib
    path = normalize(path, True)
    p = Path(path)
    movin_files(p)
        
    
    for f in p.iterdir():
        
        if f.is_dir() and  f.name not in search_files.keys():
            parse_folder((path +'\\'+ f.name), level+1)
            
            
def movin_files (folder_n):
    for f in folder_n.iterdir():
        if f.is_file():
            
            mov_fil = select_folder(f.name)
            
            f_name =  normalize(f.name)
           
            new_way = search_path + '\\' + str(mov_fil) + '\\' + f_name
            
            if mov_fil:
                if mov_fil != 'archives':
                      shutil.move(f, new_way) 
                else:
                    shutil.unpack_archive(f, new_way.rsplit('.')[-2])
                    Path(f).unlink()

             
def start ():
    global search_path
    try:
     
        search_path = sys.argv[1]
                    
        if os.path.exists(search_path):
        
            search_path = normalize(search_path, True)
            print (search_path)
                                    
            make_dir_for_search_files(search_path)
                    
                    
            parse_folder(search_path)

            del_empty_fold(search_path)

            print('Списки знайдених  файлів :', '\n') 
            
            for value in search_files.items():
                print (value)


            print ('Include extension : ', extension_files)
            print ('Unknown extension : ', unknow_ext_files)
            return
        else:
            print ('Incorrect Path > try again ')  
            return
        
    except:
        print ( 'Incorrect Path > try again ')
    




if __name__ == '__main__':
    
    start()
   