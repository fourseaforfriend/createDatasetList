import os
import sys

def find_dir(file_dir):
    dirs_list = []
    for root,dirs,files in os.walk(file_dir):
        dirs_list = dirs
        break
    return dirs_list

def writeActionList(findDirPath,dirs_list,saveFilePath):
    trainList = open(saveFilePath+'/'+'train.txt','w')
    valList = open(saveFilePath+'/'+'val.txt','w')
    testList = open(saveFilePath+'/'+'test.txt','w')
    label = open(saveFilePath+'/'+'label.txt','w')
    classID = 0

    for dir in dirs_list:
        for root,dirs,files in os.walk(os.path.join(findDirPath,dir)):
            classLen = len(files)
            trainLen = int(classLen*0.6)
            valLen = int((classLen-trainLen)*0.5) + trainLen
            testLen = classLen
            count = 1
            for file in files:
                if (count <= trainLen):
                    trainList.write(os.path.join(findDirPath,dir,file)+' '+str(classID)+'\n')
                if ((count > trainLen) and (count <= valLen)):
                    valList.write(os.path.join(findDirPath,dir,file)+' '+str(classID)+'\n')
                if ((count > valLen) and (count <= testLen)):
                    testList.write(os.path.join(findDirPath,dir,file)+' '+str(classID)+'\n')
                count += 1
        label.write(dir+' '+str(classID)+'\n')
        classID += 1
    
    label.close()
    trainList.close()
    valList.close()
    testList.close()
    print('Check is done!')

if __name__ == '__main__':
    findDirPath = sys.argv[1] #this is dir's path
    saveDirPath = sys.argv[2] #this is file's path that is include filename 
    dirs_list = find_dir(findDirPath)
    writeActionList(findDirPath,dirs_list,saveDirPath) #saveDirPath is not end with '/'
