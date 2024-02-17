import yaml
import logging

logger = logging.getLogger(__name__)

async def process_message(message, message_counter):
    try:
        parsed_yaml = yaml.safe_load(message)
        logger.info(f"Processing message {message_counter}...")
        logger.info("Received and processing YAML data:")
        logger.info(parsed_yaml)

        modified_message = f"Processed: {message}"

        logger.info(f"Message {message_counter} processing complete.")
        
        return modified_message
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return None
