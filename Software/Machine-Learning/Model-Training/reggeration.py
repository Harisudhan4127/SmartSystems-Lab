import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics  import accuracy_score

student_data = {
    'hours_studied' : [1,2,3,4,5,6,7,8,9],
    'marks_scored' : [35,47,53,62,71,77,82,86,89]
}

student_df = pd.DataFrame(student_data)

# print(student_df.head(10))

x = student_df[['hours_studied']]
y = student_df['marks_scored']

lr = LinearRegression()
lr.fit(x,y)

print(lr.fit(x,y))

min_data = {'hours_studied' : [5]}
min_df = pd.DataFrame(min_data)

predication = lr.predict(min_df[['hours_studied']])

print(predication)