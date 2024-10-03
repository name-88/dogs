from cProfile import label
from http.client import responses
from tkinter import messagebox as mb
from tkinter *
import requests
from PIL import Image, ImageTk
from io import BytesIO

from requests import request


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            label.config(image-img)
            label.image = img
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка {e}")




# Главное окно
window = Tk()
window.title("Фото собак")
window.geometry(360x420)

label = Label()
label.pack(pady=10)

button = Button(text="Загрузить фото", command=show_image)
button.pack(pady=10)