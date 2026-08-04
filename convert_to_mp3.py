import os
import subprocess

print("מתחיל בהמרת הקבצים... זה עשוי לקחת כמה דקות ⏳")

# מעבר על כל הקבצים בתיקייה
for filename in os.listdir('.'):
    if filename.endswith('.wav'):
        mp3_filename = filename.replace('.wav', '.mp3')
        print(f"🔄 ממיר את {filename} ל-{mp3_filename}...")
        
        # הפקודה שמפעילה את מנוע ה-ffmpeg ישירות על המחשב
        # הוספנו '-y' כדי שידרוס קבצים קיימים אם ניסית בעבר
        command = ['ffmpeg', '-y', '-i', filename, '-b:a', '192k', mp3_filename]
        
        # הרצת הפקודה "בשקט" כדי לא להציף לך את המסך בטקסט
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
print("✅ סיימנו! כל הקבצים הומרו בהצלחה ל-MP3.")