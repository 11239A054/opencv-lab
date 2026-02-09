import cv2
import numpy as np

# Create a blank image (black background)
img = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw a line
cv2.line(img, (50, 50), (250, 50), (0, 255, 0), 2)

# Draw a rectangle
cv2.rectangle(img, (50, 100), (250, 200), (255, 0, 0), 2)

# Draw a circle
cv2.circle(img, (150, 300), 50, (0, 0, 255), 2)

# Draw a filled triangle
pts = np.array([[350, 100], [300, 200], [400, 200]], np.int32)
cv2.fillPoly(img, [pts], (0, 255, 255))

# Show the image
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
