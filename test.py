from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("khung_dichvu.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text",(0,0,0),font=font)
img.save('sample-out.jpg')
