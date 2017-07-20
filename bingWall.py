import requests
from PIL import Image
from StringIO import StringIO
import ctypes
import os 

def changeBG(path):
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 0)    
	return


def getImage():
	response = requests.get("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-us")
	element = response.json()
	theUrl =  "http://www.bing.com"+element['images'][0]['url']
	image = requests.get(theUrl)
	wallPep = Image.open(StringIO(image.content))
	wallPep.save("img_today.jpg")
	cwd = os.getcwd()
	imagePath = str(cwd)+'\img_today.jpg'
	return imagePath


if __name__ == '__main__':
	imagePath = getImage()
	changeBG(imagePath)


