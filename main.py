import os
import argparse
from src import capture_images, encode_faces, recognize_faces

def main():
    parser = argparse.ArgumentParser(description="Face Recognition Attendance System")
    parser.add_argument('--capture', action='store_true', help="Capture images for a new user")
    parser.add_argument('--encode', action='store_true', help="Encode the captured faces")
    parser.add_argument('--recognize', action='store_true', help="Recognize faces and mark attendance")
    args = parser.parse_args()

    if args.capture:
        user_id = input("Enter User ID: ")
        user_name = input("Enter User Name: ")
        capture_images.capture_images(user_id, user_name)
        print("Images captured successfully.")

    if args.encode:
        encode_faces.encode_faces()
        print("Faces encoded successfully.")

    if args.recognize:
        recognize_faces.recognize_faces()
        print("Face recognition and attendance marking completed.")

if __name__ == "__main__":
    main()