import cv2

# Full path of your image
image_path = r"C:\Users\Administrator\Desktop\input.jpg"

# Load image
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load image. Check file name or path.")
else:
    print("Image loaded successfully!")

    # 1. Averaging Blur
    blur = cv2.blur(img, (5, 5))

    # 2. Gaussian Blur
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)

    # 3. Median Blur
    median = cv2.medianBlur(img, 5)

    # 4. Bilateral Filter (smooth + keep edges)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    # Show images
    cv2.imshow("Original", img)
    cv2.imshow("Averaging Blur", blur)
    cv2.imshow("Gaussian Blur", gaussian)
    cv2.imshow("Median Blur", median)
    cv2.imshow("Bilateral Filter", bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
