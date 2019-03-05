from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
img = Image.open("khung_dichvu.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 70)
with open('card.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
	for e in row:
		draw.text((70, 250),e,(0,0,0),font=font)
		print(e)
img.save('card4.jpg')
csvFile.close()

