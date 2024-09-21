import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
data = pd.read_csv("sales_data.csv")

# Просмотр первых строк данных
print("Данные о продажах за 1 квартал 2023 года:")
print(data.head())

# Фильтрация данных за 1 квартал 2023 года
quarter_data = data[(data['date'] >= '2023-01-01') & (data['date'] <= '2023-03-31')]

# Агрегирование данных: общие продажи по категориям
sales_by_category = quarter_data.groupby('category')['sales'].sum()

# Вывод на экран суммы продаж по категориям
print("\nСумма продаж по категориям за 1 квартал 2023 года:")
print(sales_by_category)

# Построение диаграммы
sales_by_category.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category (Q1 2023)')
plt.ylabel('Sales (in $)')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение диаграммы в файл
plt.savefig("sales_by_category.png")

# Показ диаграммы
plt.show()
