#Python program to find and rename TV Series Episods with Subtitle
#Works only .mp4 .mkv .srt
#it will remove all the extra characters in the name 
#The.Lord.of.the.Rings.The.Rings.of.Power.S01E06.1080p.AMZN.WEBRip.DDP5.1.x264-SMURF.mp4
#=> The Lord Of The Rings The Rings Of Power S01E06.mp4
import os, re, shutil
from subConverter import convertType as SRT2VTT
# import re
# import shutil
def ReMovDelCon(settings):
    print('You Can Type Exit or press Escape To Exit The RENAM Program.\n')
    varForCounting = 0 
    # the settings if default then the program will move and rename folder withou asking
    if settings == True:
        print('Default Settings in the Rename: ')
    elif settings == False:
        settings = False
        print('Costom Settings in the Rename: ')
        # looping because if I want to enter multiple locations
    while  True:
        #user input or the path to the content 
        # must be similar to Z:\movies\GodFather
            userInput = str(input('Enter Folder Path or Exit To Exit: '))
                
            # if the user enter enter os escape or exit then exit the loop
            if len(userInput) < 1 or userInput == 'Exit' or userInput == 'exit':
                print('\n\n\nExiting...\nGoodBye.')
                break
            # else precede the process
            else:
                try:
                    #(excpectig video and/or/without subtitles in the dir)
                    path =   userInput + '\\'
                    pathForRenameDir = userInput
                    # list all files and directories in the folder that the user enter
                    filesDir = os.listdir(path) 
                    # creating a group if the files not recognize as 
                    # tv episodes or movies 
                    group = []
                    #loob in the dir and find all the files in it
                    for file in filesDir:
                        #find out if the file is a episode/subtitle of an episode
                        # pattern for episode is name before the S (season)
                        #  and number and E (episode) and number
                        findNameandSEandType = re.findall('(.+)([S|s][0-9]+[E|e][0-9]+).*(.mp4$|.mkv$|.srt$|.vtt)', file)
                        # find out if the file is a movie/subtitle of a movie
                        #pattern for movie is nameo of the movie year other
                        #  details if exist .mp4 .mkv .srt .vtt
                        findMovie =  re.findall("(.*)([(0-9]{4})[.| ].*(mp4$|mkv$|srt$|vtt)", file)
                        # find if there is an image in the folder 
                        isImage = re.search('.*.jpg$',file)                    
                        #if the program finds an episode/subitile of an episode then >
                        if findNameandSEandType:
                            # ensure that the fmovie is false becuase in 
                            # this time we found an episode not a movie
                            fMovie = False
                            # if the extracted name ends with mp4 or 
                            # mkv then it will become the name of the folder
                            isMp4 = re.search('.*.mp4$|.mkv$', findNameandSEandType[0][2])
                            if isMp4:
                                fileType = ".mp4"
                                nameForFolder = isMp4.group()
                            else:
                                fileType = findNameandSEandType[0][2]
                            #count how much files
                            varForCounting += 1 
                            #extract the final name 
                            finalNewName = str(findNameandSEandType[0][0]).title().replace('.', ' ') + str(findNameandSEandType[0][1]).upper()+ str(fileType)
                            # if the extracted name ends with mp4 or 
                            # mkv then it will become the name of the folder
                            isMp4 = re.search('.*.mp4$|.mkv$', finalNewName)
                            if isMp4:
                                nameForFolder = isMp4.group()
                            # if the path = the new path then there is no need to rename the file
                            # continue to another file in the folder
                            if path + file == path + finalNewName:
                                print('No Need To Rename:   ', file)
                                SRT2VTT(path, finalNewName)
                                continue
                            # if not the same then try to rename the file to the new name
                            else:
                                try:
                                    os.rename(path + file, path + finalNewName)
                                    # here call the srt to vtt funcion 
                                    # and insert the path and the name
                                    # if the name ends with srt it 
                                    # will automatically convert the file to vtt
                                    SRT2VTT(path, finalNewName)
                                    print('Just Renamed:    ', file, '\nTo >  ',finalNewName )
                                except:
                                    # if there was a problem with renaming 
                                    print('Error Can Not Rename:   ', file)
                        #here if the file is a movie/subtitle of a movie
                        elif findMovie:
                            # the fmovie is true becuase it is a movie that the program found 
                            # will explain why I used fMovie
                            fMovie = True
                            # extention type
                            exType = str(findMovie[0][2])
                            # if the extention of the file was mp4 or 
                            # mkv then the final name will be the folder name
                            if exType == 'mp4':
                                nameForFolder = str(findMovie[0][0]).title().replace('.', ' ') + str(findMovie[0][1])  
                                fileType = findMovie[0][1]
                            elif exType == 'mkv':
                                nameForFolder = str(findMovie[0][0]).title().replace('.', ' ') + str(findMovie[0][1])  
                                fileType = "mp4"
                            else:
                                fileType = findMovie[0][1]
                            # if the old path = the new path then there is no need to rename
                            # extract the final name
                            finalNewName = str(findMovie[0][0]).title().replace('.', ' ') + str(findMovie[0][1]) + '.' + str(fileType)


                            if path + file == path + finalNewName:
                                SRT2VTT(path, finalNewName)
                                print('No Need To Rename:   ', file)
                                continue
                            else:
                            # if the old path was not the same as the new path
                            # then try to rename and convert srt if exists
                                try:
                                    os.rename(path + file, path + finalNewName)
                                    SRT2VTT(path, finalNewName)
                                    print('Just Renamed:    ', file, '\nTo >  ',finalNewName )
                                except:
                                    print('Error Can Not Rename:   ', file)
                        # if there is an image then take the name of the image
                        elif isImage:
                            imageName = isImage.group()
                        else: 
                            group.append(file)
                    #if there was any thing not a video or subtitle 
                    if group:
                        #you have a choice to delete the other files and dir
                        #if the program did not recognize them as 
                        #subtitle or video .mp4 .mkv .srt
                        print('\n\nThe Program Did Not Recognize these as .mp4 or .mkv or .srt\nDo You Want To Delete These?  \n\n')
                        for thing in group:
                            print('---->', thing)
                        respone = str(input('\n\nIf Yes type: yes  \n'))
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
                                        #try as not an emty folder 
                                        try:
                                            shutil.rmtree(path + thing, ignore_errors=True)
                                            print('****Just Deleted:  ', thing)
                                        #if not print messige to the user
                                        except:
                                            print('Error Can Not Delete:   ', thing)
                    # it is another way of saing if there was an episode/subtitle of an episode
                    if varForCounting:
                        # the main is the server or my server location 
                        # to be provided to the program so I don't have to write 
                        # the locatoin over and over if it was for the website or generating json
                        main = 'Z:/dist/content/tv/'

                        try:
                            # if there was only two files in the folder
                            if varForCounting <= 2:
                                # there take the full name like "wednsday s01e03" for the folder name
                                tvSeriesName = re.search('(.+)([S|s][0-9]+[E|e][0-9]+)', nameForFolder).group()
                                dirOldName = os.path.basename(pathForRenameDir)
                                dirNewPath = pathForRenameDir.replace(dirOldName, nameForFolder)
                            # if ther was more than 2 files in the folder
                            else:
                                # then only take the tv series name for the folder name like "wednsday"
                                tvSeriesName = re.search('(.+[S|s][0-9]+)', nameForFolder).group()
                                dirOldName = os.path.basename(pathForRenameDir)
                                dirNewPath = pathForRenameDir.replace(dirOldName, tvSeriesName)
                            # make sure that the counting is zero 
                            varForCounting = 0
                            # if the settings was true mean the deafult settings are
                            # applied then in this case I made the user input is yes
                            if settings == True:
                                userInputTF = 'yes'
                            # here if the settings are costome so the program will ask
                            # if you want to rename the folder and move it
                            else:
                                userInputTF =str(input('\nRenam The folder And Move: '))
                            if userInputTF == 'yes':
                                try:
                                    # if the old path = the new path then
                                    # there is no need for renaming the folder
                                    if pathForRenameDir == dirNewPath:
                                        print('\nNo Need To Rename The Folder.')
                                    # else rename the folder
                                    else:
                                        os.rename(pathForRenameDir, dirNewPath)
                                        print('\n\n\nJust Renamed Folder: ', dirOldName, '\nTo > ', tvSeriesName)
                                    # here is the main path is wher the program will 
                                    # move the final tv sereis to it
                                    mainPath = dirNewPath.replace(tvSeriesName, '')
                                    # extract the tv series name
                                    tvName = re.findall('(.*)( [S|s][0-9]+)', tvSeriesName)
                                    # if the settings was true mean default settings
                                    if settings == True:
                                        # check if ther is a directory in the same path 
                                        isdir = os.path.isdir(main + tvName[0][0])
                                        # directory dirC here will be the main path the server 
                                        # path because the settings are defaults 
                                        dirC = main
                                    # if the setting was costom
                                    else:
                                        # the main become the mainpath means will rename folder and create 
                                        # new folder and move it in the same location
                                        main = mainPath
                                        # get the directory name
                                        dirName = os.path.dirname(main)
                                        # get the base directory name
                                        baseName = os.path.basename(dirName)
                                        # replase the base name to the new folder name
                                        dirC = dirName.replace(baseName, tvName[0][0])
                                        # check if ther is a folder named the same
                                        isdir = os.path.isdir(dirC)
                                    # if there is a folder named the same name
                                    if isdir == True:
                                        try:
                                            # then no need to create folder
                                            print('No Need To Create Folder: ')
                                            # if the folder is already in its plase 
                                            # no need to move the folder
                                            if dirNewPath == dirC + '\\' + tvSeriesName:
                                                print('No need To Move the Folder: \n')
                                            # if the folder wasn't in its place 
                                            # then move it 
                                            else:
                                                shutil.move(dirNewPath, main + tvName[0][0] + '\\' + tvSeriesName)
                                                print('\n\n\nJust Moved Folder: ', dirNewPath.replace('/', '\\'), '\nTo > ', main.replace('/', '\\') + tvName[0][0] + '\\' + tvSeriesName)
                                        except:
                                            print('Error With Moving:    ')
                                    # if ther wasn't folder named the same then
                                    elif isdir == False:
                                        try:
                                            # create folder named the tv series name 
                                            # without season or episode
                                            os.mkdir(main + tvName[0][0])
                                            print('\n\n\nJust Created Folder: ', main + tvName[0][0])
                                            # move the folder 
                                            shutil.move(dirNewPath, main + tvName[0][0] + '\\' + tvSeriesName)
                                            print('\n\n\nJust Moved Folder: ', dirNewPath.replace('/', '\\'), '\nTo > ', main.replace('/', '\\') + tvName[0][0] + '\\' + tvSeriesName)
                                        except:
                                            print('Error With Moving:    \n')
                                # here if there was only 2 files in the folder then 
                                # it is probaply one episode and suptitle
                                # if ther was folder named the same create new folder and
                                # generate a number in the end of the name
                                except:
                                    try:
                                        i = 0 
                                        while i <= 10:
                                            try:
                                                randomN = '.' + str(i)
                                                
                                                if pathForRenameDir == dirNewPath + randomN:
                                                    print('\nNo Need To Rename The Folder.\n')
                                                    break
                                                else:
                                                    os.rename(pathForRenameDir, dirNewPath + randomN)
                                                    print('\n\n\nJust Renamed Folder: ', dirOldName, '\nTo > ', tvSeriesName + randomN + '\n')
                                                    break
                                            except:
                                                i += 1
                                                continue
                                    except:
                                        print('Error Can Not Rename:   \n', dirOldName)
                        except:
                            print('Error Can Not Rename Folder.\n')

                    # renaming the image if it exists
                    try:
                        if imageName[0].lower() == nameForFolder[0].lower():
                            oldImage = pathForRenameDir + '\\' + imageName
                            newImage = pathForRenameDir + '\\' + nameForFolder + '.jpg'
                            try:
                                isImageExist = os.path.isfile(newImage)
                                if isImageExist:
                                    print('No Need To Rename The Image:    \n')
                                else:
                                    os.rename(oldImage, newImage)
                                    print('\n\n\nJust Renamed Image: ', imageName, '\nTo > ', nameForFolder + '.jpg\n')  
                            except:
                                print('\nError Renaming The Image:     \n')
                    except:
                        print('No Image \n')
                    # another way to say that the file was a movie/subtitle of a movie
                    if fMovie == True:
                        # the server folder
                        main = 'Z:/dist/content/movie/'
                        try:
                            # get the folder name of the files
                            dirOldName = os.path.basename(pathForRenameDir)
                            dirNewPath = pathForRenameDir.replace(dirOldName, nameForFolder)
                            # get main path  of the folder > the father folder
                            mainPath = pathForRenameDir.replace(dirOldName, '')
                            # if default settings renaming is automatically applied
                            if settings == True:
                                userInputTF = 'yes'
                            # if costom settings ask the user if he want to rename the folder
                            else:
                                userInputTF =str(input('\nRenam The folder: '))
                            if userInputTF == 'yes':
                                try:
                                    if pathForRenameDir == dirNewPath:
                                        print('\nNo Need To Rename The Folder.\n')
                                    else:
                                        os.rename(pathForRenameDir, dirNewPath)
                                        print('\n\n\nJust Renamed Folder: ', dirOldName, '\nTo > ', nameForFolder + '\n')
                                    if settings:
                                        try:
                                            if dirNewPath == main.replace('/', '\\') + nameForFolder:
                                                print('No need To Move the Folder: \n')
                                            else:
                                                try:
                                                    shutil.move(dirNewPath, main)
                                                    print('\n\n\nJust Moved Folder: ', dirNewPath, '\nTo > ', main + '\n')
                                                except:
                                                    print('Error When Moving:    \n')
                                        except:
                                            print('Error When Moving:    \n')
                                except:
                                    print('Error With Rename Move:    \n')
                        except:
                            print('Error Can Not Rename Folder.\n')
                        
                except:
                    print('You did Not Enter a Path !! Please Try Again !!!!\nYou Can Type Exit To Exit The Program.\n')
                print('\nFinish..\n\n\n\n\n')