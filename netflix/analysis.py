import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from IPython.display import display

# Настройки отображения pandas
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
pd.set_option("display.max_colwidth", 120)

# Настройки графиков
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 12

DATA_PATH = "netflix_titles.csv"

df = pd.read_csv(DATA_PATH)

print("Размер датасета:", df.shape)
display(df.head())

# Первчиные данные
print("\nИнформация о колонках:")
df.info()

print("\nНазвания колонок:")
print(df.columns.tolist())

print("\nКоличество строк и колонок:")
print(f"Строк: {df.shape[0]}")
print(f"Колонок: {df.shape[1]}")

print("\nПервые 5 строк:")
display(df.head())

print("\nСлучайные 5 строк:")
display(df.sample(5, random_state=42))

# Проверка дубликатов
print("Количество полных дубликатов:", df.duplicated().sum())
print("Количество дубликатов по show_id:", df["show_id"].duplicated().sum())
print("Количество дубликатов по title:", df["title"].duplicated().sum())

# Удаление полных дубликатов
df = df.drop_duplicates()
