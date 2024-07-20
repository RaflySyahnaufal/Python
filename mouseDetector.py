import cv2
import mediapipe as mp
import numpy as np
import pyautogui

# Inisialisasi Mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Mengambil video dari webcam
cap = cv2.VideoCapture(0)

# Mendapatkan ukuran layar
screen_width, screen_height = pyautogui.size()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Konversi gambar ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Proses gambar dan deteksi tangan
    results = hands.process(image_rgb)

    # Gambar landmark tangan jika ada tangan yang terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Dapatkan posisi landmark tangan
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))
            
            # Kontrol kursor mouse menggunakan landmark index finger
            if lm_list:
                index_finger_tip = lm_list[8]
                x, y = index_finger_tip[1], index_finger_tip[2]
                
                # Konversi koordinat dari gambar ke layar
                screen_x = np.interp(x, (0, w), (0, screen_width))
                screen_y = np.interp(y, (0, h), (0, screen_height))
                
                # Pindahkan kursor
                pyautogui.moveTo(screen_x, screen_y)

    # Tampilkan gambar
    cv2.imshow('Virtual Mouse', image)

    # Keluar dengan menekan 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
