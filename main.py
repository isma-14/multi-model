import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image Viewer - Multi Model Application")

flask_url = 'http://15.207.113.67:5000'  # Update with your EC2 public IP if different

# Fetch and display image history
def fetch_image_history():
    response = requests.get(f"{flask_url}/history")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch image history.")
        return []

# Display uploaded images history
st.header("Uploaded Images History")
image_history = fetch_image_history()

if image_history:
    for item in reversed(image_history):  # Show latest first
        st.subheader(f"Image: {item['filename']}")
        st.write(f"Type: {item['image_type']}")
        st.write(f"Uploaded At: {item['timestamp']}")

        # Fetch and display the image
        image_response = requests.get(f"{flask_url}/uploads/{item['filename']}")
        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption=item['filename'], use_column_width=True)
        else:
            st.warning("Unable to load image.")
else:
    st.write("No images uploaded yet.")
