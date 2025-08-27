import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/cclab/Pictures/photo-8434386_640.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert for correct color display in matplotlib

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image = cv2.imread('/home/cclab/Pictures/photo-8434386_640.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(gray, 100, 200)

blur = cv2.GaussianBlur(img_rgb, (15, 15), 0)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(edges, cmap='gray')
plt.title('Edges (Canny)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(blur)
plt.title('Blurred')
plt.axis('off')

plt.tight_layout()
plt.show()

