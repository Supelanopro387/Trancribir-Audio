import whisper

# Ruta del archivo .m3u
archivo_m3u = r"C:\Users\nicop\Videos\Music\T3M4CH1N45.m3u"

# Leer las rutas desde el archivo .m3u
with open(archivo_m3u, "r", encoding="utf-8") as f:
    rutas_audios = [line.strip() for line in f if not line.startswith("#") and line.strip()]

# Cargar el modelo de Whisper
modelo = whisper.load_model("medium")  # Cambiá "base" por "small", "medium", o "large" si querés más precisión

# Transcribir cada archivo de audio
for ruta_audio in rutas_audios:
    if ruta_audio.endswith((".m4a", ".mp3")):  # Verifica que sea un archivo de audio válido
        print(f"Transcribiendo: {ruta_audio}...")
        resultado = modelo.transcribe(ruta_audio, language="es")  # Transcribir en español
        
        # Guardar la transcripción en un archivo .txt
        nombre_salida = ruta_audio.split("\\")[-1].replace(".m4a", ".txt").replace(".mp3", ".txt")
        ruta_salida = "\\".join(ruta_audio.split("\\")[:-1]) + "\\" + nombre_salida
        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.write(resultado["text"])
        
        print(f"Transcripción guardada en: {ruta_salida}")

print("¡Listo! Todas las transcripciones han sido procesadas.")
