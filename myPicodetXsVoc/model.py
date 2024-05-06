# -*- coding:utf-8 -*-
"""
作者: bedy
日期: 2024年05月06日
"""
import paddle

# 定义模型的类
class MyModel(paddle.nn.Layer):
    def __init__(self):
        super(MyModel, self).__init__()
        # 定义模型的层

    def forward(self, x):
        # 定义前向传播逻辑
        return x

# 加载模型参数
model = MyModel()
paddle.load('pdiparams.pdiparams', model)

# 使用模型进行训练或推理
