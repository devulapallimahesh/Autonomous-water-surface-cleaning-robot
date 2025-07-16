import cv2

def detect_waste():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        cap.release()
        return False

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = (25, 50, 50)
    upper = (100, 255, 255)
    mask = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cap.release()
    return len(contours) > 0