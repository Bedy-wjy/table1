import streamlit as st
from PIL import Image
import pytesseract

def main():
    st.title("图像表格识别应用")
    st.write("上传一张包含表格的图片，我们将识别其中的文本。")

    uploaded_image = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="上传的图片", use_column_width=True)

        if st.button("识别文本"):
            extracted_text = perform_ocr(image)
            st.subheader("提取的文本结果：")
            st.write(extracted_text)

def perform_ocr(image):
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

if __name__ == "__main__":
    main()
