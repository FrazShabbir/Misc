from PIL import Image

img1 = Image.open(r"Source_Image_path")

# The values used to crop the original image (will form a bbox)
x1, y1, x2, y2 = 10, 10, 400, 400

# The angle at which the cropped Image must be rotated
angle = 50

# cropping the original image 
img = img1.crop((x1, y1, x2, y2))

# Firstly converting the Image mode to RGBA, and then rotating it
img = img.convert("RGBA").rotate(angle, resample=Image.BICUBIC)

# calibrating the bbox for the beginning and end position of the cropped image in the original image 
# i.e the cropped image should lie in the center of the original image
x1 = int(.5 * img1.size[0]) - int(.5 * img.size[0])
y1 = int(.5 * img1.size[1]) - int(.5 * img.size[1])
x2 = int(.5 * img1.size[0]) + int(.5 * img.size[0])
y2 = int(.5 * img1.size[1]) + int(.5 * img.size[1])

# pasting the cropped image over the original image, guided by the transparency mask of cropped image
img1.paste(img, box=(x1, y1, x2, y2), mask=img)

# converting the final image into its original color mode, and then saving it
# converting the final image into its original color mode, and then saving it
img1.convert(img1.mode).save("Destination_path")

