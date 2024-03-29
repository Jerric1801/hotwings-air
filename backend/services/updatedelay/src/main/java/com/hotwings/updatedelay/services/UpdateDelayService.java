package com.hotwings.updatedelay.services;

import com.hotwings.updatedelay.dto.FlightMessage;
import com.hotwings.updatedelay.dto.NotificationsMessage;
import com.hotwings.updatedelay.models.User;
import com.hotwings.updatedelay.publisher.RabbitMQProducer;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class UpdateDelayService {

    private final WebClient webClient;
    private final RabbitMQProducer producer;

    public void getAffectedUsers(FlightMessage flightMessage) {
        String date = flightMessage.getDate();
        String flight_id = flightMessage.getFlight_id();
        List<User> affectedUsers = webClient.post()
                .uri("http://localhost:8080/user/disruption")
                .contentType(MediaType.APPLICATION_JSON)
                .bodyValue(flightMessage)
                .retrieve()
                .bodyToMono(new ParameterizedTypeReference<List<User>>() {})
                .block();
        if (affectedUsers != null) {
            for (User u : affectedUsers) {
                String email = u.getEmail();
                String msg_body = "We are sorry to inform you that your flight " + flight_id + " on " + date + "has been delayed. You will receive an email with steps on what to do next.";
                NotificationsMessage msg = new NotificationsMessage(email, "Flight Delay", msg_body);
                producer.sendNotifications(msg);
            }
        }
    }

}
