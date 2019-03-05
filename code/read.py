from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
i = 1
font = ImageFont.truetype("../font/DejaVuSansMono.ttf", 70)
with open('../input/card.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)#decode("utf-8-sig").encode("utf-8".splitlines())
    for row in reader:
	for e in row:
		img = Image.open("../image_input/image.png") 
		draw = ImageDraw.Draw(img)
		draw.text((70, 250),e,(0,0,0),font=font) 
		img.save('../output/card' + str(i) + '.jpg') 				
		i = i + 1
		print(e)
csvFile.close()

