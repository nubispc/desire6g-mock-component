import os
import asyncio
from aio_pika import connect, IncomingMessage, Message
from ProcessingSystems.processor_base import process_message, logger

# RabbitMQ connection parameters
rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
input_topic = os.getenv("INPUT_TOPIC", "input_topic")
output_topic = os.getenv("OUTPUT_TOPIC", "output_topic")

async def main_loop():
    message_counter = 0

    # Connect to RabbitMQ
    connection = await connect(f"amqp://{rabbitmq_host}/")
    channel = await connection.channel()

    # Declare queues and get the default exchange
    input_queue = await channel.declare_queue(input_topic)
    output_queue = await channel.declare_queue(output_topic)
    default_exchange = channel.default_exchange

    async def on_message(message: IncomingMessage):
        nonlocal message_counter
        message_counter += 1
        modified_message = await process_message(message.body, message_counter)
        if modified_message:
            await default_exchange.publish(
                Message(modified_message.encode()),
                routing_key=output_topic
            )
            logger.info(f"Processed message {message_counter}: {message.body.decode()}")

    await input_queue.consume(on_message)
    logger.info("Waiting for messages to process. To exit, press CTRL+C")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_loop())
