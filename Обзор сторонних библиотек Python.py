# Pandas
import pandas as pd

# pandas - мощная библиотека для анализа данных, которая позволяет считывать, обрабатывать и анализировать данные.

#	Чтение данных: метод pd.read_csv() позволяет загрузить данные из CSV-файла в DataFrame.
df = pd.read_csv("data.csv")
print(df)

#	Фильтрация данных: с помощью методов DataFrame можно отфильтровать строки и столбцы по различным критериям.
filter_df = df[df["age"] > 30]
print(filter_df)

#	Агрегация данных: метод .groupby() позволяет группировать данные по определенному столбцу и применять агрегатные функции (например, sum, mean, count).
avg_salary = df.groupby("city")["salary"].mean()
print(avg_salary)

# Matplotlib
import matplotlib.pyplot as plt

# matplotlib - это библиотека для визуализации данных.

#	Построение линейного графика: функция plt.plot() позволяет создать линейный график на основе переданных данных.
years = [2018, 2019, 2020, 2021]
values = [150, 200, 250, 300]

plt.plot(years, values, label="Revenue", color="blue", marker="o")
plt.xlabel("Year")
plt.ylabel("Revenue (in thousands)")
plt.title("Company Revenue Over Years")
plt.legend()
plt.show()

#	Гистограмма: plt.hist() создаёт гистограмму, полезную для анализа распределения данных.
data = [20, 20, 22, 23, 23, 25, 25, 25, 30, 35, 40, 45]
plt.hist(data, bins=5, color="green", edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Data Distribution")
plt.show()

#	Настройка графика: можно настроить оси, заголовок и легенду графика с помощью функций plt.xlabel, plt.ylabel, и plt.title и тд.
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 87, 94, 78, 77, 85]

plt.scatter(x, y, color="purple")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot Example")
plt.show()