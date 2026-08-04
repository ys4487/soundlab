import numpy as np
from scipy.io.wavfile import write

sample_rate = 44100
duration = 1800  # 30 דקות

t = np.linspace(0, duration, int(sample_rate * duration), False, dtype=np.float32)

# תדרי תטא לחלום צלודי (פער של 6 הרץ)
freq_left = 200.0
freq_right = 206.0
wave_left = (np.sin(2 * np.pi * freq_left * t) * 0.25).astype(np.float32)
wave_right = (np.sin(2 * np.pi * freq_right * t) * 0.25).astype(np.float32)

def generate_pink_noise(samples):
    white = np.random.randn(samples).astype(np.float32)
    X = np.fft.rfft(white)
    S = np.sqrt(np.arange(X.size) + 1.0).astype(np.float32)
    Y = X / S
    return np.fft.irfft(Y, samples).astype(np.float32)

one_minute_samples = sample_rate * 60
pink_noise_1_min = generate_pink_noise(one_minute_samples)
repeats = int(np.ceil(duration / 60))
pink_noise = np.tile(pink_noise_1_min, repeats)[:len(t)]

pink_noise -= np.mean(pink_noise, dtype=np.float32)
pink_noise = (pink_noise / np.max(np.abs(pink_noise))) * 0.25

left_channel = wave_left + pink_noise
right_channel = wave_right + pink_noise

del wave_left
del wave_right
del pink_noise

stereo_signal = np.vstack((left_channel, right_channel)).T
del left_channel
del right_channel

stereo_signal /= np.max(np.abs(stereo_signal))
stereo_signal *= 32767
stereo_signal = stereo_signal.astype(np.int16)

write('lucid_dream_6hz.wav', sample_rate, stereo_signal)
print("קובץ חלום צלודי 6Hz נוצר בהצלחה!")