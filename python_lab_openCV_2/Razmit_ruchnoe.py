import cv2
import numpy as np

def gaussian_filter(img, kernel_size, sigma):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

img = cv2.imread("ergo-proksi.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gaussian_5_3 = gaussian_filter(gray, 5, 3)
gaussian_7_5 = gaussian_filter(gray, 7, 5)



cv2.imshow("Original", gray)
cv2.imshow("Gaussian 5x5, sigma=3", gaussian_5_3)
cv2.imshow("Gaussian 7x7, sigma=5", gaussian_7_5)

cv2.waitKey(0)
cv2.destroyAllWindows()
