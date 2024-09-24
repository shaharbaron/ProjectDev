FROM nginx:latest 
RUN rm -rf /usr/share/nginx/html/index.html
COPY . /usr/share/nginx/html/index.html/
RUN chmod -R 755 /usr/share/nginx/html
RUN chown -R 101:101 /usr/share/nginx/html 
# try without
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
