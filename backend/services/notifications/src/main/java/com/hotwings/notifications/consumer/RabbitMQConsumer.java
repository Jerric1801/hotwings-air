package com.hotwings.notifications.consumer;

import com.hotwings.notifications.dto.NotificationsMessage;
import com.hotwings.notifications.services.NotificationsService;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class RabbitMQConsumer {

    private static final Logger LOGGER = LoggerFactory.getLogger(RabbitMQConsumer.class);
    private final NotificationsService notificationsService;

    @RabbitListener(queues = {"${rabbitmq.queue.name}"})
    public void consumeUser(NotificationsMessage notificationsMessage) {
        LOGGER.info(String.format("Received message -> %s", notificationsMessage));
        notificationsService.sendUserEmail(notificationsMessage);
    }
}
