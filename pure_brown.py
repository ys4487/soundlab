import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter

sample_rate = 44100
duration = 1800  # שנה ל-900 עבור 15 דקות של רעש חום רציף

# ייצור רעש לבן והמרתו לרעש חום (חיתוך תדרים צורמים)
white_noise = np.random.normal(0, 1, sample_rate * duration)
brown_noise = lfilter([1], [1, -0.98], white_noise)
brown_noise -= np.mean(brown_noise)
brown_noise_normalized = np.int16((brown_noise / np.max(np.abs(brown_noise))) * 32767)

# שכפול לשני הערוצים (סטריאו)
stereo_signal = np.vstack((brown_noise_normalized, brown_noise_normalized)).T

write('pure_brown.wav', sample_rate, stereo_signal)
print("קובץ רעש חום טהור נוצר בהצלחה!")