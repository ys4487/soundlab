import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter

sample_rate = 44100
duration = 1800  # 30 דקות

t = np.linspace(0, duration, int(sample_rate * duration), False, dtype=np.float32)

# תדר 741 הרץ עם פער אלפא להרגעה מנטלית (10 הרץ)
freq_left = 741.0
freq_right = 751.0
wave_left = (np.sin(2 * np.pi * freq_left * t) * 0.25).astype(np.float32)
wave_right = (np.sin(2 * np.pi * freq_right * t) * 0.25).astype(np.float32)

one_minute_samples = sample_rate * 60
white_1_min = np.random.normal(0, 1, one_minute_samples).astype(np.float32)
brown_1_min = lfilter([1], [1, -0.98], white_1_min)
repeats = int(np.ceil(duration / 60))
brown_noise = np.tile(brown_1_min, repeats)[:len(t)]

brown_noise -= np.mean(brown_noise, dtype=np.float32)
brown_noise = (brown_noise / np.max(np.abs(brown_noise))) * 0.3

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

write('anger_release_741hz.wav', sample_rate, stereo_signal)
print("קובץ שחרור כעסים 741Hz נוצר בהצלחה!")