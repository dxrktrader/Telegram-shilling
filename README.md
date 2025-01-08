# Telegram Shilling Bot

A simple Telegram shilling bot that sends random messages to a list of group chats or channels at random intervals. This bot is designed for educational purposes to demonstrate automation using a Telegram account (not a bot). It uses the [Telethon](https://github.com/LonamiWebs/Telethon) library for interacting with Telegram.

## Features
- Sends random messages from a predefined list.
- Sends messages to a list of groups or channels.
- Implements a daily message limit to prevent spamming.
- Messages are sent at random intervals (between 1 and 3 hours).

## Prerequisites
Before running the bot, you need:
- A **Telegram account** (not a bot).
- **Python 3** installed on your system.
- A **Telegram API ID** and **API Hash**.

## Installation

1. **Clone the Repository**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/yourusername/telegram-shilling-bot.git
     ```

2. **Navigate to Project Directory**
   - Go to the project folder:
     ```bash
     cd telegram-shilling-bot
     ```

3. **Install Dependencies**
   - Install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```
   - If you don’t have `requirements.txt`, run:
     ```bash
     pip install telethon python-dotenv
     ```

4. **Get Telegram API Credentials**
   - Go to [Telegram API Development Tools](https://my.telegram.org/auth) and log in.
   - Create a new application and get your **API ID** and **API Hash**.
   - Add these credentials to a `.env` file in the root of the project:
     ```env
     TELEGRAM_API_ID=your_api_id
     TELEGRAM_API_HASH=your_api_hash
     ```

5. **Create a `.gitignore` File** (Optional but recommended)
   - Add `.env` to your `.gitignore` to avoid uploading sensitive information:
     ```
     .env
     __pycache__/
     *.pyc
     *.pyo
     ```

6. **Set Up Chat List**
   - Update the `chat_list` variable in the `shilling_bot.py` file with the usernames or IDs of the Telegram groups or channels you want the bot to send messages to:
     ```python
     chat_list = ['@mygroupname', -1001234567890]
     ```

7. **Set Up Daily Limit**
   - Optionally, set a daily message limit by modifying the `DAILY_MESSAGE_LIMIT` variable in the script:
     ```python
     DAILY_MESSAGE_LIMIT = 10  # Change this number to control the limit
     ```

---

## Running the Bot

1. **Run the Bot Script**
   - Open a terminal and navigate to the project directory.
   - Run the Python script:
     ```bash
     python3 shilling_bot.py
     ```

2. **Login to Telegram Account**
   - On the first run, the script will ask you to log in with your phone number.
   - You’ll receive a verification code in your Telegram app.

3. **Monitor the Bot**
   - The bot will begin sending messages to the specified chat(s) at random intervals.
   - It will respect the daily message limit.

---

## Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit them (`git commit -m 'Add new feature'`).
4. Push your changes (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---

## Disclaimer

- **Educational Use Only**: This project is for learning purposes and should not be used to spam or violate Telegram's terms of service.
- **Use Responsibly**: Automating a Telegram account (not a bot) can result in restrictions or bans if abused.

---

