# Discord Bot

## 📌 About the Project

This is a Discord bot built using Python and the `discord.py` library. It provides logging, message sending, and account generation functionalities.

## ⚡ Features

- **Logging System**: Logs bot activity and commands.
- **Message Sending**: Sends messages to a Discord channel.
- **Account Generation** (`gen` command):
  - Generates and sends account credentials.
  - Requires users to have the "your\_role" role.
  - Limits requests to a maximum of 10 accounts per command.
  - Reads data from a CSV file.
- **File Operations**:
  - Saves generated accounts to a text file.
  - Removes used accounts from the CSV file.

## 🛠 Installation & Setup

### Prerequisites

Make sure you have Python installed (recommended version: 3.8 or newer) and install the required dependencies:

```bash
pip install discord.py
```

### Configuration

1. **Set Up the Bot Token**:

   - Replace `#add your discord token here` with your actual bot token in the script.

2. **Specify the CSV File Path**:

   - Replace `#path to csv file` with the actual path to the CSV file containing account data.

### Running the Bot

To start the bot, run the following command:

```bash
python bot.py
```

## 🎮 Commands

| Command                   | Description                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------- |
| `!gen <amount> <country>` | Generates a specified number of accounts (max 10) for a given country. Requires the "your_role" role. |

## 📜 License

This project is for educational purposes only. Use responsibly.

## 💡 Notes

- The bot requires **all intents enabled** in the Discord Developer Portal.
- Make sure the bot has proper permissions to send messages and manage roles.
- Handle account generation responsibly and follow Discord’s Terms of Service.

---

**Author:** Neqaative

🚀 Happy coding!

