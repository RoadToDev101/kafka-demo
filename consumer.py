from confluent_kafka import Consumer, KafkaError

def consume_kafka_message(consumer, topic):
    """
    Consume messages from a Kafka topic using a Kafka consumer.

    Args:
        consumer (kafka.KafkaConsumer): The Kafka consumer to use for consuming messages.
        topic (str): The name of the Kafka topic to consume messages from.
    """
    running = True
    try:
        consumer.subscribe([topic])

        while running:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    c = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })

    topic = 'test-topic'

    consume_kafka_message(c, topic)
