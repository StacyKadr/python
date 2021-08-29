
import os.path
project_path = 'my project'
path = ['settings', 'mainapp', 'adminapp', 'authapp']

for d in path:
    os.makedirs(os.path.join(os.curdir, project_path, d), exist_ok=True)