import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile

st.set_page_config(page_title="Détecteur d’objets IA", layout="centered")
st.title("Détecteur d’objets dans une image")

uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Image d’origine", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image.save(tmp.name)
        model = YOLO("yolov8n.pt")
        results = model(tmp.name)
        boxes = results[0].plot()  # Annotated image

        st.image(boxes, caption="Objets détectés", use_container_width=True)