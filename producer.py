from confluent_kafka import Producer

def delivery_report(err, msg):
    """
    Callback function that gets triggered when a message is delivered to the Kafka broker.

    Args:
        err (KafkaError): An error object that is None if the message was delivered successfully.
        msg (Message): The message object that was delivered.

    Returns:
        None
    """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_kafka_message(producer, topic, message):
    producer.produce(topic, message, callback=delivery_report)
    producer.poll(0)

if __name__ == '__main__':
    p = Producer({'bootstrap.servers': 'localhost:9092'})

    topic = 'test-topic'
    message = "Hello, Kafka!"

    produce_kafka_message(p, topic, message)

    p.flush(10)
