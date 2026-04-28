from PIL import Image, ImageEnhance

for i in range(1, 6):
    img = Image.open(f"{i}.jpg")
    enhancer = ImageEnhance.Contrast(img)
    result = enhancer.enhance(1.5)
    result.save(f"new_{i}.jpg")

