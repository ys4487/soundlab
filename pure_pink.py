import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100
duration = 1800  # 30 דקות

def generate_pink_noise(samples):
    white = np.random.randn(samples).astype(np.float32)
    X = np.fft.rfft(white)
    S = np.sqrt(np.arange(X.size) + 1.0).astype(np.float32)
    Y = X / S
    return np.fft.irfft(Y, samples).astype(np.float32)

one_minute_samples = sample_rate * 60
pink_1_min = generate_pink_noise(one_minute_samples)
repeats = int(np.ceil(duration / 60))
pink_noise = np.tile(pink_1_min, repeats)[:int(sample_rate * duration)]

pink_noise -= np.mean(pink_noise, dtype=np.float32)
pink_noise = (pink_noise / np.max(np.abs(pink_noise))) * 32767
pink_noise = pink_noise.astype(np.int16)

stereo_signal = np.vstack((pink_noise, pink_noise)).T

write('pure_pink.wav', sample_rate, stereo_signal)
print("קובץ רעש ורוד טהור נוצר בהצלחה!")