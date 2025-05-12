from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Mock prediction function
def mock_predict(image_path):
    import random
    return "This is a healthy plant." if random.choice([True, False]) else "This is an infected plant."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file.'}), 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Call the mock prediction function
    prediction = mock_predict(file_path)

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
