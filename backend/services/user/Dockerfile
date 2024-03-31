FROM openjdk:21-jdk
WORKDIR /app
COPY target/user-0.0.1-SNAPSHOT.jar /app/user-0.0.1-SNAPSHOT.jar
EXPOSE 5003 
ENTRYPOINT ["java", "-jar", "user-0.0.1-SNAPSHOT.jar"]