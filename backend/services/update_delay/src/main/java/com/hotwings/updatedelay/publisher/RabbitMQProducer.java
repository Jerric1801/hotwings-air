package com.hotwings.updatedelay.publisher;

import com.hotwings.updatedelay.dto.FlightMessage;
import com.hotwings.updatedelay.dto.NotificationsMessage;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class RabbitMQProducer {

    @Value("${rabbitmq.exchange.name}")
    private String exchange;

    @Value("${rabbitmq.notifications.routing.key}")
    private String notificationsRoutingKey;

    @Value("${rabbitmq.tracker.routing.key}")
    private String trackerRoutingKey;

    private static final Logger LOGGER = LoggerFactory.getLogger(RabbitMQProducer.class);

    private final RabbitTemplate rabbitTemplate;

    public void sendNotifications(NotificationsMessage notificationsMessage) {
        LOGGER.info(String.format("Message sent -> %s", notificationsMessage));
        rabbitTemplate.convertAndSend(exchange, notificationsRoutingKey, notificationsMessage);
    }

    public void sendTracker(FlightMessage flightMessage) {
        LOGGER.info(String.format("Message sent -> %s", flightMessage));
        rabbitTemplate.convertAndSend(exchange, trackerRoutingKey, flightMessage);
    }
}
