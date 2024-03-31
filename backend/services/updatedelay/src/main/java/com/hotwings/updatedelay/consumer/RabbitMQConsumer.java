package com.hotwings.updatedelay.consumer;

import com.hotwings.updatedelay.dto.FlightMessage;
import com.hotwings.updatedelay.services.UpdateDelayService;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class RabbitMQConsumer {

    private static final Logger LOGGER = LoggerFactory.getLogger(RabbitMQConsumer.class);
    private final UpdateDelayService updateDelayService;

    @RabbitListener(queues = {"${rabbitmq.tracker.queue.name}"})
    public void consume(FlightMessage flightMessage) {
        LOGGER.info(String.format("Received message -> %s", flightMessage));
        updateDelayService.getAffectedUsers(flightMessage);
    }
}
