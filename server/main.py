import glob
import shutil
import os
from zipfile import ZipFile
import time

source_path = '../source/*'
destination_path = '../destination'
server_path = '../server'

"""print(server_path)
print(destination_path)
print(source_path)"""

postfix = [1, 2, 3]

while True:
    source_objects = glob.glob(source_path)
    #print(source_objects)
    if len(source_objects) > 0:
        for source_object in source_objects:
            if ".py" in source_object:
                #print(source_object)
                try:
                    print("This is the", source_object.split('\\')[-1], "file found in source folder :")
                    exec(open(source_object).read())
                    print("""
                    """)
                    time.sleep(3)
                except Exception as e:
                    print("ERROR HANDLED : ", e, " in ", source_object,"and", source_object.split('\\')[-1], "PROGRAM TERMINATED")
                    print("""
                            """)
                    time.sleep(3)
                #os.remove(source_object)

        #time.sleep(2)

        if ".txt" in source_objects[0]:
            object_paths = source_objects[0]
            print("This is the", object_paths.split('\\')[-1], "file found in source folder :")
            print("")
            #print(object_paths)
            with open(object_paths, 'r') as f:
                content = f.readlines()
                #print(content)
            shutil.copy(object_paths, '.')
            object_name = object_paths.split('\\')[-1].split('.')
            #print(object_name)

            prefix = object_name[0]
            #print(prefix)
            postfix2 = object_name[1]
            #print(postfix2)

            zip_file = f"{prefix}_combined.zip"

            index = 10

            for item in range(len(postfix)):

                filename = prefix + '_' + str(item) + '.' + postfix2
                #print(item)
                #print(filename)
                shutil.copy(object_paths, f"{server_path}/{filename}")
                with open(f"{server_path}/{filename}", 'w') as file:
                    for i in range(index):
                        file.write(content[i])
                with ZipFile(zip_file, 'a') as zip:
                    zip.write(filename)
                    time.sleep(.5)
                    print(f"{filename} added to {zip_file}")
                    os.remove(filename)
                index += 10

            shutil.copy(f"{server_path}/{zip_file}", f"{destination_path}/{zip_file}")
            os.remove(f"{server_path}/{zip_file}")
            with ZipFile(f"{destination_path}/{zip_file}", 'r') as zipOBJ:
                #print(zipOBJ.namelist())
                zipOBJ.extractall(destination_path)
                print("")
                print(f"{zip_file} extracted to {destination_path} successfully")
                print("")

                os.remove(object_paths)
                to_be_deleted = object_paths.split('\\')[-1]
                os.remove(to_be_deleted)
                time.sleep(4)

        else:
            print("No .txt file found in source folder")
            print("")
            print("Waiting for .txt file to be added to source folder")
            print("")
            time.sleep(3)


        #time.sleep(5)
    else:
        print("No files found in source folder")
        print("")
        time.sleep(3)