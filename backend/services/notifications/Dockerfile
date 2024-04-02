FROM openjdk:21-jdk
EXPOSE 5007 8000
WORKDIR /app
COPY target/notifications.jar /app/notifications.jar
ENTRYPOINT ["java", \
            "-Xdebug", \
            "-Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=*:8000", \
            "-jar", "notifications.jar"] 