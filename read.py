import cv2 as cv

# ---------- Load and Show Image ----------
img = cv.imread('Photos/cat.jpg')

if img is None:
    print("Error: Image not found or path is incorrect")
else:
    cv.imshow('Cat', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

#video image
def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#live video
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

# ---------- Read and Play Video ----------
capture = cv.VideoCapture('Video/dog.mp4')  # Check path and filename

if not capture.isOpened():
    print("Error: Could not open video file")
else:
    while True:
        isTrue, frame = capture.read()

        if not isTrue:
            break  # End of video

        frame_resized = rescaleframe(frame)
        cv.imshow('Video', frame_resized)

        # Exit on 'd' key
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()
