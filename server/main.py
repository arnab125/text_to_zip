import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'
print(source_path)

postfix = [1, 2, 3]

source_objects = glob.glob(source_path)
print(source_objects)

object_paths = source_objects[0]
print(object_paths)
shutil.copy(object_paths, '.')
object_name = object_paths.split('\\')[-1].split('.')
print(object_name)

prefix = object_name[0]
print(prefix)
postfix2 = object_name[1]
print(postfix2)

for item in range(len(postfix)):
    filename = prefix + '_' + str(item) + '.' + postfix2
    print(item)
    print(filename)
    shutil.copy(object_paths, f"{destination_path}/{filename}")

os.remove(object_paths)
to_be_deleted =object_paths.split('\\')[-1]
os.remove(to_be_deleted)
