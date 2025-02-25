from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

IMAGE_TYPES = {
    '1__': 'PPE',
    '2__': 'License Plate',
    '3__': 'Face Detection'
}

UPLOAD_FOLDER = 'uploads'
HISTORY_FILE = 'history.json'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load or initialize history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'r') as f:
        image_history = json.load(f)
else:
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

    # Save the image
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Add to history
    entry = {
        'filename': filename,
        'image_type': image_type,
        'timestamp': datetime.utcnow().isoformat()
    }
    image_history.append(entry)

    # Save history
    with open(HISTORY_FILE, 'w') as f:
        json.dump(image_history, f)

    return jsonify({'filename': filename, 'image_type': image_type}), 200

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(image_history), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
