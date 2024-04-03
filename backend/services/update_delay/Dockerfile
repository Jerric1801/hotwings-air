FROM openjdk:21-jdk
EXPOSE 5009
WORKDIR /app
COPY target/update_delay.jar /app/update_delay.jar
ENTRYPOINT ["java", \
            "-Xdebug", \
            "-jar", "update_delay.jar"] 