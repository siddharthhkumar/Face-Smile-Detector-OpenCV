import cv2

print("Attempting to open camera...")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Trying with DirectShow first

if not cap.isOpened():
    print("ERROR: Could not open camera. Python can't 'see' your webcam.")
    print("Check: Is another app (Zoom, Teams) using it?")
else:
    print("Camera found! Reading frame...")
    ret, frame = cap.read()
    
    if ret:
        print("Success! Camera is working.")
        cv2.imshow("Test", frame)
        cv2.waitKey(0)
    else:
        print("ERROR: Camera opened, but failed to send an image (frame is empty).")

cap.release()
cv2.destroyAllWindows()
