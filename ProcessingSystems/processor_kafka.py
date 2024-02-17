import os
from kafka import KafkaConsumer, KafkaProducer
from ProcessingSystems.processor_base import process_message, logger

# Kafka connection parameters
kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
input_topic = os.getenv("INPUT_TOPIC", "input_topic")
output_topic = os.getenv("OUTPUT_TOPIC", "output_topic")

def main_loop():
    # Create Kafka consumer and producer
    consumer = KafkaConsumer(input_topic, bootstrap_servers=kafka_bootstrap_servers)
    producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

    # Process incoming messages
    message_counter = 0
    for message in consumer:
        message_counter += 1
        processed_message = process_message(message.value.decode(), message_counter)
        if processed_message:
            producer.send(output_topic, processed_message.encode())
            logger.info(f"Processed message {message_counter}: {message.value.decode()}")

if __name__ == "__main__":
    main_loop()
