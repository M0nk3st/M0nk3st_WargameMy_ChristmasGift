from PIL import Image

# Ruta del archivo GIF
gif_path = "gift.gif"

# Abrir el archivo GIF
gif = Image.open(gif_path)

# Extraer los fotogramas del GIF
frames = []
while True:
    frames.append(gif.copy())  # Guardar el fotograma actual
    try:
        gif.seek(gif.tell() + 1)  # Mover al siguiente fotograma
    except EOFError:
        break  # Salir cuando se acaben los fotogramas

# Obtener los últimos 15 fotogramas
last_15_frames = frames[-15:]

# Guardar los últimos 15 fotogramas
for i, frame in enumerate(last_15_frames):
    frame.save(f"last_frame_{i+1}.png")
