from PIL import Image

# Open the image
image = Image.open('/home/cclab/Pictures/photo-8434386_640.jpg')

# Show the image
image.show()

# Save the image
image.save('saved_image.jpg')

