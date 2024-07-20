import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Buka kamera
cap = cv2.VideoCapture(0)

# Fungsi untuk menghitung jumlah jari yang terangkat
def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Landmark untuk ujung jari: telunjuk, tengah, manis, kelingking
    thumb_tip = 4  # Landmark untuk ujung ibu jari
    
    fingers = []
    for tip in finger_tips:
        # Jari terangkat jika y dari landmark ujung lebih rendah (lebih kecil) dari y landmark dari jari terdekat
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    
    # Ibu jari terangkat jika x dari landmark ujung lebih besar dari x landmark dari jari terdekat
    if hand_landmarks.landmark[thumb_tip].x > hand_landmarks.landmark[thumb_tip - 2].x:
        fingers.append(1)
    else:
        fingers.append(0)
    
    return sum(fingers)

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Konversi gambar ke RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Proses gambar untuk mendeteksi tangan
    results = hands.process(img_rgb)
    
    total_fingers = 0
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar landmark tangan
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Hitung jumlah jari yang terangkat dari masing-masing tangan
            fingers_count = count_fingers(hand_landmarks)
            total_fingers += fingers_count
    
    # Tampilkan jumlah total jari yang terangkat
    cv2.putText(img, f'Total Fingers: {total_fingers}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Tampilkan gambar
    cv2.imshow("Finger Detector", img)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan setelah selesai
cap.release()
cv2.destroyAllWindows()
hands.close()
