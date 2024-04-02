package com.hotwings.user.consumer;

import com.hotwings.user.dto.amqp.CostMessage;
import com.hotwings.user.dto.points.PointsRequest;
import com.hotwings.user.dto.points.PointsResponse;
import com.hotwings.user.services.UserService;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class RabbitMQConsumer {

    private static final Logger LOGGER = LoggerFactory.getLogger(RabbitMQConsumer.class);
    private final UserService userService;

//    @RabbitListener(queues = {"${rabbitmq.cost.queue.name}"})
//    public PointsResponse consume(CostMessage costMessage) {
//        LOGGER.info(String.format("Received message -> %s", costMessage));
//        String email = costMessage.getEmail();
//        int points = costMessage.getLoyalty_points();
//        PointsRequest pointsRequest = new PointsRequest(points);
//        return userService.updateLoyaltyPoints(email, pointsRequest);
//    }
}
