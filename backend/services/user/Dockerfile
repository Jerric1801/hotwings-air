FROM openjdk:21-jdk
EXPOSE 5003 
WORKDIR /app
COPY target/user.jar /app/user.jar
ENTRYPOINT ["java", \
            "-Xdebug", \
            "-jar", "user.jar"] 