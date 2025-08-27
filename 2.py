import cv2

# Read the image in grayscale
gray_image = cv2.imread('/home/cclab/Pictures/photo-8434386_640.jpg', cv2.IMREAD_GRAYSCALE)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image
cv2.imwrite('gray_image.jpg', gray_image)

from PIL import Image

# Open the image
image = Image.open('/home/cclab/Pictures/photo-8434386_640.jpg')

# Show the image
image.show()

# Save the image
image.save('saved_image.jpg')

