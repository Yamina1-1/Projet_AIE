import cv2

url = "http://10.182.131.62:4747/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Impossible de lire le flux")
        break

    # Convertir en RGB pour test
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow("Flux DroidCam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()