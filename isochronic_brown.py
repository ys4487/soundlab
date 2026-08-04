import numpy as np
from scipy.io.wavfile import write
from scipy.signal import lfilter

sample_rate = 44100
duration = 1800

t = np.linspace(0, duration, int(sample_rate * duration), False)

# 1. יצירת הטון האיזוכרוני (נדלק ונכבה)
base_freq = 200.0
beat_freq = 10.0
base_wave = np.sin(2 * np.pi * base_freq * t)
envelope = np.sin(2 * np.pi * beat_freq * t)**2
isochronic_wave = base_wave * envelope * 0.4

# 2. ייצור רעש חום
white_noise = np.random.normal(0, 1, sample_rate * duration)
brown_noise = lfilter([1], [1, -0.98], white_noise)
brown_noise -= np.mean(brown_noise)
brown_noise_normalized = (brown_noise / np.max(np.abs(brown_noise))) * 0.2

# 3. חיבור (הגל האיזוכרוני משוכפל אותו דבר לימין ולשמאל)
combined_channel = isochronic_wave + brown_noise_normalized
stereo_signal = np.vstack((combined_channel, combined_channel)).T
stereo_signal = np.int16((stereo_signal / np.max(np.abs(stereo_signal))) * 32767)

write('isochronic_brown.wav', sample_rate, stereo_signal)
print("קובץ איזוכרוני (ללא צורך באוזניות) משולב עם רעש חום נוצר!")