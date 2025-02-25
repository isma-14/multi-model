from flask import Flask, request, jsonify, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

IMAGE_TYPES = {
    '1__': 'PPE',
    '2__': 'License Plate',
    '3__': 'Face Detection'
}

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# To store uploaded images metadata
image_history = []

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = file.filename
    prefix = filename[:3]
    image_type = IMAGE_TYPES.get(prefix, 'Unknown')

    # Save image
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Store metadata with timestamp
    image_metadata = {
        'filename': filename,
        'image_type': image_type,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    image_history.append(image_metadata)

    return jsonify({'message': 'Image uploaded successfully', 'image_type': image_type}), 200

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(image_history), 200

@app.route('/uploads/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
