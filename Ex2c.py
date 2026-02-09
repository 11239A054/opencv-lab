import cv2

# Read the input image
img = cv2.imread("input_image.jpg")

# Check if image is loaded properly
if img is None:
    print("Error: Image not found")
else:
    # Convert and save into different formats
    cv2.imwrite("output_image.jpg", img)
    cv2.imwrite("output_image.bmp", img)
    cv2.imwrite("output_image.png", img)
    cv2.imwrite("output_image.tif", img)

    print("Image converted into JPG, BMP, PNG, and TIFF formats successfully.")
