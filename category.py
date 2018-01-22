# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:48:34 2018

@author: Administrator
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


#读取文件
readFileName="test.xlsx"
#读取excel
df=pd.read_excel(readFileName)

ser1=df["黑中介分数"]


def f(x):
    if 100>=x>=80:
        return "[80,100]"
    if 79>=x>=60:
        return "[60,79]"
    if 59>=x>=40:
        return "[40,59]"  
    if 39>=x>=20:
        return "[20,39]"     
    if 19>=x>=11:
        return "[11,19]" 
    if 10>=x>=6:
        return "[6,10]"  
    if 5>=x>=0:
        return "[0,5]"  
        
ser2=ser1.map(f)

df1=pd.DataFrame({"黑中介分数":ser1,"分类":ser2},columns=["黑中介分数","分类"])

df1.to_excel("save.xlsx")





