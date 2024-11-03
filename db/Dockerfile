FROM mysql:latest

ENV MYSQL_DATABASE=medsched_db
ENV MYSQL_USER=medsched_user
ENV MYSQL_PASSWORD=MedSched123!
ENV MYSQL_ROOT_PASSWORD=rootpassword

COPY init.sql /docker-entrypoint-initdb.d/
