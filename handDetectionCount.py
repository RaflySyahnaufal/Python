import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Konversi gambar ke RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Proses gambar untuk mendeteksi tangan
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        count = len(results.multi_hand_landmarks)
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        # Tampilkan jumlah tangan yang terdeteksi
        cv2.putText(img, f'Hands Detected: {count}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        # Jika tidak ada tangan terdeteksi, set count menjadi 0
        count = 0
        cv2.putText(img, 'Hands Detected: 0', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Tampilkan gambar
    cv2.imshow("Hand Detector", img)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan setelah selesai
cap.release()
cv2.destroyAllWindows()
hands.close()
