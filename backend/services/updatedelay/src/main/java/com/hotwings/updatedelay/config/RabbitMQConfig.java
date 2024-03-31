package com.hotwings.updatedelay.config;

import org.springframework.amqp.core.*;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitMQConfig {

    @Value("${rabbitmq.exchange.name}")
    private String exchange;

    //    Flight Tracker Queue
    @Value("${rabbitmq.tracker.queue.name}")
    private String trackerQueue;
    @Value("${rabbitmq.tracker.routing.key}")
    private String trackerRoutingKey;

    //    Notifications Queue
    @Value("${rabbitmq.notifications.queue.name}")
    private String notificationsQueue;
    @Value("${rabbitmq.notifications.routing.key}")
    private String notificationsRoutingKey;

    @Bean
    public TopicExchange exchange() {
        return new TopicExchange(exchange);
    }

    @Bean
    public Queue trackerQueue() {
        return new Queue(trackerQueue, true);
    }

    @Bean
    public Queue notificationsQueue() {
        return new Queue(notificationsQueue, true);
    }

    @Bean
    public Binding trackerBinding() {
        return BindingBuilder.bind(trackerQueue())
                .to(exchange())
                .with(trackerRoutingKey);
    }

    @Bean
    public Binding notificationsBinding() {
        return BindingBuilder.bind(notificationsQueue())
                .to(exchange())
                .with(notificationsRoutingKey);
    }

    @Bean
    public Jackson2JsonMessageConverter converter() {
        return new Jackson2JsonMessageConverter();
    }

    @Bean
    public AmqpTemplate template(ConnectionFactory connectionFactory) {
        final RabbitTemplate rabbitTemplate = new RabbitTemplate(connectionFactory);
        rabbitTemplate.setMessageConverter(converter());
        return rabbitTemplate;
    }
}
