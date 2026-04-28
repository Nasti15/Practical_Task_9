from PIL import Image, ImageDraw

img = Image.open("2.jpg")
draw = ImageDraw.Draw(img)
draw.text((img.width-120, img.height-30), "Zenit", fill="white")
img.save("Zenit.jpg")

img1 = Image.open("Zenit.jpg")
img1.show()

print("Вдяной знак справа снизу")