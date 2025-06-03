import streamlit as st
import requests

st.title("Find Your Twin!")

st.write("Upload a photo or take one with your webcam to find your top 3 lookalikes.")

# Upload or capture image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
camera_image = st.camera_input("Or take a photo")

image_bytes = None
if uploaded_file is not None:
    image_bytes = uploaded_file.read()
elif camera_image is not None:
    image_bytes = camera_image.getvalue()

if image_bytes:
    with st.spinner("Searching for your twins..."):
        files = {"file": ("image.jpg", image_bytes, "image/jpeg")}
        try:
            response = requests.post(
                "http://localhost:8000/find_twin?top_k=3",  # Adjust port if your Flask backend uses a different one
                files=files,
                timeout=60
            )
            if response.status_code == 200:
                results = response.json()
                if isinstance(results, dict):  # If backend returns a single result
                    results = [results]
                st.success("Here are your top matches!")
                for idx, result in enumerate(results, 1):
                    st.subheader(f"Match #{idx}: {result.get('label', 'Unknown')}")
                    st.image(
                        "data:image/jpeg;base64," + result.get("image_base64", ""),
                        caption=f"Similarity: {result.get('similarity', 0):.2f}",
                        use_column_width=True
                    )
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
else:
    st.info("Please upload or capture an image to begin.")