
import os, re, json, time
from imgCreater import imgCreater as img
from api import tvMovieapi
def jsonCreater(default):
    if default is True:
        jname = 'main'
        mainPath = 'Z:\dist\content'
    else:
        mainPath = str(input("Enter Folder Path To Create JSON: ")) 
        if len(mainPath) < 1:
            mainPath = 'Z:\dist\content'
        elif mainPath == 'exit':
            print('exiting the JSON Creater')
        
        jname = str(input("\nEnter The Name of The JSON File You Want: "))
        if len(jname) < 1:
            jname = 'main'
        elif jname == 'exit':
            print('exiting the JSON Creater')

            
    #for movies 
    try:
        moviesPath = mainPath + "\\movie"
        filesDir = os.listdir(moviesPath) 
        i = 0
        movies = {}
        for file in filesDir:
                    try:
                        findMovie =  re.findall("(.*)([(0-9]{4}).*", file)
                        if findMovie:
                            modified = os.path.getmtime(moviesPath + "\\" + file)
                            modifiedTime =   time.ctime(modified)
                            modifiedTimeStr = time.strptime(modifiedTime)
                            finalModifiedTime = time.strftime("%Y-%m-%d %H:%M:%S", modifiedTimeStr)
                            name = str(findMovie[0][0]).strip()
                            year = str(findMovie[0][1]).strip()
                            #here you put the api
                            Details = tvMovieapi(name, year)
                            isImage = os.path.isfile(moviesPath + '\\' + file + "\\" +file +'.jpg')
                            if isImage == False:
                                img(moviesPath + '\\' + file, Details["Poster"], file)
                            movies[name + " " + year] = {"name":name, "year":year,"type":"Movie", "last Modified":finalModifiedTime,"Details":Details}
                        else:
                            continue
                    except:
                        continue
        print("\nDone with JSON Movies!! ", len(movies))
        movieSort = sorted(movies.items(),key = lambda x:x[1]['last Modified'], reverse=True)
        newMovie = dict()
        for items in movieSort:
            newMovie[items[0]] = items[1]
    except:
        print("\nError With JSON Movies!!")
    #for tv
    try:
        l =0
        tvs = {}
        tvPath = mainPath + "\\tv"
        filesDir = os.listdir(tvPath) 
        for file in filesDir:
            try:
                tvDir = tvPath + "\\" + file
                tvDirList = os.listdir(tvDir)
                modified = os.path.getmtime(tvPath + "\\" + file)
                modifiedTime =   time.ctime(modified)
                modifiedTimeStr = time.strptime(modifiedTime)
                finalModifiedTime = time.strftime("%Y-%m-%d %H:%M:%S", modifiedTimeStr)
                #here you put the api
                                        #here you create a picture from the object api link
                        # print(f"{tvPath}\\{file}\\{file}.jpg")
                name = file
                Details = tvMovieapi(name, '')
                # if l == 18:
                #     print(movieDetails)
                # print(moviesPath + '\\' + file)
                # print(file + " test")
                isImage = os.path.isfile(tvPath + '\\' + file + "\\" +file +'.jpg')
                if isImage == False:
                    img(tvPath + '\\' + file, Details["Poster"], file)
                tvs[file] = {"Seasons": {}, "type":"TV", "last Modified":finalModifiedTime,"year":'',
                    "Details":Details}
                for season in tvDirList:
                    try:
                        tvSeasonsDir = tvDir + "\\" + season
                        tvSeasonsDirList = os.listdir(tvSeasonsDir)
                        findSeason = re.findall('(.+)[S|s]([0-9]+)', season)
                        tvs[file]["Seasons"][findSeason[0][1]] = {}
                        for episode in tvSeasonsDirList:
                            try:
                                find = re.findall('(.+)([S|s][0-9]+)([E|e])([0-9]+).*(.mp4$)', episode)
                                if find:
                                    epi = "Episode " + find[0][3]
                                    tvs[file]["Seasons"][findSeason[0][1]][epi] = find[0][0] + find[0][1] + find[0][2] + find[0][3]
                                else:
                                    continue
                            except:
                                continue
                    except:
                        continue
            except:
                print('5')
                continue
            tvsSort = sorted(tvs.items(),key = lambda x:x[1]['last Modified'], reverse=True)
            newTVS = dict()
            for items in tvsSort:
                newTVS[items[0]] = items[1]
        print("\nDone With JSON TVS!! ", len(tvsSort))
    except:
        print("\nError With JSON TVS!!")



    try:
        main = {"Movies":newMovie, "TV":newTVS}
        json_object = json.dumps(main, indent = 4)
        if default == True:
            jfile = 'Z:\dist\json\\' + jname + ".json"
        else:
            ask = str(input("Do you Want to replace the server file: "))
            if ask == 'yes':
                jfile = 'Z:\dist\json\\' + jname + ".json"
            else:
                jfile = jname + ".json"
        with open(jfile, "w") as outfile:
            outfile.write(json_object)
        print("\nJust Created JSON File Named: ", jfile)
    except:
        print("\nError with JSON!!")