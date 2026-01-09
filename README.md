# Image Captioning Web App

This project is a Flask-based web application for generating captions for uploaded images. The app uses a pre-trained LSTM model to predict descriptive captions for images uploaded by the user.

---

## Features
- **User-Friendly Interface**: Upload an image and view the generated caption.
- **Caption Generation**: Uses a pre-trained LSTM model for generating image captions.
- **Dynamic Rendering**: Displays the uploaded image alongside its generated caption on the same page.

---

## Requirements
- Python 3.7 or higher

### Libraries
Install the following Python libraries:
```bash
pip install flask
```

Additionally, ensure the `Caption_it` module is implemented for loading the pre-trained LSTM model and predicting captions.

---

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/SamarthKuchya/Image-Caption.git
cd image-captioning-app
```

### 2. Place the Pre-trained Model
Ensure the pre-trained LSTM model is placed in the appropriate directory as required by the `Caption_it` module.

### 3. Run the Application
Run the Flask application using:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

---

## Folder Structure
```
project-directory/
│
├── app.py                  # Main Flask application
├── Caption_it.py           # Module for caption prediction
├── static/                 # Directory for storing uploaded images
├── templates/
│   └── index.html          # Frontend HTML file
```

---

## How It Works
1. **Homepage**:
   - Displays an upload form for the user to upload an image.

2. **Image Upload**:
   - The uploaded image is saved to the `static/` directory.

3. **Caption Prediction**:
   - The `Caption_it` module processes the uploaded image and generates a caption using the LSTM model.

4. **Display Results**:
   - The uploaded image and its predicted caption are displayed on the same page.

---

## Customization
- **Model**: Replace the pre-trained model in the `Caption_it` module if needed.
- **Styling**: Modify the `index.html` file for UI enhancements.

---

## Limitations
- **Model Accuracy**: The quality of captions depends on the training data and model architecture.
- **File Formats**: Ensure the uploaded images are in supported formats (e.g., `.jpg`, `.png`).

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
Special thanks to the creators of Flask and the LSTM model for enabling this project.
