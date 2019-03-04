from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("khung_dichvu.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 90)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((60, 90),"Sample Text",(0,50,50),font=font)
img.save('sampleout.jpg')
