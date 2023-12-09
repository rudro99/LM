import pandas as pd

df = pd.read_excel('dataset1.xlsx')

print(df)

age_mean = df['Age'].mean()

print("Age mean = ", age_mean)

salary_mean = df['Salary'].mean()

print('Salary mean = ', salary_mean)

df['Age'] = df['Age'].fillna(age_mean)
df['Salary'] = df['Salary'].fillna(salary_mean)

print(df)

df.to_excel('updated_dataset1.xlsx')