import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hand dan Drawing
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Inisialisasi video capture
cap = cv2.VideoCapture(0)

# Fungsi untuk mengenali huruf berdasarkan posisi landmark tangan
def recognize_letter(landmarks, h, w):
    thumb_tip = (int(landmarks[mp_hands.HandLandmark.THUMB_TIP].x * w), int(landmarks[mp_hands.HandLandmark.THUMB_TIP].y * h))
    index_tip = (int(landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w), int(landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h))
    middle_tip = (int(landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * w), int(landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * h))
    ring_tip = (int(landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].x * w), int(landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y * h))
    pinky_tip = (int(landmarks[mp_hands.HandLandmark.PINKY_TIP].x * w), int(landmarks[mp_hands.HandLandmark.PINKY_TIP].y * h))

    # Logika untuk mengenali huruf tertentu (contoh sederhana)
    if thumb_tip[1] < index_tip[1] and index_tip[1] < middle_tip[1]:
        return "L"
    elif thumb_tip[0] < index_tip[0] and index_tip[0] < middle_tip[0] and middle_tip[0] < ring_tip[0] and ring_tip[0] < pinky_tip[0]:
        return "O"
    elif thumb_tip[1] < index_tip[1] and index_tip[1] < middle_tip[1]:
        return "V"
    elif thumb_tip[1] > index_tip[1] and index_tip[1] > middle_tip[1] and middle_tip[1] > ring_tip[1] and ring_tip[1] > pinky_tip[1]:
        return "E"
    return ""

# Inisialisasi MediaPipe Hands
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Balik gambar frame secara horizontal untuk menghilangkan efek mirror
        frame = cv2.flip(frame, 1)

        # Konversi frame ke RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Proses deteksi tangan
        results = hands.process(image)

        # Konversi kembali ke BGR untuk OpenCV
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Gambar landmark tangan
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Ambil koordinat landmark yang diperlukan
                h, w, _ = image.shape
                letter = recognize_letter(hand_landmarks.landmark, h, w)
                if letter:
                    cv2.putText(image, letter, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)

        # Tampilkan gambar
        cv2.imshow('Hand Detection', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
