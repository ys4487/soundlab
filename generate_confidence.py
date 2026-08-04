import numpy as np
from scipy.io.wavfile import write

duration_minutes = 30
sample_rate = 44100
duration_seconds = duration_minutes * 60

base_freq = 432.0  # תדר בסיס מרגיע והרמוני
beat_freq = 12.0   # תדר 12 הרץ - ערנות רגועה וביטחון עצמי

left_freq = base_freq - (beat_freq / 2)
right_freq = base_freq + (beat_freq / 2)

t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)
left_wave = np.sin(2 * np.pi * left_freq * t)
right_wave = np.sin(2 * np.pi * right_freq * t)

noise = np.random.normal(0, 0.1, len(t))

left_channel = (left_wave * 0.6) + (noise * 0.4)
right_channel = (right_wave * 0.6) + (noise * 0.4)

stereo_signal = np.vstack((left_channel, right_channel)).T
stereo_signal = np.int16(stereo_signal * 32767)

write("confidence_432hz.wav", sample_rate, stereo_signal)
print("✅ נוצר קובץ ה-WAV לביטחון עצמי!")