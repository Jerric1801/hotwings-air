FROM openjdk:21-jdk
EXPOSE 5009 8000
WORKDIR /app
COPY target/update_delay.jar /app/update_delay.jar
ENTRYPOINT ["java", \
            "-Xdebug", \
            "-Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=*:8000", \
            "-jar", "update_delay.jar"] 