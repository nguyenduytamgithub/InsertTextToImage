from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
i = 1
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 70)
with open('card.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)#decode("utf-8-sig").encode("utf-8".splitlines())
    for row in reader:
	for e in row:
		img = Image.open("khung_dichvu.png") 
		draw = ImageDraw.Draw(img)
		draw.text((70, 250),e,(0,0,0),font=font) 
		img.save('image/card' + str(i) + '.jpg') 				
		i = i + 1
		print(e)
csvFile.close()

