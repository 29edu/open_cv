
# import cv2 as cv

# img = cv.imread('cat.png')

# resized = cv.resize(img, (900, 700)) # width, height
# cv.imshow("Reduced size", resized)
# cv.waitKey(0)

# # Rotate
# (h, w) = img.shape[:2]
# center = (w//2, h//2)
# M = cv.getRotationMatrix2D(center, 45, 1.0)

# rotated = cv.warpAffine(img, M, (w, h))
# cv.imshow("Rotated  Image", rotated)
# cv.waitKey(0)

# cv.destroyAllWindows()

import cv2 as cv

def nothing(x):
    pass

img = cv.imread("cat.png")

(h, w) = img.shape[:2]
center = (w // 2, h // 2)

cv.namedWindow("Rotate")

# Angle: 0 to 360
cv.createTrackbar("Angle", "Rotate", 0, 360, nothing)

# Scale: 1 to 300
# We'll divide by 100 later
cv.createTrackbar("Scale", "Rotate", 100, 300, nothing)

while True:
    angle = cv.getTrackbarPos("Angle", "Rotate")

    # Convert 100 -> 1.0  It means Original Image
    # Convert 50  -> 0.5 It means zoom to 50%
    # Convert 200 -> 2.0  It means zoom to 200%. Increasse the size of the image
    scale = cv.getTrackbarPos("Scale", "Rotate") / 100.0

    M = cv.getRotationMatrix2D(center, angle, scale)   # Positive Angle means anti-clockwise and negative means clockwise

    rotated = cv.warpAffine(img, M, (w, h))

    cv.imshow("Rotate", rotated)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()