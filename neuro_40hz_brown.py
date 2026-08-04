import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter

sample_rate = 44100
duration = 1800  # 30 דקות

t = np.linspace(0, duration, int(sample_rate * duration), False, dtype=np.float32)

base_freq = 150.0
beat_freq = 40.0
base_wave = np.sin(2 * np.pi * base_freq * t).astype(np.float32)
envelope = (np.sin(2 * np.pi * beat_freq * t)**2).astype(np.float32)
isochronic_wave = base_wave * envelope * 0.4

one_minute_samples = sample_rate * 60
white_1_min = np.random.normal(0, 1, one_minute_samples).astype(np.float32)
brown_1_min = lfilter([1], [1, -0.98], white_1_min)
repeats = int(np.ceil(duration / 60))
brown_noise = np.tile(brown_1_min, repeats)[:len(t)]

brown_noise -= np.mean(brown_noise, dtype=np.float32)
brown_noise = (brown_noise / np.max(np.abs(brown_noise))) * 0.3

combined_channel = isochronic_wave + brown_noise

del isochronic_wave
del brown_noise

stereo_signal = np.vstack((combined_channel, combined_channel)).T
del combined_channel

stereo_signal /= np.max(np.abs(stereo_signal))
stereo_signal *= 32767
stereo_signal = stereo_signal.astype(np.int16)

write('neuro_40hz_brown.wav', sample_rate, stereo_signal)
print("הקובץ הנוירולוגי 40Hz עם רעש חום נוצר בהצלחה!")