# Kafka Demo

This is a simple Kafka demo that illustrates the publish-subscribe model using Python and the Confluent Kafka library. This demo consists of a producer and a consumer that communicate through an Apache Kafka topic.

## Prerequisites

Before running this demo, make sure you have the following prerequisites:

- [Apache Kafka](https://kafka.apache.org/) installed and running.
- Python 3.x installed on your system.
- The `confluent-kafka` library installed. You can install it using pip:

```bash
pip install confluent-kafka
```

## Usage

### Kafka Producer

Run the Kafka producer script using the following command:

```bash
python producer.py
```

This script sends a sample message to the Kafka topic.

### Kafka Consumer

Run the Kafka consumer script using the following command:

```bash
python consumer.py
```

This script listens to the Kafka topic and prints the received messages.

Make sure you have a Kafka broker set up and running on `localhost:9092` or adjust the configurations in the scripts accordingly.

## Configuration

- You can modify the `bootstrap.servers` configuration parameter in both scripts to point to your Kafka broker.
- The default topic used in the demonstration is 'test-topic'. You can change it as per your requirement.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
