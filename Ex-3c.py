import cv2
from matplotlib import pyplot as plt

# Full path of your image
image_path = r"C:\Users\Administrator\Desktop\input.jpg"

# Load image
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load image. Check file path.")
else:
    print("Image loaded successfully!")

    # ---- Grayscale Histogram ----
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.plot(gray_hist, color='black')
    plt.xlim([0, 256])
    plt.show()

    # ---- Color Histogram ----
    color = ('b', 'g', 'r')  # OpenCV uses BGR
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    for i, col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()
