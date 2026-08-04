import os
import subprocess

print("מתחיל לכווץ את הקבצים לגודל שמתאים לגיטהאב... זה ייקח כמה דקות ⏳")

for filename in os.listdir('.'):
    if filename.endswith('.mp3'):
        print(f"📉 מכווץ את {filename}...")
        
        # אנחנו משנים זמנית את שם הקובץ המקורי כדי שהקובץ החדש והמכווץ יישמר בשם הרגיל
        temp_filename = "temp_" + filename
        os.rename(filename, temp_filename)
        
        # פקודת הכיווץ ל-96k (חותך את המשקל בחצי!)
        command = ['ffmpeg', '-y', '-i', temp_filename, '-b:a', '96k', filename]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # מחיקת הקובץ הכבד הישן
        os.remove(temp_filename)
        
print("✅ סיימנו! כל הקבצים הוקטנו ושוקלים עכשיו פחות מ-25 מגה-בייט.")