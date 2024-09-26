FROM nginx:latest 
# מוחק את הקובץ הדיפולטי של nginx שלא יתנגש עם הקבצים שלי
RUN rm -rf /usr/share/nginx/html/index.html
# מעתיק את כל הקבצים שנמצאים בתיקיה שנמצא הקובץ דוקר אל התיקיה המצוינת
COPY . /usr/share/nginx/html/index.html/
# פותח את פורט 80 כדי שניתן יהיה לגשת לאפליקציה דרך הדפדפן
EXPOSE 80
# מוודא ש-nginx ירוץ במצב פעיל (ולא רק כרקע) בתוך הקונטיינר
CMD ["nginx", "-g", "daemon off;"]

# FROM node:16.14
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# CMD [ "npm", "start" ]

