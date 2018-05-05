from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '10033669'
API_KEY = 'FqQdAifvOsvadi5s8QEEHhXB'
SECRET_KEY = 'Y5jChkCNbSEhjdYZ4OjwGODqoMC7MBvY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
filePath = '微信图片_20180425104357.jpg'
with open(filePath, 'rb') as fp:
    image = fp.read()

""" 调用表格文字识别 """
res = client.tableRecognitionAsync(image);

#requestId = "10033669_251679"
requestId = res['result']["request_id"]

""" 调用表格识别结果 """
client.getTableRecognitionResult(requestId);

""" 如果有可选参数 """
options = {}
options["result_type"] = "excel"

""" 带参数调用表格识别结果 """
client.getTableRecognitionResult(requestId, options)
