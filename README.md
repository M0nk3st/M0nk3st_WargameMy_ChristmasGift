to solve this chall as its title said that we have to wait for the end i assumed i only had to take the last photograms of the gift,
so i made this pyhton script:

from PIL import Image

Ruta del archivo GIF
gif_path = "gift.gif"

Abrir el archivo GIF
gif = Image.open(gif_path)

Extraer los fotogramas del GIF
frames = []
while True:
    frames.append(gif.copy())  # Guardar el fotograma actual
    try:
        gif.seek(gif.tell() + 1)  # Mover al siguiente fotograma
    except EOFError:
        break  # Salir cuando se acaben los fotogramas

Obtener los últimos 15 fotogramas
last_15_frames = frames[-15:]

Guardar los últimos 15 fotogramas
for i, frame in enumerate(last_15_frames):
    frame.save(f"lastframe{i+1}.png")


This solver get the 15 last photograms just in case it had more information in other photogram and that was all :D
