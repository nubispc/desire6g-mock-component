import os
from ProcessingSystems import processor_rabbitmq, processor_kafka

# Get the messaging system from environment variable
messaging_system = os.getenv("MESSAGING_SYSTEM", "rabbitmq")

if messaging_system.lower() == "rabbitmq":
    processor_rabbitmq.main_loop()
elif messaging_system.lower() == "kafka":
    processor_kafka.main_loop()
else:
    raise ValueError("Invalid messaging system. Please specify either 'rabbitmq' or 'kafka'.")
