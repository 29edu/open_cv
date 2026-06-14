
# Terms

## Canny Image

    Canny Edge Detection is an image processing algorithm used to find the edges (boundaries) of objects in an image.

    Why do we need it?

    Computers don't naturally understand objects like humans do. Finding edges helps with:
    
    1. Object detection
    2. Face recognition
    3. Self-driving cars
    4. Medical image analysis
    5. Computer vision task

    Steps in Canny Edge Detection
    1. Noise Reduction:- 
        Images don't contain random noises. Before finding edges, the image is blurred using Gaussian Filter so noise doesn't mistaken for edges.

    2. Calculate Intensity Gradient
        The algorithm checks how quickly pixel brightness changes.

        Small change → probably not an edge
        Large change → possible edge

    3. 