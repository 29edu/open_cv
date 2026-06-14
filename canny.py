import cv2 as cv

def nothing(x):
    pass

img = cv.imread("cat.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)

cv.namedWindow("Canny")

cv.createTrackbar("Low", "Canny", 50, 255, nothing)
cv.createTrackbar("High", "Canny", 150, 255, nothing)

while True:
    low = cv.getTrackbarPos("Low", "Canny")
    high = cv.getTrackbarPos("High", "Canny")

    edges = cv.Canny(blurred, low, high)

    cv.imshow("Canny", edges)

    if cv.waitKey(1) & 0xFF == 27:  # ESC key
        break

cv.destroyAllWindows()