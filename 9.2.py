from PIL import Image

image = Image.open('i.webp')

image_3 = (image.width // 3, image.height // 3)
cat_image = image.resize(image_3)
cat_image.save("cat_image.jpeg")
cat_image.show()

cat_h = image.transpose(Image.FLIP_LEFT_RIGHT)
cat_h.save("cat_h.jpeg")
cat_h.show()

cat_v = image.transpose(Image.FLIP_TOP_BOTTOM)
cat_v.save("cat_v.jpeg")
cat_v.show()