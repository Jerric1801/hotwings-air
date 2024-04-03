const amqp = require('amqplib');
const config = require('./config');

class Producer {
    channel;
    
    async createChannel() {
        const connection = await amqp.connect(config.rabbitMQ.url);
        this.channel = await connection.createChannel();
    }

    async publishMessage(routingKey, email, notification_type, notification_message) {
        if (!this.channel) {
            await this.createChannel();
        }

        const exchangeName = config.rabbitMQ.exchangeName;
        await this.channel.assertExchange(exchangeName, 'topic', {durable: false});

        const logDetails = {
            email: email,
            notification_type: notification_type,
            notification_message: notification_message,
        }
        
        await this.channel.publish(exchangeName, routingKey,
            Buffer.from(JSON.stringify(logDetails))
        );

        console.log(`The message ${notification_message} is sent to exchange ${exchangeName}`);
    }
}

module.exports = Producer;