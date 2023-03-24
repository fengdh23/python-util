# -*- coding: utf-8 -*-
# 引入依赖包 Label 7个颜色是否可以实际场景的颜色一致，血清的颜色？透明
# pip install alibabacloud_imagerecog20190930

# 1. 1个颜色 不应该返回2个结果
# 2. 2个颜色，不能返回一个结果,三个+结果

import io
from urllib.request import urlopen
from alibabacloud_imagerecog20190930.client import Client
from alibabacloud_imagerecog20190930.models import RecognizeImageColorAdvanceRequest
from alibabacloud_tea_openapi.models import Config
from alibabacloud_tea_util.models import RuntimeOptions

config = Config(
  # "YOUR_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_SECRET" 的生成请参考 https://help.aliyun.com/document_detail/175144.html
  # 如果您是用的子账号AccessKey，还需要为子账号授予权限AliyunVIAPIFullAccess，请参考https://help.aliyun.com/document_detail/145025.html
  # 您的 AccessKey ID
  access_key_id='LTAI5t7fZAUQseupHW6n4ZUH',
  # 您的 AccessKey Secret
  access_key_secret='8Q7Adu7E8IQllskrKvBjcR8Iot0MPO',
  # 访问的域名
  endpoint='imagerecog.cn-shanghai.aliyuncs.com',
  # 访问的域名对应的region
  region_id='cn-shanghai'
)
#场景一：文件在本地
stream = open(r'C:\\Users\\fdh32\\Pictures\\1-blue.png', 'rb')
#场景二：使用任意可访问的url
# url = 'https://viapi-test-bj.oss-cn-beijing.aliyuncs.com/viapi-3.0domepic/imagerecog/RecognizeImageColor/RecognizeImageColor1.jpg'
# img = urlopen(url).read()
recognize_image_color_request = RecognizeImageColorAdvanceRequest(
    #场景一：文件在本地
    url_object=stream,
    # url_object=io.BytesIO(img),
    color_count=2
)
runtime = RuntimeOptions()
try:
  # 初始化Client
  client = Client(config)
  response = client.recognize_image_color_advance(recognize_image_color_request, runtime)
  # 获取整体结果
  print(response.body)
except Exception as error:
  # 获取整体报错信息
  print(error)
  # 获取单个字段
  print(error.code)

#关闭流
#stream.close()