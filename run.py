def generate_img(output="", theme={}, text="asd", resolution=(1920,1080)):

    img = Image.open("/home/InsertTextToImage/khung_dichvu.png")
    #img = Image.new("RGB", resolution, theme["background"])
    W, H = img.size

    logo = Image.open("/home/InsertTextToImage/khung_dichvu.png")
    colorized_img = ImageOps.colorize(logo.convert("L"), theme["text"], theme["background"])
    size = int((W/100)*17)
    logo_newsize = colorized_img.resize((size, size), Image.ANTIALIAS)
    img.paste(logo_newsize, (int((W-size)/2), int((H-size)/2)))

    draw = ImageDraw.Draw(img)

    base_font_pixle = int((56/1920)*resolution[0])

    font = ImageFont.truetype("DejaVuSansMono.ttf", base_font_pixle)
    w, h = font.getsize(text)

    text_draw(draw, text, base_font_pixle, img.size, theme)

    img.save(output, quality=100)
