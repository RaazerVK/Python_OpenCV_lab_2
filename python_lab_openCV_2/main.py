import cv2
import numpy as np

def apply_gaussian_filter(frame):
    # Фильтр Гаусса
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

    return cv2.filter2D(frame, -1, kernel)

# Запуск
cap = cv2.VideoCapture(0)

# Выбираем кодек и создаем видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# Дисплей вебкамеры
while True:
    ret, frame = cap.read()
    if ret:
        # конвертируем в серый
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # применияем фильтр
        filtered = apply_gaussian_filter(gray)

        out.write(filtered)

        # вывод в окно
        cv2.imshow('Webcam', filtered)

        # По нажатию на q закрываем
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
