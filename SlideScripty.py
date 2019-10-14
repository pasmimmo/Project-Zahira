import os
import subprocess
import shutil
from multiprocessing import Process

currDir=os.getcwd()
imgSources="/imgSources"
tmpFolder="/tmp"
iterator=0
logFile= open(currDir+"/log.txt","w")
slideShowName="slideshow.mp4"
logFile.writelines("Benvenuti nel Log di SlideScripty, \n")

def createWorkingDirectory():
        print("Creo le directories necessarie")
        os.mkdir(currDir+imgSources)
        print(imgSources+ ",\tinserisci le immagini sorgente in questa directory")
        os.mkdir(currDir+tmpFolder)
        print(tmpFolder+",\tdirectory dei files temporanei")
        print("posiziona le immagini in "+imgSources + ",quindi riesegui lo script")

def resize_files(fname):
    global iterator
    dirName = currDir+tmpFolder+"/"
    fileName= "img"+str(iterator)+".png"
    newName = dirName+fileName
    subprocess.call(['ffmpeg', '-i', fname, '-vf', 'scale=1920:1080', newName, '-y' ])
    #Scrittura log.txt
    if len(fname)<12:
            fname+="\t"
    logFile.writelines(fname+"\t\t convertito in \t\t"+fileName+"\n")
    iterator+=1

def convertImages(dir):
    for item in os.listdir(dir):
        resize_files(item)

def slideShowcreate(dir):
        os.chdir(dir)
        subprocess.call(["ffmpeg","-framerate","1/5","-pattern_type","glob","-i","*.png", slideShowName])
def cleanTempFiles():
        os.rename(os.getcwd()+"/"+slideShowName, currDir+"/"+slideShowName)
        shutil.rmtree(currDir+tmpFolder)
        os.mkdir(currDir+tmpFolder)
        logFile.writelines("tempfiles eliminati\n")

def startSlideShow(dir):
        os.chdir(dir)
        subprocess.call(["cvlc", "-f", "--loop", slideShowName])
        #logFile.writelines("avvio slideshow")  


value=0
pid=0
for directory in os.listdir(currDir):
        scrDir=imgSources.replace("/","")
        if directory==imgSources.replace("/",""):
                value+=1
        if directory == tmpFolder.replace("/",""):
                value+=1
                
if value<1:
        print("Cartelle di lavoro non presenti")
        createWorkingDirectory()
        print("inizzializzazione directories completata")
else:
        convertImages(os.chdir(currDir+imgSources))
        slideShowcreate(currDir+tmpFolder)
        cleanTempFiles()
        p=Process(target=startSlideShow,args=(currDir,))
        p.start()
        logFile.writelines("pid="+str(p.pid))
        logFile.close()
