from PIL import Image

img = Image.open("photo.jpg")   # image name
img.show()

print("Format:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)
