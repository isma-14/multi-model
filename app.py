from flask import Flask, request, jsonify
import os

app = Flask(__name__)


IMAGE_TYPES = {
    '1__': 'PPE',
    '2__': 'License Plate',
    '3__': 'Face Detection'
}

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

    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    return jsonify({'filename': filename, 'image_type': image_type}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
