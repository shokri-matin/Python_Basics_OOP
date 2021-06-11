import os

print(os.getcwd())
# 'C:\Program Files\PyScripter'

print(os.listdir())

print(os.listdir('C:\\'))

os.mkdir('test')
os.rename('test', 'new_one')
os.remove('old.txt')
os.rmdir('new_one')

import shutil
shutil.rmtree('test')

os.listdir()