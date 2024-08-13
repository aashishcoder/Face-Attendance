import cv2
import os

def capture_images(user_id, user_name):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capture Image")
    img_counter = 0

    user_dir = f"dataset/{user_name}_{user_id}"
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    while True:
        ret, frame = cam.read()
        if not ret:
            break
        cv2.imshow("Capture Image", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:  # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:  # SPACE pressed
            img_name = f"{user_dir}/img_{img_counter}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

user_id = input("Enter User ID: ")
user_name = input("Enter User Name: ")
capture_images(user_id, user_name)