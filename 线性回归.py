# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:21:31 2020

@author: jiawei
"""


import numpy as np

ud=(0,5,-3,3,-2,8 )#自变量采样区间
c=(5,2,4,-3)
er=0.01

m=10
v=np.zeros((m,3))

for i in range(3): 
    r1=er*np.random.random(m)
    v[:,i]=np.linspace(ud[2*i],ud[2*i+1],m)+r1
    
Y=er*np.random.random((m,1))+c[0]

for i in range(3):
    Y[:,0]+=v[:,i]*c[i+1]
    
X=np.zeros((m,4));
X[:,0]=1;
X[:,1:]=v
# 构建采样数据 Y 和 X。

# 线性回归解 Y=X.C。特别 X的行数大于列数。
M=X.T.conjugate();
A=M.dot(X);
B=M.dot(Y);
AI=np.linalg.linalg.inv(A)
C1=AI.dot(B);
# 或者  C2=np.linalg.solve(A,B)
print('c=',np.ravel(C1));
error=np.max(X.dot(C1)-Y).round(4)
print('error=',error)
# 实际工作中Y 和 X可能来源于实验。