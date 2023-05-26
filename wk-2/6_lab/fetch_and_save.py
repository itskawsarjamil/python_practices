import requests
import json
import PyWallpaper

response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
string_content=response.content.decode("utf-8")

json_content=json.loads(string_content)
img_url=json_content['hdurl']
img_res=requests.get(img_url)

with open("img.png",'wb') as image:
    image.write(img_res.content)


PyWallpaper.change_wallpaper("D:\code\Phitron\course 4 python\6_lab\img.png")

# print()


# import requests
# import json




# print( )

# with open("img2.png",'wb') as image:
#     image.write(requests.get(json.loads(requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY").content.decode("utf-8"))["hdurl"]).content)
    
    