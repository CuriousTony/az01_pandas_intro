import pandas as pd

# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).
df = pd.read_csv('World-happiness-report-2024.csv')
print(df.head(6))
print(df.info())
print(df.describe())

# Определите среднюю зарплату (Salary) по городу (City)
new_df = pd.read_csv('dz.csv')
avg_slry = new_df.groupby('City')['Salary'].mean()
print(avg_slry)
