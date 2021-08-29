import yaml
#создаем файл .yaml
#hosts_template = [
#    'base my_project',
#    'settings __init__.py,dev.py,prod.py',
#    'mainapp __init__.py,models.py,views.py',
#    'mainapp/templates/mainapp base.html,index.html',
#    'authapp __init__.py,models.py,views.py',
#    'authapp/templates/authapp base.html,index.html'
#    ]
#to_yaml = {'host': hosts_template}

#with open('config.yaml', 'w') as f:
#    yaml.dump(to_yaml, f, default_flow_style=False)
#проверяем что записано в файле
#with open('config.yaml') as f:
#    print(f.read())

import os
settings = {}
with open('config.yaml') as f:
    lines = dict(map(str.split, f.readlines()))

base_dir = lines.pop('base')
for k,v in lines.items():
    os.makedirs(os.path.join(os.curdir, base_dir, k), exist_ok=True)
    print(f'Создаем каталог: {k}')
    for i in v.split(','):
         with open(os.path.join(os.curdir, base_dir, k, i), "w") as f:
             print (f'Создан файл: {i} в каталоге {k}')


