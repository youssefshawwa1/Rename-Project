import requests
def imgCreater(path, url, name):
    with open(f'{path}\\{name}.jpg', 'wb') as handler:
            poster_data=requests.get(url).content
            handler.write(poster_data)
            print(f"Just Saved Image {name}.jpg in {path}")