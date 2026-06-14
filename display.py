
import cv2 as cv
import sys # command that give information about system level commands

# Load an image
img = cv.imread('cat.png')

if img is not None:
    cv.imshow("Display Window", img)
    cv.waitKey(0) # it means the image window will disappear only when a key is pressed
    
    # Printing the height and width
    h , w = img.shape[:2]
    print(f'Height is {h} And Width is {w}')
    
    # Gray scale ->  Will show image in Gray Colour (1 channel)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray Picture", gray)
    cv.waitKey(0)
    
    # To find the edge of object in image, we will follow the steps
    # Apply guassian blur
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    
    # Show the uncanny images
    edges = cv.Canny(blurred, 50, 150)
    
    cv.imshow("Normal Picture", img)
    cv.imshow("Blurrred Image", gray)
    cv.imshow("Uncaany Images", edges)
    
    cv.waitKey(0)
    
    cv.destroyAllWindows()
    
else:
    print("Not able to load the image")
    



