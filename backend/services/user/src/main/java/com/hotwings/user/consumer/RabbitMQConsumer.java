package com.hotwings.user.consumer;

import com.hotwings.user.dto.amqp.CostMessage;
import com.hotwings.user.dto.amqp.NotificationsMessage;
import com.hotwings.user.dto.points.PointsRequest;
import com.hotwings.user.dto.points.PointsResponse;
import com.hotwings.user.models.User;
import com.hotwings.user.publisher.RabbitMQProducer;
import com.hotwings.user.repository.UserRepository;
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
    private final RabbitMQProducer producer;
    private final UserRepository userRepository;

   @RabbitListener(queues = {"${rabbitmq.cost.queue.name}"})
   public void consume(CostMessage costMessage) {
       LOGGER.info(String.format("Received message -> %s", costMessage));
       String email = costMessage.getEmail();
       int points = costMessage.getLoyalty_points();
       User user = userRepository.findOneByEmail(email).orElse(null);
       if (user != null){
           int currentPoints = user.getLoyalty_points();
           int newPoints = currentPoints + points;
           user.setLoyalty_points(newPoints);
           userRepository.save(user);
           String lpMsg = "Your new loyalty points are " + newPoints;
           NotificationsMessage nm = new NotificationsMessage(email, "Loyalty Points", lpMsg);
           producer.sendNotifications(nm);
       }
   }
}
