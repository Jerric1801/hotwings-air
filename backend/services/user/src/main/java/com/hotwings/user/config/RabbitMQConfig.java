package com.hotwings.user.config;

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

    //    Error Queue
    @Value("${rabbitmq.error.queue.name}")
    private String errorQueue;
    @Value("${rabbitmq.error.routing.key}")
    private String errorRoutingKey;

    //    Notifications Queue
    @Value("${rabbitmq.notifications.queue.name}")
    private String notificationsQueue;
    @Value("${rabbitmq.notifications.routing.key}")
    private String notificationsRoutingKey;

    //    Cost Analysis Queue
    @Value("${rabbitmq.cost.queue.name}")
    private String costQueue;
    @Value("${rabbitmq.cost.routing.key}")
    private String costRoutingKey;

    @Bean
    public TopicExchange exchange() {
        return new TopicExchange(exchange, false, false);
    }

    @Bean
    public Queue errorQueue() {
        return new Queue(errorQueue, true);
    }

    @Bean
    public Queue notificationsQueue() {
        return new Queue(notificationsQueue, true);
    }

    @Bean
    public Queue costQueue() {
        return new Queue(costQueue, true);
    }

    @Bean
    public Binding errorBinding() {
        return BindingBuilder.bind(errorQueue())
                .to(exchange())
                .with(errorRoutingKey);
    }

    @Bean
    public Binding notificationsBinding() {
        return BindingBuilder.bind(notificationsQueue())
                .to(exchange())
                .with(notificationsRoutingKey);
    }

    @Bean
    public Binding costBinding() {
        return BindingBuilder.bind(costQueue())
                .to(exchange())
                .with(costRoutingKey);
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
