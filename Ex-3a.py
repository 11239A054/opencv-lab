import cv2
import os

# Check if file exists
path = r"C:\Users\Administrator\Desktop\input.jpg"
print("File Exists:", os.path.exists(path))

# Load image
image = cv2.imread(path)

if image is None:
    print("Error: Could not load image. Check file name or path.")
else:
    print("Image loaded successfully!")

    # Flip image
    flipped = cv2.flip(image, 1)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Flipped Image", flipped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
