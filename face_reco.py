import cv2

# Load the Haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start the webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set webcam resolution
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Capture frame
    ret, img = webcam.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Optional: Normalize lighting
    gray = cv2.equalizeHist(gray)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Show the frame
    cv2.imshow("Face Detection", img)

    # Exit on pressing 'ESC'
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release webcam and close windows
webcam.release()
cv2.destroyAllWindows()
