import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Game Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

game_area = frame[0:500,0:100]
gray = cv2.cvtColor(game_area,cv2.COLOR_BGR2GRAY)