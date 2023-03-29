import pandas as pd
import numpy as np
import matplotlib.pyplot as mt
from sklearn import linear_model
import math

df = pd.read_csv("C:/Users/admin/Desktop/SubjectiveAnswerEvaluation/finaldataset.csv")
df

reg = linear_model.LinearRegression()

reg.fit(df[['keyword','grammar','length','class']],df.marks)

reg.coef_

reg.intercept_

#Answer converted into list and compare with keyword

ans = input("Enter Your Answer ")

keyword = input("Enter The Keyword ")


a = ans.split()
k = keyword.split()

count = 0
for i in a:
    for j in k:
        if i==j:
            count=count+1
k = count

#grammar mistake counts

from gingerit.gingerit import GingerIt

result = GingerIt().parse(ans)

g = len(result['corrections'])

#length of answer

answer = ans.split(". ")

length = len(answer)

l = length

c = int(input("Enter The Class Of Student "))
m = int(input("Enter The Maximum Marks "))


r = reg.predict([[k,g,l,c]])

res = math.ceil(r)

updatedmarks=0

if res>=m:
    updatedmarks = m
elif res<0:
    updatedmarks = 0
else:
    updatedmarks = res

print("Student Got " + str(updatedmarks) +  " Marks in Exam")
