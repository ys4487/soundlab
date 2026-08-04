import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter

sample_rate = 44100
duration = 1800

t = np.linspace(0, duration, int(sample_rate * duration), False)

# 1. תדרי דלתא (פער של 2 הרץ בלבד)
freq_left = 150.0
freq_right = 152.0
wave_left = np.sin(2 * np.pi * freq_left * t) * 0.4
wave_right = np.sin(2 * np.pi * freq_right * t) * 0.4

# 2. ייצור רעש חום
white_noise = np.random.normal(0, 1, sample_rate * duration)
brown_noise = lfilter([1], [1, -0.98], white_noise)
brown_noise -= np.mean(brown_noise)
brown_noise_normalized = (brown_noise / np.max(np.abs(brown_noise))) * 0.3 # רעש חום קצת יותר מורגש לשינה

# 3. חיבור
left_channel = wave_left + brown_noise_normalized
right_channel = wave_right + brown_noise_normalized

stereo_signal = np.vstack((left_channel, right_channel)).T
stereo_signal = np.int16((stereo_signal / np.max(np.abs(stereo_signal))) * 32767)

write('delta_brown.wav', sample_rate, stereo_signal)
print("קובץ דלתא (שינה) משולב עם רעש חום נוצר!")