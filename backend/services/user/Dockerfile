FROM openjdk:21-jdk
EXPOSE 8080
WORKDIR /app
COPY target/user.jar /app/user.jar
ENTRYPOINT ["java", "-jar", "user.jar"]