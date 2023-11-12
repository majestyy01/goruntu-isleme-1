import webbrowser
import time
import cv2
import numpy as np
import tkinter as tk
import threading
import mediapipe as mp
import pyautogui


#9142
#WoxicDEV
#İnstagram : @woxicdev

screen_width, screen_height = pyautogui.size()


screen_x, screen_y = pyautogui.position()



instagram_url = "https://www.instagram.com/techmate9142/"

webbrowser.open_new(instagram_url)


root = tk.Tk()
root.title("Yönlendirme 9142")


window_width = 600  
window_height = 400  
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


direction_label = tk.Label(root, text="BY Team9142", font=("Helvetica", 36, "bold"), fg="blue")
direction_label.pack(pady=20)


countdown_label = tk.Label(root, text="", font=("Helvetica", 24))
countdown_label.pack()


for i in range(5, 0, -1):
    countdown_label.config(text=f"Yönlendiriliyorsunuz... {i} saniye")
    root.update()
    time.sleep(1)

#
additional_text = tk.Label(root, text="Takip Ettiğiniz için Teşekkürler!", font=("Helvetica", 24, "bold"), fg="blue")
additional_text.pack(pady=20)
additional_text = tk.Label(root, text="Kamera sekmesinden çıkış için q tuşuna basılı tutun", font=("Helvetica", 14, "bold"), fg="blue")
additional_text.pack(pady=10)  


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

def motionDetection():
    
    cap = cv2.VideoCapture(0)

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Boş kamera çerçevesi görmezden geliyoruz.")
                
                break

            
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = holistic.process(image_rgb)

            if results.face_landmarks:
                
                mp_drawing.draw_landmarks(
                    image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 190, 255)),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 0)))

            if results.left_hand_landmarks:
                
                mp_drawing.draw_landmarks(
                    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 190, 255)),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 0)))
                
                
                x, y = int(results.left_hand_landmarks.landmark[9].x * image.shape[1]), int(results.left_hand_landmarks.landmark[9].y * image.shape[0])
                x1, y1 = int(results.left_hand_landmarks.landmark[12].x * image.shape[1]), int(results.left_hand_landmarks.landmark[12].y * image.shape[0])
                font = cv2.FONT_HERSHEY_PLAIN
                if y1 > y:
                    cv2.putText(image, "KAPALI", (10, 30), font, 2, (0, 0, 0), 2)
                else:
                    cv2.putText(image, "ACIK", (10, 30), font, 2, (0, 0, 0), 2)

            if results.right_hand_landmarks:
                
                mp_drawing.draw_landmarks(
                    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 190, 255)),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 0)))

            
            if results.face_landmarks:
                landmarks = results.face_landmarks.landmark
                for landmark in [landmarks[10], landmarks[152], landmarks[234], landmarks[454]]:
                    x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
                    cv2.circle(image, (x, y), 2, (0, 0, 0), -1)

            cv2.imshow('9142 Algilayici | Instagram techmate9142', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


def exitApplication():
    root.destroy()


start_button = tk.Button(root, text="Başlat", command=motionDetection, font=("Helvetica", 18))
start_button.pack()


exit_button = tk.Button(root, text="Çıkış", command=exitApplication, font=("Helvetica", 18))
exit_button.pack()

root.mainloop()

