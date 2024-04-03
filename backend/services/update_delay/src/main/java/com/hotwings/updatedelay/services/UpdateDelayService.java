package com.hotwings.updatedelay.services;

import com.hotwings.updatedelay.dto.FlightMessage;
import com.hotwings.updatedelay.dto.ItineraryMessage;
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
        String departure = flightMessage.getDeparture();
        String flight_number = flightMessage.getFlight_number();
        List<User> affectedUsers = webClient.post()
                .uri("http://host.docker.internal:5003/user/disruption")
                .contentType(MediaType.APPLICATION_JSON)
                .bodyValue(flightMessage)
                .retrieve()
                .bodyToMono(new ParameterizedTypeReference<List<User>>() {})
                .block();
        if (affectedUsers != null) {
            for (User u : affectedUsers) {
                String email = u.getEmail();
                String msg_body = "We are sorry to inform you that your flight " + flight_number + " on " + departure + "has been delayed. You will receive an email with steps on what to do next.";
                NotificationsMessage msg = new NotificationsMessage(email, "Flight Delay", msg_body);
                producer.sendNotifications(msg);
            }

            createItinerary(flightMessage, affectedUsers);
        }
    }

    public void createItinerary(FlightMessage flightMessage, List<User> affectedUsers) {
        ItineraryMessage iti = new ItineraryMessage(affectedUsers, flightMessage.getFlight_id(), flightMessage.getDeparture(), flightMessage.getFlight_number());
         webClient.post()
            .uri("http://host.docker.internal:5010/create_itinerary")
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(iti)
            .retrieve()
            .bodyToMono(ItineraryMessage.class)
            .block();
    }

}
