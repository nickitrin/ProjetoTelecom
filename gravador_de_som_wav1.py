import sounddevice as sd
import numpy as np
from scipy.io import wavfile

# Defina as configurações de gravação
fs = 44100  # Taxa de amostragem (em Hz)
duration = 10  # Duração da gravação em segundos

# Função para gravar áudio
def record_audio(filename, duration, fs):
    print("Iniciando gravação...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    print("Gravação concluída.")

    # Salve os dados do áudio em um arquivo WAV
    wavfile.write(filename, fs, audio_data)

# Nome do arquivo de saída
output_filename = "audio_gravado.wav"

# Chame a função para gravar áudio
record_audio(output_filename, duration, fs)

print(f"Áudio gravado e salvo como {output_filename}")
