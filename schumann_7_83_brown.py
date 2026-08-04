import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter

sample_rate = 44100
duration = 1800  # 30 דקות

t = np.linspace(0, duration, int(sample_rate * duration), False, dtype=np.float32)

freq_left = 136.1
freq_right = 136.1 + 7.83
wave_left = (np.sin(2 * np.pi * freq_left * t) * 0.3).astype(np.float32)
wave_right = (np.sin(2 * np.pi * freq_right * t) * 0.3).astype(np.float32)

one_minute_samples = sample_rate * 60
white_1_min = np.random.normal(0, 1, one_minute_samples).astype(np.float32)
brown_1_min = lfilter([1], [1, -0.98], white_1_min)
repeats = int(np.ceil(duration / 60))
brown_noise = np.tile(brown_1_min, repeats)[:len(t)]

brown_noise -= np.mean(brown_noise, dtype=np.float32)
brown_noise = (brown_noise / np.max(np.abs(brown_noise))) * 0.4

left_channel = wave_left + brown_noise
right_channel = wave_right + brown_noise

del wave_left
del wave_right
del brown_noise

stereo_signal = np.vstack((left_channel, right_channel)).T
del left_channel
del right_channel

stereo_signal /= np.max(np.abs(stereo_signal))
stereo_signal *= 32767
stereo_signal = stereo_signal.astype(np.int16)

write('schumann_7_83_brown.wav', sample_rate, stereo_signal)
print("קובץ תהודת שומאן 7.83Hz עם רעש חום נוצר בהצלחה!")