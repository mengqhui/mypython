from aip import AipOcr

""" ��� APPID AK SK """
APP_ID = '10033669'
API_KEY = 'FqQdAifvOsvadi5s8QEEHhXB'
SECRET_KEY = 'Y5jChkCNbSEhjdYZ4OjwGODqoMC7MBvY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" ��ȡͼƬ """
filePath = '΢��ͼƬ_20180425104357.jpg'
with open(filePath, 'rb') as fp:
    image = fp.read()

""" ���ñ������ʶ�� """
res = client.tableRecognitionAsync(image);

#requestId = "10033669_251679"
requestId = res['result']["request_id"]

""" ���ñ��ʶ���� """
client.getTableRecognitionResult(requestId);

""" ����п�ѡ���� """
options = {}
options["result_type"] = "excel"

""" ���������ñ��ʶ���� """
client.getTableRecognitionResult(requestId, options)
