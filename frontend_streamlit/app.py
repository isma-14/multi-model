import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image Viewer - Multi Model Application")

# Upload image via Streamlit
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Send image to Flask backend
    flask_url = 'http://15.207.113.67:5000/upload'  # Change this to EC2 public IP when deploying
    files = {'file': (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post(flask_url, files=files)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Image Type: {result['image_type']}")
    else:
        st.error(f"Error: {response.text}")
