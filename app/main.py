
import streamlit as st
from PIL import Image

st.set_page_config(page_title="YouTube Analytics", layout="wide")

st.title("YouTube Channel Performance Analytics")
st.markdown("""

Добро пожаловать!  
Используйте меню слева для перехода по страницам:  
- Обзор данных,  
- Инсайты
- Предсказания.  
""")
image = Image.open("photo_2024-12-18 00.56.25.jpeg")
width, height = image.size
new_width = 200
new_height = int((new_width / width) * height)
image = image.resize((new_width, new_height))
st.image(image, caption="Борис", use_column_width=0)
