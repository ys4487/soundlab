import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter

sample_rate = 44100
duration = 1800  # שנה ל-900 עבור 15 דקות

t = np.linspace(0, duration, int(sample_rate * duration), False)

# 1. תדרי אלפא (פער של 10 הרץ) בווליום בינוני
freq_left = 400.0
freq_right = 410.0
wave_left = np.sin(2 * np.pi * freq_left * t) * 0.4
wave_right = np.sin(2 * np.pi * freq_right * t) * 0.4

# 2. ייצור רעש חום נעים ורך ברקע
white_noise = np.random.normal(0, 1, sample_rate * duration)
brown_noise = lfilter([1], [1, -0.98], white_noise)
brown_noise -= np.mean(brown_noise)
brown_noise_normalized = (brown_noise / np.max(np.abs(brown_noise))) * 0.2

# 3. חיבור התדרים והרעש
left_channel = wave_left + brown_noise_normalized
right_channel = wave_right + brown_noise_normalized

stereo_signal = np.vstack((left_channel, right_channel)).T
stereo_signal = np.int16((stereo_signal / np.max(np.abs(stereo_signal))) * 32767)

write('alpha_brown.wav', sample_rate, stereo_signal)
print("קובץ אלפא משולב עם רעש חום נוצר!")