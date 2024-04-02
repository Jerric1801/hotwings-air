FROM openjdk:21-jdk
EXPOSE 5003 8000
WORKDIR /app
COPY target/user.jar /app/user.jar
ENTRYPOINT ["java", \
            "-Xdebug", \
            "-Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=*:8000", \
            "-jar", "user.jar"] 