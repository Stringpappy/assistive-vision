
import cv2


def main():

    # Step 1: Connect to the default webcam
    cap = cv2.VideoCapture(0)

    # Step 2: Check whether the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    try:
        # Step 3: Continuously capture video frames
        while True:

            # Capture one frame
            success, frame = cap.read()

            # Step 4: Check whether the frame was captured
            if not success:
                print("Error: Could not read frame.")
                break

            # Step 5: Display the captured frame
            cv2.imshow("Assistive Vision System", frame)

            # Step 6: Exit when the user presses Q
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        # Step 7: Release the webcam
        cap.release()

        # Close all OpenCV windows
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
