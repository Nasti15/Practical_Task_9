from PIL import Image

image = Image.open('i.webp')
image.show()

print("Размер изображения равен: ", image.size)
print("Формат изображения: ", image.format)
print("Цветовая модель изображения: ", image.mode)
