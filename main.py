import os
import sys
import time
import hashlib
import argparse
import shutil

def get_args():
    """defining the arguments"""
    parser = argparse.ArgumentParser(description='Synchronizing two folders in one way.')
    parser.add_argument("-s",metavar="--source",required=True,help="path to source folder")
    parser.add_argument("-r", metavar="- -duplicate", required=True, help="path to duplicate folder")
    parser.add_argument("-i", metavar="--interval", type=int, default=120, help="synchronization tie in seconds")
    parser.add_argument("-l", metavar="--log", help="path to log file")
    return parser.parse_args()

def get_file_hash(filepath):
    """tried to use md5"""
    with open(filepath,'rb') as f:
        file = f.read()
    return hashlib.md5(file).hexdigest()

def syn_folders(source_path,duplicate_path,log_path):
    if not os.path.exists(duplicate_path):
        os.makedirs(duplicate_path)
"""creating a directory for source and duplicate file"

    source_folder = os.listdir(source_path)
    duplicate_folder = os.listdir(duplicate_path)
    print("source_folder", source_folder)
    print("duplicate_folder", duplicate_folder)


    for item in source_folder:
        source_folder_path = os.path.join(source_path,item)
        duplicate_folder_path = os.path.join(duplicate_path,item)
        if os.path.isfile(source_folder_path):
            if item not in duplicate_folder:
                shutil.copy2(source_folder_path,duplicate_folder_path)
                with open(log_path,'a') as f:
                    f.write(f'copied file:{source_folder_path} to {duplicate_folder_path}\n')
        elif os.path.isdir(source_folder_path):
            syn_folders(source_folder_path,duplicate_folder_path,log_path)
        print("source_folder_path ", source_folder_path)
        print("duplicate_folder_path", duplicate_folder_path)





if __name__ == '__main__':
    args = get_args()

    while True:
        syn_folders(args.s, args.r, args.l)
        time.sleep(args.i)



