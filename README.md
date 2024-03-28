# Image Object Detection Web App

This is a simple web application built with Flask that allows users to upload images and detect objects like faces and cars using OpenCV's Haar cascade classifiers.

## Features

- Upload images from your local machine.
- Detect faces and cars in the uploaded images.
- Annotate the uploaded images with rectangles around the detected objects.
- View the original and annotated images.

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/your-username/image-object-detection-web-app.git
    ```

2. Navigate to the project directory:

    ```
    cd image-object-detection-web-app
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```
    python app.py
    ```

5. Open your web browser and go to http://localhost:5000 to access the web application.

## Usage

1. On the home page, click on the "Choose File" button to select an image file from your local machine.
2. Click the "Upload" button to upload the selected image.
3. After uploading, the application will detect faces and cars in the image and annotate them with rectangles.
4. You will be redirected to the results page where you can view both the original and annotated images.

## Directory Structure

├── app.py # Flask application script
├── static # Static assets
│ ├── uploads # Uploaded images and annotated images
│ └── haarcascades # Haar cascade XML files for object detection
├── templates # HTML templates
│ ├── upload.html # Upload form template
│ └── result.html # Results template
├── README.md # Project documentation
└── requirements.txt # Python dependencies


## Dependencies

- Flask
- OpenCV

