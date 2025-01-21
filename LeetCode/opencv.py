import cv2
import mediapipe as mp

# Initialize Mediapipe Hands and Drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Function to count raised fingers
def count_fingers(hand_landmarks):
    """
    Counts raised fingers based on landmarks.
    """
    finger_tips = [8, 12, 16, 20]  # Index for fingertips
    finger_base = [6, 10, 14, 18]  # Corresponding finger bases

    count = 0
    for tip, base in zip(finger_tips, finger_base):
        if hand_landmarks[tip].y < hand_landmarks[base].y:  # If fingertip is above the base
            count += 1

    # Check thumb separately
    if hand_landmarks[4].x < hand_landmarks[3].x:  # Check if thumb is extended
        count += 1

    return count

# Initialize webcam and Mediapipe Hands
cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    print("Program Started. Show 1 finger for 'Hello', 2 for 'How are you', and 3 to close.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Flip and process the frame
        frame = cv2.flip(frame, 1)  # Flip horizontally for a mirror view
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # Draw hand landmarks and detect finger count
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Count raised fingers
                finger_count = count_fingers(hand_landmarks.landmark)

                # Display messages based on finger count
                if finger_count == 1:
                    cv2.putText(frame, "Hello!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif finger_count == 2:
                    cv2.putText(frame, "How are you?", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                elif finger_count == 3:
                    cv2.putText(frame, "Closing...", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

        # Display the processed frame
        cv2.imshow('Hand Detection', frame)

        # Quit program with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
