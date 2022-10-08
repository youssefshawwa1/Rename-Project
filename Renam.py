#Python program to find and rename TV Series Episods with Subtitle
#Works only .mp4 .mkv .srt
#it will remove all the extra characters in the name 
#The.Lord.of.the.Rings.The.Rings.of.Power.S01E06.1080p.AMZN.WEBRip.DDP5.1.x264-SMURF.mp4
#=> The Lord Of The Rings The Rings Of Power S01E06.mp4
from ast import And
import os, re, shutil
# import re
# import shutil
try:
    #enter the path of a dir contains files 
    #example of path F:\Hawkeye
    #(excpectig video and subtitles in the dir)
    path = str(input('Enter Folder Path: '))  + '\\'
    filesDir = os.listdir(path) 
    group = []
    #loob in the dir and find all the files in it
    for file in filesDir:
        #find out if the file is a video or subtitle
        findNameandSEandType = re.findall('(.+)([S|s][0-9]+[E|e][0-9]+).*(.mp4$|.mkv$|.srt$)', file)
        #if subtitle or video rename it to a new name
        if findNameandSEandType:
            finalNewName = str(findNameandSEandType[0][0]).title().replace('.', ' ') + str(findNameandSEandType[0][1]).upper()+ str(findNameandSEandType[0][2])
            if path + file == path + finalNewName:
                print('No Need To Rename:   ', file)
                continue
            else:
                try:
                    os.rename(path + file, path + finalNewName)
                    print('Just Renamed:    ', file)
                except:
                    print('Error Can Not Rename:   ', file)
        #if not a video or subtitle put it in a list named group
        elif not findNameandSEandType: 
            group.append(file)
    #if there was any thing not a video or subtitle 
    if group:
        #you have a choice to delete the other files and dir
        #if the program did not recognize them as 
        #subtitle or video .mp4 .mkv .srt
        print('\n\nThe Program Did Not Recognize these as .mp4 or .mkv or .srt\nDo You Want To Delete These?  \n\n')
        for thing in group:
            print('---->', thing)
        respone = str(input('\n\nIf yes type yes:   '))
        if respone == 'yes':
            for thing in group:
                #try delete the thing in the group of not recognize
                #as a normal file
                try:
                    os.remove(path + thing)
                    print('****Just Deleted:  ', thing)
                #if not 
                except:
                    #try as an emty folder
                    try:
                        os.rmdir(path + thing)
                        print('****Just Deleted:  ', thing)
                    #if not 
                    except:
                        #try as a not emty folder 
                        try:
                            shutil.rmtree(path + thing, ignore_errors=True)
                            print('****Just Deleted:  ', thing)
                        #if not print messige to the user
                        except:
                            print('Error Can Not Delete:   ', thing)

        else:
            exit
except:
    print('You did Not Enter a Path !! Please Try Again !!!!')
print('\n\n\nFinish..\nExiting...')