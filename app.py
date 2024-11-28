import streamlit as st
from diffusers import DiffusionPipeline

# Загрузка модели
pipe = DiffusionPipeline.from_pretrained("John6666/mala-anime-mix-nsfw-pony-xl-v3-sdxl")

# Заголовок страницы
st.title("Image Generation with Diffusers")

# Ввод текста пользователем
prompt = st.text_input("Enter your prompt", "nude girl")

# Генерация изображения
if st.button("Generate Image"):
    image = pipe(prompt).images[0]
    st.image(image, caption="Generated Image", use_column_width=True)