from flask import Flask, render_template, request, redirect, url_for, flash
import os
import cv2

app = Flask(__name__)

# Define the folder to store uploaded images
UPLOAD_FOLDER = "static/uploads"

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths to the Haar cascade XML files
face_cascade_path = os.path.join(current_dir, 'static', 'haarcascades', 'haarcascade_frontalface_default.xml')
car_cascade_path = os.path.join(current_dir, 'static', 'haarcascades', 'haarcascade_car.xml')

# Load the Haar cascade classifiers for face and car detection
face_cascade = cv2.CascadeClassifier(face_cascade_path)
car_cascade = cv2.CascadeClassifier(car_cascade_path)

def detect_objects(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)

    return faces, cars


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file:
            # Save the uploaded file
            filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filename)

            # Read the saved image
            image = cv2.imread(filename)

            # Detect faces and cars
            faces, cars = detect_objects(image)

            # Draw rectangles around detected faces
            for x, y, w, h in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Draw rectangles around detected cars
            for x, y, w, h in cars:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Save the annotated image
            annotated_filename = os.path.join(
                app.config["UPLOAD_FOLDER"], "annotated_" + file.filename
            )
            cv2.imwrite(annotated_filename, image)

            # Display the uploaded image and the annotated image
            return render_template(
                "result.html",
                original_image=file.filename,
                annotated_image="annotated_" + file.filename,
            )

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
