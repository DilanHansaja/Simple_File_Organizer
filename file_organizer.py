from pathlib import Path
import shutil
import os

media_extensions = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.heif', '.heic', '.raw','.jfif'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm', '.mpeg', '.3gp', '.m4v', '.ts'],
    'audios': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma', '.opus', '.aiff', '.amr'],
    'documents': ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.rtf', '.odt', '.ods', '.odp', '.csv', '.md'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso'],
    'executables': ['.exe', '.msi', '.bat', '.sh', '.apk', '.dmg'],
    'codes': ['.html', '.css', '.js', '.json', '.xml', '.java', '.py', '.c', '.cpp', '.cs', '.php', '.rb', '.go', '.ts', '.sql'],
    }

duplicates=[]

folders = {"Images":None,"Videos":None,"Audios":None,"Documents":None,"Archives":None,"Executables":None,"Codes":None,"Other":None}

def scanDirectory(directory_path):

    path = Path(directory_path)

    number_of_files = len(os.listdir(directory_path))

    if number_of_files > 0 :

        increment = 100 / number_of_files

        percentage = 0

        for file in path.iterdir():

            scanned_file = Path(file)

            if scanned_file.suffix in media_extensions["images"]:

                create_folder("Images", directory_path, scanned_file)

            elif scanned_file.suffix in media_extensions["videos"]:

                create_folder("Videos", directory_path, scanned_file)

            elif scanned_file.suffix in media_extensions["audios"]:

                create_folder("Audios", directory_path, scanned_file)

            elif scanned_file.suffix in media_extensions["documents"]:

                create_folder("Documents", directory_path, scanned_file)

            elif scanned_file.suffix in media_extensions["archives"]:

                create_folder("Archives", directory_path, scanned_file)

            elif scanned_file.suffix in media_extensions["executables"]:

                create_folder("Executables", directory_path, scanned_file)

            elif scanned_file.suffix in media_extensions["codes"]:

                create_folder("Codes", directory_path, scanned_file)

            else:

                create_folder("Other", directory_path, scanned_file)

            percentage += increment
            print(f'Progress: {int(percentage)}%', end='\r')

        print(f'Completed: 100%', end="\r")
        print()

        checkDuplicates()

    else:
        print("Provided directory is empty!")

def create_folder(folder_name,directory_path,scanned_file):

    if folders.get(folder_name) is None:

        folders[folder_name]= Path(directory_path,folder_name)
        folders[folder_name].mkdir(0o777, True, True)

        moveFile(scanned_file, folders[folder_name])

    else:
        moveFile(scanned_file, folders[folder_name])


def moveFile(source,destination):

    def check_if_already_exists():

        check_path = Path(destination,source.name)

        if check_path.exists():

           duplicates.append(source)

        else:
            shutil.move(source,destination)
            #print(f'{source.name} is moved to {destination}')

    check_if_already_exists()

def checkDuplicates():

    if len(duplicates) >0:
        print(f'{len(duplicates)} Duplicate files were found.\nThey are not affected by the program.')

def initialize():

    while True:

        provided_path = input('Enter the directory path  to organize files : ')
        print()
        confirmation = input('Please make sure your path have only files in it.\nIf folders found they will move to the folder named "Other" after organized.\nContinue (y/n) :').lower()
        print()

        if confirmation.__eq__("y"):

            path = Path(provided_path)
            if path.exists():
                scanDirectory(provided_path)
                print()
                break
            else:
                print("Invalid path!")
                print()
                continue

        elif confirmation.__eq__("n"):
            print("Thank you for using file organizer!")
            break
        else:
            print("Invalid Command!")
            print()
            continue

initialize()