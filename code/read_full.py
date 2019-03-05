from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from array import *
import csv
x_pos = 50
y_pos = 170
x_move = 506
y_move = 415
T = []
x = 0 # insert e to array with x
pos = 0 #draw number string with pos to T
img = Image.open("../image_input/image_full.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("../font/DejaVuSansMono.ttf", 45)
with open('../input/card.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)#decode("utf-8-sig").encode("utf-8".splitlines())
	for row in reader:
		for e in row:
			T.insert(x,e)
			x = x+1
			print(e)
	#for j in T:
		#print(j)
	for l in range(8):
		for k in range(5):
			draw.text((x_pos+k*x_move, y_pos+l*y_move),T[pos],(0,0,0),font=font) 				
			pos = pos + 1
img.save('../output/card.jpg')# + str(i) + '.jpg') 				
csvFile.close()

