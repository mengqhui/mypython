import pandas  
with open('C:\Users\zhaoyingh\Desktop\\a.txt','r') as f:  
    df = pandas.read_html(f.read().decode("gb2312").encode('utf-8'),encoding='utf-8')  
print df[0]  
bb = pandas.ExcelWriter('out.xlsx')  
df[0].to_excel(bb)  
bb.close()  