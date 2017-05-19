from bencoder import  bdecode
import sys
reload(sys)
sys.setdefaultencoding('utf8') # 设置编码
li =open('tt.txt','rb')
ll=li.readlines()
nname=open('name.txt','wb')

for tl in ll :
    with open(tl.replace('\r\n',''),'rb') as f:
        torrent=bdecode(f.read())
        nn=torrent['info']['name']
		nname.write(f.name+'=')
		nname.write(nn.encode('utf-8')+'.torrent'+'\r\n')
        print(f.name)
