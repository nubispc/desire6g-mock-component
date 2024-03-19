# ProcessingSystems/messaging.py
import yaml
import logging
import asyncio
from aio_pika import IncomingMessage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_message(message: IncomingMessage):
    try:
        parsed_yaml = yaml.safe_load(message.body)
        logger.info("Processing message...")
        logger.info("Received and processing YAML data:")
        logger.info(parsed_yaml)

        modified_message = f"Processed: {message.body.decode()}"

        logger.info("Message processing complete.")
        return modified_message
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return None
