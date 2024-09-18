# שימוש בתמונה בסיסית של Python
FROM python:3.9

# התקנת ספריות ותלויות גרפיות (xvfb)
RUN apt-get update && apt-get install -y \
    python3-pygame \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קבצי הפרויקט לתוך הקונטיינר
COPY . /app

# התקנת כל התלויות הנוספות (כגון Pygame)
RUN pip install pygame

# הפקודה שמריצה את Pygame באמצעות Xvfb (המשמש ליצירת מסך וירטואלי)
CMD ["xvfb-run", "python", "tetris.py"]
