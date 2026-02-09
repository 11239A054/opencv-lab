import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
    exit()

x = 100
y = 50
w = 200
h = 150

cropped_img = img[y:y+h, x:x+w]

cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
