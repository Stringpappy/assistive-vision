import cv2


def main():

    # Connect to the default webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not access webcam.")
        return

    try:
        while True:

            success, frame = cap.read()

            if not success:
                break

            height, width, channels = frame.shape
            print(height, width, channels)

            # Display the webcam feed
            cv2.imshow("Frame Analysis", frame)

            # Exit when Q is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
