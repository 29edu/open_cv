
import cv2 as cv

img = cv.imread('cat.png')

flipped = cv.flip(img, 1)
cv.imshow("Flipped Image", flipped)
cv.waitKey(0)
cv.destroyAllWindows()

# Draw the line
cv.line(img, (0,0), (100, 100), (255, 0, 0), 2)
cv.imshow("Draw the line", img)
cv.waitKey(0)

# Draw the Rectangle

cv.rectangle(img, (10, 10), (500, 200), (0,0, 255), 2)
cv.imshow("Rectangel", img)
cv.waitKey(0)