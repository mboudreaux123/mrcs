import cv2 as cv
import head

COLOR_GREEN = (0, 255, 0)

face_cascade_name = "haarcascade_frontalface.xml"
face_cascade = cv.CascadeClassifier()
camera_device = int(0)

X_LOWER_LIMIT = 100 # Default 100
X_UPPER_LIMIT = 560 # Default 560
Y_LOWER_LIMIT = 100 # Default 100
Y_UPPER_LIMIT = 560 # Default 560
X_MID = X_UPPER_LIMIT - X_LOWER_LIMIT
Y_MID = Y_UPPER_LIMIT - Y_LOWER_LIMIT

head = head.Head()
current_x = X_MID
current_y = Y_MID

def detectFace(frame):
	frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	frame_gray = cv.equalizeHist(frame_gray)

	#-- Detect faces
	faces = face_cascade.detectMultiScale(frame_gray)
	for (x,y,w,h) in faces:
		# Get center of face
		center = (x + w//2, y + h//2)

		# Get center of frame
		h, w = frame.shape[:2]
		h, w = h/2, w/2

		# Move camera
		if center[0] > w:
			current_x = current_x -1
		if center[0] < w:
			current_x = current_x +1

		if center[1] > h:
			current_y = current_y -1
		if center[1] < h:
			current_y = current_y +1

		# Set the turn to calculations
		head.turnX(current_x)
		head.turnY(current_y)

		# Draw box around face
		cv.rectangle(frame, (x, y), (x + w, y + h), COLOR_GREEN, 2)

	return frame, faces

def main():

	#-- 1. Load the cascades
	if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
		print('--(!)Error loading face cascade')
		exit(0)

	#-- 2. Read the video stream
	cap = cv.VideoCapture(camera_device)
	if not cap.isOpened:
		print('--(!)Error opening video capture')
		exit(0)

	while True:
		ret, frame = cap.read()
		if frame is None:
			print('--(!) No captured frame -- Break!')
			break

		detectFace(frame)


		if cv.waitKey(10) == 27:
			break


if __name__ == '__main__':
	main()