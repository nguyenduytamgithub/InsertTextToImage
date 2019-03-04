from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("khung_dichvu.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 70)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((60, 160),"216733368746104",(0,0,0),font=font)
img.save('card.jpg')
