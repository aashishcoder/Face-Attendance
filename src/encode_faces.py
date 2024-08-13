# import face_recognition
# import os
# import pickle

# def encode_faces():
#     known_encodings = []
#     known_names = []

#     dataset_dir = "dataset"
#     for root, dirs, files in os.walk(dataset_dir):
#         for file in files:
#             if file.endswith("jpg"):
#                 path = os.path.join(root, file)
#                 user_name = os.path.basename(root)

#                 image = face_recognition.load_image_file(path)
#                 face_encodings = face_recognition.face_encodings(image)

#                 if face_encodings:
#                     known_encodings.append(face_encodings[0])
#                     known_names.append(user_name)

#     data = {"encodings": known_encodings, "names": known_names}

#     with open("encodings.pickle", "wb") as f:
#         pickle.dump(data, f)

# encode_faces()
import face_recognition
import cv2
import os
import pickle
from imutils import paths

def encode_faces(dataset_path='dataset', encodings_file='encodings/encodings.pickle', model='cnn'):
    # Grab the paths to the input images in our dataset
    image_paths = list(paths.list_images(dataset_path))
    known_encodings = []
    known_names = []

    print(f"[INFO] Quantifying faces from {len(image_paths)} images...")

    # Loop over the image paths
    for (i, image_path) in enumerate(image_paths):
        # Extract the person name from the image path
        name = image_path.split(os.path.sep)[-2]

        # Load the input image and convert it from BGR (OpenCV) to RGB (face_recognition)
        image = cv2.imread(image_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect the (x, y)-coordinates of the bounding boxes corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb_image, model=model)
        print(f"[INFO] Detected {len(boxes)} faces in image {i + 1}/{len(image_paths)}")

        # Compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb_image, boxes)

        # Loop over the encodings
        for encoding in encodings:
            # Add each encoding + name to our set of known names and encodings
            known_encodings.append(encoding)
            known_names.append(name)

    # Dump the facial encodings + names to disk
    print(f"[INFO] Serializing {len(known_encodings)} encodings...")
    data = {"encodings": known_encodings, "names": known_names}

    # Save to the pickle file
    with open(encodings_file, 'wb') as f:
        pickle.dump(data, f)

    print(f"[INFO] Encodings saved to {encodings_file}")

if __name__ == "__main__":
    encode_faces()
