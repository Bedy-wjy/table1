# -*- coding:utf-8 -*-
"""
作者: bedy
日期: 2024年05月05日
"""
import streamlit as st
from PIL import Image
import numpy as np
import os
import paddlehub as hub
import cv2
stylepro_artistic = hub.Module(name="stylepro_artistic")
st.markdown('### 梵高星空夜图像风格迁移')
st.write('点击 Browse files 上传张图片，生成梵高星空夜风格的图片，赶快试试吧~')
with st.form(key="图像风格迁移"):
    per_image = st.file_uploader("上传图片", type=['png', 'jpg','jpeg'], label_visibility='hidden')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('#### 原始图片')
        if per_image:
            st.image(per_image)
        else:
            st.image("https://codelab-public.bj.bcebos.com/base.jpeg")
    submit = st.form_submit_button("开始生成")
    with col2:
        st.markdown('#### 预测结果')
        if per_image:
            img = Image.open(per_image)
            img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
            result =stylepro_artistic.style_transfer(images=
            [{
            'content': img,
            'styles': [cv2.imread(os.path.join(os.path.dirname(os.path.realpath(__file__)),'StarryNight.png'))]
            }])
            st.image(result[0]['data'])
        else:
            st.image("https://codelab-public.bj.bcebos.com/test.jpeg")
st.markdown('#### 梵高星空夜作品展示')
st.image("https://bkimg.cdn.bcebos.com/pic/d01373f082025aafcce937a8f7eda")