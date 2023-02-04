import cv2

def apply_gaussian_blur(frame, kernel_size=(5, 5)):
    """Размытие по Гауссу."""
    return cv2.GaussianBlur(frame, kernel_size, 0)


cap = cv2.VideoCapture(0)

# Проверка успешности открытия вебки
if not cap.isOpened():
    print("Не удается получить доступ к вебке")
    exit()

# Считываем изображение с вебки
ret, frame = cap.read()

# Конвертирование в серый
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Использование самой функции
blurred_frame = apply_gaussian_blur(gray_frame)

# Сохранение изображения после применения Гаусса
cv2.imwrite("output.png", blurred_frame)

# Вывод изображения на дисплей
cv2.imshow("Laptop Webcam", blurred_frame)
cv2.waitKey(0)


cap.release()
cv2.destroyAllWindows()
