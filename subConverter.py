import sys, re, os

def convertType(path, fileName):
    findSRT2Convert = re.search('.+.srt$', fileName)
    if findSRT2Convert:
        try:
            srtFile = path + fileName
            subtitlefile = open(srtFile, "r",  encoding='utf8')
            vttName = fileName.replace('.srt', '.vtt')
            isVTTExist = os.path.isfile(path + vttName)
            if isVTTExist == True:
                print('No Need To Convert:    SRT TO VTT')
            else:
                convertedFile = open(path + vttName, "w",  encoding='utf8')

                lineArray = subtitlefile.read().splitlines()    
                
                convertedFile.write('WEBVTT\n\n')

                i = 1
                while i < len(lineArray):
                    if not lineArray[i].isdigit():
                        convline = re.sub(',(?! )', '.', lineArray[i])
                        test = re.search(".*({.*}).*", convline)
                        if test:
                            convline = re.sub("{.*}", '', test.group())
                        convertedFile.write(convline + '\n')
                    
                    i += 1
                print('Just Converted:    ', fileName, '   To >  ',vttName )
                convertedFile.close()
        except:
            print('Error With SRT To VTT:    ')