# encoding:utf-8
import base64
from io import BytesIO
from urllib import parse, request
from PIL import Image
'''
人脸检测与属性分析
'''
# [调用鉴权接口获取的token]
access_token = '24.06e8f29ad866fa60eaa5651318b5b921.2592000.1527857966.282335-10033669'
params = {"face_field": "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
          "face_type": "LIVE", "image": '', "image_type": "BASE64", "max_face_num": 10}

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
request_url = request_url + "?access_token=" + access_token

fPath = 'D:\个人\picture\picture\经济学院大合影.jpg'
A = {
    "access_token": "24.06e8f29ad866fa60eaa5651318b5b921.2592000.1527857966.282335-10033669",
    "session_key": "9mzdCy57TlIrlKSrkIcBFb2T2\\/KbVG7yuckmVuu4Jeml83Ua\\/5ZB553wS+HklFwhackDnb4OA5OhqYyYpvolTLIqycTiAg==",
    "scope": "vis-faceverify_FACE_V3 vis-ocr_ocr brain_ocr_general brain_ocr_general_basic brain_solution brain_ocr_accurate brain_ocr_accurate_basic vis-faceverify_faceverify_v2 vis-faceattribute_faceattribute vis-faceverify_vis-faceverify-detect vis-faceverify_faceverify vis-faceverify_faceverify_match_v2 public brain_all_scope wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\\u6743\\u9650 vis-classify_flower lpq_\\u5f00\\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base",
    "refresh_token": "25.4f708d85aeb73518cd384701e4ce7ee4.315360000.1840625966.282335-10033669",
    "session_secret": "cbc0ab3c953a927e0653e291b71746a4",
    "expires_in": 2592000
}

# 二进制方式打开图片文件


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return base64.b64encode(fp.read())


#img = get_file_content(fPath)


def image_to_base64(image_path):
    img = Image.open(image_path)
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


XY = (100, 450, 6600, 1100)
XX = 300
YY = 300

params['image'] = img
params = parse.urlencode(params).encode(encoding='UTF8')

req = request.Request(url=request_url, data=params)
# ('Content-Type', 'application/x-www-form-urlencoded')
req.add_header('Content-Type', 'application/json')
response = request.urlopen(req)
content = response.read()
if content:
    print(content)
