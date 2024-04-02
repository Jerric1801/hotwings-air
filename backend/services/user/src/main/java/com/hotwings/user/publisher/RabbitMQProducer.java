package com.hotwings.user.publisher;

import com.hotwings.user.dto.amqp.CostMessage;
import com.hotwings.user.dto.amqp.ErrorMessage;
import com.hotwings.user.dto.amqp.NotificationsMessage;
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

    @Value("${rabbitmq.error.routing.key}")
    private String errorRoutingKey;

    @Value("${rabbitmq.notifications.routing.key}")
    private String notificationsRoutingKey;

    private static final Logger LOGGER = LoggerFactory.getLogger(RabbitMQProducer.class);

    private final RabbitTemplate rabbitTemplate;

    public void sendError(ErrorMessage errorMessage) {
        LOGGER.info(String.format("Message sent -> %s", errorMessage));
        rabbitTemplate.convertAndSend(exchange, errorRoutingKey, errorMessage);
    }

    public void sendNotifications(NotificationsMessage notificationsMessage) {
        LOGGER.info(String.format("Message sent -> %s", notificationsMessage));
        rabbitTemplate.convertAndSend(exchange, notificationsRoutingKey, notificationsMessage);
    }
}
