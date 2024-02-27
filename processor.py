import os
import asyncio
from ProcessingSystems import processor_rabbitmq, processor_kafka

# Get the messaging system from environment variable
messaging_system = os.getenv("MESSAGING_SYSTEM", "rabbitmq")

if messaging_system.lower() == "rabbitmq":
    asyncio.run(processor_rabbitmq.main_loop())  # Await the main_loop coroutine
elif messaging_system.lower() == "kafka":
    asyncio.run(processor_kafka.main_loop())  # Await the main_loop coroutine
else:
    raise ValueError("Invalid messaging system. Please specify either 'rabbitmq' or 'kafka'.")
