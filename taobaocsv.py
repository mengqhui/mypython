# -*- coding:utf-8 -*-
import pandas as pd
import re

def read_taobaocsv(filepath)
	df=pd.read_csv(filepath,sep='\t',encoding='utf-16',header=2)
	print len(df)

def to_taobaocsv(filepath)
	df.to_csv(filepath,sep='\t',index=False,encoding='UTF-16')

def replace_phone(df)
	for description in df[u'宝贝描述']:
		re.sub('1\d{10}','18621631419',description)
		print description

def num(df)
	df[u'宝贝数量']=[random.randint(900,1000) for _ in range(len(df))]

import random

[random.randint(900,1000) for _ in range(len(df))]
#[57, 93, 22, 55, 41, 64, 47, 32, 93, 61]


