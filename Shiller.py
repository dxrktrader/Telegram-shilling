import random
import time
import os
from telethon import TelegramClient
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Get API credentials from environment variables
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

# Create Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# List of messages to send
messages = [
    "Lets fly baby",
    "Nothing to worry about chads",
    "Believe in something",
    "Lets get this money",
    "We looking good honey"
]

# List of chat usernames or IDs where messages will be sent
chat_list = ['chat_username1', 'chat_username2']  # Replace with actual usernames or chat IDs

# Set daily message limit
DAILY_MESSAGE_LIMIT = 5  # Number of messages allowed per day
message_count = 0  # Counter for the number of messages sent
reset_time = datetime.now() + timedelta(days=1)  # Time to reset the daily counter

# Function to send random messages with a daily limit
async def send_random_messages():
    global message_count, reset_time

    while True:
        # Check if the daily message limit has been reached
        if message_count >= DAILY_MESSAGE_LIMIT:
            print(f"Daily message limit of {DAILY_MESSAGE_LIMIT} reached. Waiting until reset.")
            # Wait until the reset time
            sleep_time = (reset_time - datetime.now()).total_seconds()
            time.sleep(sleep_time)

            # Reset the counter and set the next reset time
            message_count = 0
            reset_time = datetime.now() + timedelta(days=1)

        try:
            # Pick a random chat and a random message
            chat = random.choice(chat_list)
            message = random.choice(messages)

            # Send the message
            await client.send_message(chat, message)
            message_count += 1  # Increment the message counter
            print(f"Message sent to {chat}: {message} (Message {message_count}/{DAILY_MESSAGE_LIMIT})")

            # Wait for a random interval (e.g., 1 to 3 hours)
            wait_time = random.randint(3600, 10800)  # Random time in seconds (1 to 3 hours)
            print(f"Waiting for {wait_time // 3600} hours before the next message...")
            time.sleep(wait_time)

        except Exception as e:
            print(f"An error occurred: {e}")
            # Wait a bit before retrying in case of an error
            time.sleep(60)

# Start the client and run the loop
with client:
    client.loop.run_until_complete(send_random_messages())