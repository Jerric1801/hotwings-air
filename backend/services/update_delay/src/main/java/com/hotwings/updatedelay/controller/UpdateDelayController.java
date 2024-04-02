package com.hotwings.updatedelay.controller;

import com.hotwings.updatedelay.dto.FlightMessage;
import com.hotwings.updatedelay.dto.NotificationsMessage;
import com.hotwings.updatedelay.publisher.RabbitMQProducer;
import com.hotwings.updatedelay.services.UpdateDelayService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/updatedelay")
@RequiredArgsConstructor
@CrossOrigin
public class UpdateDelayController {

    private final UpdateDelayService updateDelayService;
    private final RabbitMQProducer producer;


    @PostMapping("/notifications")
    @ResponseStatus(HttpStatus.OK)
    public ResponseEntity<String> sendNotifications(@RequestBody NotificationsMessage notificationsMessage) {
        producer.sendNotifications(notificationsMessage);
        return ResponseEntity.ok("Message sent to RabbitMQ ...");
    }

    @PostMapping("/tracker")
    @ResponseStatus(HttpStatus.OK)
    public ResponseEntity<String> sendTracker(@RequestBody FlightMessage flightMessage) {
        producer.sendTracker(flightMessage);
        return ResponseEntity.ok("Message sent to RabbitMQ ...");
    }
}
