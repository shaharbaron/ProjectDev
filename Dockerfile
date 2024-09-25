FROM nginx:latest 
RUN rm -rf /usr/share/nginx/html/index.html
# מעתיק את כל הקבצים שנמצאים בתיקיה שנמצא הקובץ דוקר אל התיקיה המצוינת
COPY . /usr/share/nginx/html/index.html/
#שיהיה ניתן לגשת דרך פורט 80 מבחוץ
EXPOSE 80
# מבטיחה שהשרת ישאר פעיל בקונטיינר ולא ירוץ כרקע
CMD ["nginx", "-g", "daemon off;"]
