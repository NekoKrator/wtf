import streamlit as st
import pandas as pd
import plotly.express as px

# Загрузка данных
@st.cache
def load_data():
    data = pd.read_csv('jm1_processed.csv')  # Путь к файлу с данными
    return data

df = load_data()

# Заголовок и описание
st.title("Визуализация даних з лабораторної роботи №1")
st.write("Цей додаток використовує дані з лабораторної роботи для візуалізації впливу різних метрик на дефекти.")

# Вибір змінних для візуалізації
st.sidebar.header("Параметри для візуалізації")
selected_columns = st.sidebar.multiselect("Оберіть змінні для візуалізації", df.columns)

# Фільтрація за умовою
min_value = st.sidebar.number_input("Фільтрувати за мінімальним значенням", value=0.0)
filtered_data = df[df[selected_columns[0]] > min_value] if selected_columns else df

# Вибір типу графіка
chart_type = st.sidebar.radio("Оберіть тип графіка", ["Точковий", "Коробкова діаграма"])

# Візуалізація
if chart_type == "Точковий":
    if len(selected_columns) >= 2:
        fig = px.scatter(filtered_data, x=selected_columns[0], y=selected_columns[1], color="defects", title="Точковий графік")
        st.plotly_chart(fig)
    else:
        st.write("Будь ласка, виберіть щонайменше дві змінні для візуалізації.")
else:
    if len(selected_columns) >= 1:
        fig = px.box(filtered_data, y=selected_columns[0], color="defects", title="Коробкова діаграма")
        st.plotly_chart(fig)
    else:
        st.write("Будь ласка, виберіть хоча б одну змінну для візуалізації.")

# Показати таблицю з даними
st.subheader("Таблиця з даними")
st.dataframe(filtered_data)
