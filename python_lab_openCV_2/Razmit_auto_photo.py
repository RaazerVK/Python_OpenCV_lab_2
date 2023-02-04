import cv2
import numpy as np

# Чтение изображения
img = cv2.imread('ergo-proksi.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Применение фильтра гаусса с размерностью матрицы свертки 5x5 и средним квадратичным отклонением 1
gaussian = cv2.GaussianBlur(gray, (5, 5), 1)

# Применение фильтра гаусса с размерностью матрицы свертки 15x15 и средним квадратичным отклонением 5
gaussian2 = cv2.GaussianBlur(gray, (15, 15), 5)

# Отображение исходного изображения и двух примененных фильтров
cv2.imshow('Original', gray)
cv2.imshow('Gaussian', gaussian)
cv2.imshow('Gaussian 2', gaussian2)

# Ожидание нажатия клавиши для закрытия окон
cv2.waitKey(0)
cv2.destroyAllWindows()
