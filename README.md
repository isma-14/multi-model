# Multi-Model Training Application

This project consists of a **Streamlit** frontend for UI and a **Flask** backend for image classification.

## Features
- Upload images through Streamlit.
- Flask backend classifies images based on filename prefix:
  - `1__` → PPE
  - `2__` → License Plate
  - `3__` → Face Detection
- Displays uploaded image and its category.

## Setup Instructions

### Backend (Flask)
```bash
cd backend_flask
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend (Streamlit)
```bash
cd frontend_streamlit
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Usage
1. Run the Flask backend.
2. Run the Streamlit frontend.
3. Upload an image via Streamlit and view the result.

## Deployment
- Deploy Flask on an EC2 instance.
- Streamlit can run locally or be deployed to a web server.

## License
MIT License
