# -*- coding:utf-8 -*-
"""
作者: bedy
日期: 2024年04月30日
"""
import streamlit as st
import cv2
from PIL import Image
import numpy as np

# 在侧边栏中添加标题和说明文本
st.sidebar.title("图像表格识别")
st.sidebar.write("上传图片并进行表格识别")

# 在主界面中添加标题
st.title("图像表格识别应用程序")

# 允许用户上传图像文件
uploaded_image = st.file_uploader("上传图像", type=["jpg", "jpeg", "png"])

# 如果用户上传了图片
if uploaded_image is not None:
    # 将上传的图像转换为OpenCV格式
    image = Image.open(uploaded_image)
    opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # 使用PPYOLO模型进行图像识别（假设你有一个名为detect_table的函数来调用PPYOLO模型）
    detected_image = detect_table(opencv_image)

    # 将识别结果显示在界面上
    st.image(detected_image, caption="识别结果", use_column_width=True)
