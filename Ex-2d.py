import cv2

path = input("Enter image path: ")
img = cv2.imread(path)

if img is None:
    print("Error: Image not found")
else:
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    angle = float(input("Enter rotation angle in degrees: "))

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h))

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
