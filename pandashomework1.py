import pandas as pd
from datetime import datetime


data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'IT'],
    'Salary': [70000, 80000, 75000, 60000, 72000],
    'JoiningDate': ['2020-01-15', '2019-03-12', '2021-07-23', '2018-11-30', '2019-05-19']
}

# Создание DataFrame
df = pd.DataFrame(data)

# Преобразуем дату в формат datetime
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])
print("DataFrame о сотрудниках:\n", df)

# --- Просмотр данных ---
print("\nПервые 3 строки DataFrame:")
print(df.head(3))

print("\nПоследние 2 строки DataFrame:")
print(df.tail(2))

# --- Фильтрация данных ---
print("\nСотрудники с зарплатой больше 70,000:")
print(df[df['Salary'] > 70000])

print("\nСотрудники, работающие в отделе IT:")
print(df[df['Department'] == 'IT'])

# --- Агрегация данных ---
print("\nСредняя зарплата сотрудников:", df['Salary'].mean())
print("Максимальная зарплата среди сотрудников:", df['Salary'].max())

# --- Сортировка данных ---
print("\nСотрудники, отсортированные по зарплате (убывание):")
print(df.sort_values(by='Salary'))

# --- Добавление нового столбца ---
current_date = datetime.now()
df['YearsAtCompany'] = (current_date - df['JoiningDate']).dt.days // 365

print("\nDataFrame с добавленным столбцом 'YearsAtCompany':")
print(df)

# --- Изменение значения ---
df.loc[df['EmployeeID'] == 104, 'Salary'] = 65000
print("\nDataFrame после изменения зарплаты сотрудника с ID 104:")
print(df)


# ------------задание 2------------


data = {
    'OrderID': [201, 202, 203, 204, 205],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Mouse'],
    'Quantity': [1, 3, 2, 1, 2],
    'Price': [1200, 25, 75, 300, 25],
    'OrderDate': ['2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14']
}

df_sales = pd.DataFrame(data)
df_sales['OrderDate'] = pd.to_datetime(df_sales['OrderDate'])

print("DataFrame о продажах:\n", df_sales)

# ---  Общий доход от продаж ---
df_sales['Total'] = df_sales['Quantity'] * df_sales['Price']
total_revenue = df_sales['Total'].sum()
print("\nОбщий доход от продаж:", total_revenue)

# --- Продукт, купленный в наибольшем количестве ---
most_bought = df_sales.groupby('Product')['Quantity'].sum().idxmax()
print("Продукт, купленный в наибольшем количестве:", most_bought)

# ---  Заказы, где количество товара больше 1 ---
print("\nЗаказы, где количество товара больше 1:")
print(df_sales[df_sales['Quantity'] > 1])




#-------------задание 3---------------

data = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Jane', 'Alice', 'Bob', 'Charlie'],
    'Course': ['Math', 'Science', 'Math', 'History', 'Science'],
    'Grade': [85, 90, 78, 88, 92]
}


df_students = pd.DataFrame(data)
print("DataFrame о студентах:\n", df_students)

# --- Средняя оценка по каждому курсу ---
avg_grade = df_students.groupby('Course')['Grade'].mean()
print("\nСредняя оценка по каждому курсу:")
print(avg_grade)

# --- Студент с наивысшей оценкой ---
top_student = df_students.loc[df_students['Grade'].idxmax()]
print("\nСтудент с наивысшей оценкой:")
print(top_student)

# --- Добавление столбца 'Pass/Fail' ---
df_students['Pass/Fail'] = df_students['Grade'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
print("\nDataFrame с добавленным столбцом 'Pass/Fail':")
print(df_students)



#-----------задание 4----------


data = {
    'Date': ['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05', '2024-08-06', '2024-08-07'],
    'Temperature': [23.5, 24.0, 22.0, 22.8, 23.0, 24.2, 25.1, 24.8]
}

df_temp = pd.DataFrame(data)
df_temp['Date'] = pd.to_datetime(df_temp['Date'])
print('DataFrame  о температуре:\n',df_temp)


# --- Средняя температура за неделю ---
avg_temp = df_temp['Temperature'].mean()
print("\nСредняя температура за неделю:", round(avg_temp, 2))

# --- Максимальная и минимальная температура ---
max_temp = df_temp['Temperature'].max()
min_temp = df_temp['Temperature'].min()
print("Максимальная температура:", max_temp)
print("Минимальная температура:", min_temp)

# ---Добавление столбца 'AboveAverage' ---
df_temp['AboveAverage'] = df_temp['Temperature'] > avg_temp
print("\nDataFrame с добавленным столбцом 'AboveAverage':")
print(df_temp)