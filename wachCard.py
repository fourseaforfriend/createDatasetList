import os
import random
import linecache
import sys

def washSave(filePath,savePath):
    f = open(filePath,'rU')
    count = len(f.readlines())
    s = range(1,count+1)

    for i in s:
        s1 = random.randint(0,count-1)
        s2 = random.randint(0,count-1)
        s[s1],s[s2] = s[s2],s[s1] # change its
    
    
    saveFile = open(savePath,'w')
    for i in s:
        saveFile.write(linecache.getline(filePath,i))

    f.close()
    saveFile.close()
    print('Process is done!')

if __name__ == '__main__':
    filePath = sys.argv[1]
    savePath = sys.argv[2]
    washSave(filePath,savePath)
