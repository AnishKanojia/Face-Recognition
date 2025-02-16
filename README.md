# Face Detection Using OpenCV

## Overview
This project demonstrates real-time face detection using OpenCV's Haar cascade classifier. The script captures video from the webcam, detects faces in real-time, and draws rectangles around them.

## Features
- Uses Haar cascade for face detection.
- Works in real-time using a webcam.
- Displays detected faces with a green rectangle.
- Normalizes lighting for improved accuracy.
- Adjustable webcam resolution.

## Prerequisites
Ensure you have Python and OpenCV installed.

### Install Dependencies
```bash
pip install opencv-python
```

## How to Run
1. Download the **Haar cascade classifier** from OpenCV:
   - [Download here](https://github.com/opencv/opencv/tree/master/data/haarcascades)
   - Place `haarcascade_frontalface_default.xml` in the same directory as the script.

2. Run the script:
```bash
python face_detection.py
```

3. Press **'ESC'** to exit the webcam window.

## Code Explanation
- Loads the Haar cascade classifier.
- Initializes the webcam and sets resolution.
- Reads frames from the webcam, converts them to grayscale, and applies histogram equalization.
- Detects faces and draws green rectangles around them.
- Displays the processed video feed.

## Troubleshooting
- **Webcam Not Opening?** Ensure it’s not being used by another application.
- **No Faces Detected?** Adjust `scaleFactor` and `minNeighbors` values.
- **Low FPS?** Try reducing the resolution.

## License
This project is open-source and free to use under the MIT License.
