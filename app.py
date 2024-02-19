from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static\gesture_images'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/upload_sign', methods=['GET', 'POST'])
def upload_sign():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'})
    
    return render_template('upload.html')  # Display the form for uploading signatures



@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    image = request.files['image']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Perform sign language prediction here
    prediction = predict_sign_language(image_path)

    return render_template('result.html', prediction=prediction)


def predict_sign_language(image_path):
    # Implement your sign language prediction logic here
    # You can use any machine learning or deep learning model for this task
    # For simplicity, let's assume the prediction is based on the filename of the uploaded image
    filename = os.path.basename(image_path)
    sign = filename.split('.')[0]

    return sign



if __name__ == '__main__':
    app.run(debug=True)