
import cv2 as cv
import numpy as np

original_img = cv.imread('parrot.png')
img = cv.resize(original_img, (700, 500)) 

# Converting in hsv
image_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Range of colour for considering the red

# lower_red = np.array([0,120,70])
# higher_red = np.array([10, 255, 255])


# Range for green colour. This will detect the green colour
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# mask = cv.inRange(image_hsv, lower_red, higher_red)
mask = cv.inRange(image_hsv, lower_green, upper_green)

result = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Original Image", img)
cv.imshow("Image", result)
cv.waitKey(0)

# Splitting the colours into B, G, R

B, G, R = cv.split(img)
cv.imshow("Original colour", img)
cv.imshow("B", B)
cv.imshow("G", G)
cv.imshow("R", R)

cv.waitKey(0)

cv.destroyAllWindows()
