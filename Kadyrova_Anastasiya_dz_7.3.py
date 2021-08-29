import os

SRC_FOLDER = 'my_project'
DST_FOLDER = 'templates'

dirs = os.walk(SRC_FOLDER)
for x, y, _ in dirs:
    for i in y:
        new_path = os.path.join(os.curdir, DST_FOLDER, os.sep.join(x.split(os.sep)[1:]), i)
        print(x.split(os.sep))
        os.makedirs(new_path, exist_ok=True)