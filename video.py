
import cv2 as cv

cap = cv.VideoCapture(0) 
# 0 -> default Webcam
# 1 -> Second camera (if connected)
# 2 -> third camera

# If i want to read a video file then i can replace the 0 with the path of the video

while True:
    
    # Reading a frame, ret -> true if frame is successfully read and false means failed one
    # frame measn the actual image captured from the camera
    ret, frame = cap.read()
    
    # frame.shape may return (480, 600, 3) -> It means 480 pixels high, 600 pixels wide and 3 channels
    
    if not ret:
        break
    
    # Covert to grayScale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Display
    # cv.imshow("Webcam", frame) This will start video without grayscale
    
    # Break on q
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    