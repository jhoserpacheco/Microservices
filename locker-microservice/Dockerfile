FROM openjdk:17-alpine
COPY "./target/service-loker.jar" "app.jar"
EXPOSE 9525
ENTRYPOINT ["java", "-jar", "app.jar"]