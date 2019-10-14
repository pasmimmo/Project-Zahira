import os, sys, subprocess, shutil, ffmpy
from multiprocessing import Process

currDir=str(os.getcwd())
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
    dirName = "/home/pi/Desktop/tmp"#currDir+tmpFolder+"/"
    fileName= "img"+str(iterator)+".png"
    newName = dirName+fileName
    subprocess.call(['ffmpeg', '-i', fname, '-vf', 'scale=1920:1080', newName ])
    #Scrittura log.txt
    if len(fname)<12:
        fname+="\t"
    logFile.writelines(fname+"\t\t convertito in \t\t"+fileName+"\n")
    iterator+=1

def convertImages(directory):
    it=0
    for item in os.listdir(directory):
        #resize_files(item)
        fname=item
        newName="img_"+str(it)+".jpg"
        print(item)
        subprocess.call(['ffmpeg', '-i', item, '-vf', 'scale=1920:1080', newName ])


def slideShowcreate(dir):
    os.chdir(dir)
    subprocess.call(["ffmpeg","-r","1/5","-pattern_type","glob","-i","*.png","-c:v","libx264","-r", "30", "-pix_fmt", "yuv420p", slideShowName])

def cleanTempFiles():
    os.rename(os.getcwd()+"/"+slideShowName, currDir+"/"+slideShowName)
    shutil.rmtree(currDir+tmpFolder)
    os.mkdir(currDir+tmpFolder)
    logFile.writelines("tempfiles eliminati\n")

def startSlideShow(dir):
    os.chdir(dir)
    subprocess.call(["vlc", "-f", "--loop", slideShowName])
    #logFile.writelines("avvio slideshow")
#convertImages("/home/pi/Desktop/imgSources")