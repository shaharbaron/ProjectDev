# שימוש בתמונה בסיסית של Nginx
FROM nginx:alpine

# העתקת קבצי ה-HTML לתוך תיקיית ברירת המחדל של Nginx
COPY . /usr/share/nginx/html

# הפקודה להריץ את Nginx (היא מובנית בתמונה)
CMD ["nginx", "-g", "daemon off;"]
