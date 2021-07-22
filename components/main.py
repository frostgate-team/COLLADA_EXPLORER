''' Entry point '''

from os import read
import func
import glob

ApplicationConfing = func.ApplicationConfigManager()
ApplicationConfing.Initialize()

open('out/errorlog.txt', 'w').writelines('')
open('out/matlist.txt', 'w').writelines('')

for i in glob.iglob(ApplicationConfing.getMeshlistPath() + '*.txt', recursive=True):
    file = open(i, 'r+').readlines()
    print("Working with: " + i)
    for line in file:
        print("\t Appeal to -> " + line.split('\n')[0])
        parsr = func.DAE_Parser(ApplicationConfing.getWorkPath() + line.split('\n')[0])
        parsr.parse()
        parsr.log()