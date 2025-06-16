# Telegram Bot Secretary

This project is a Telegram bot designed to manage incoming letters and generate responses. It utilizes various Python libraries to handle file processing, database management, and interaction with the Telegram API.

## Project Structure

```
telegram_bot_secretary/
├── bot.py                  # Main bot logic and command handlers
├── config.py               # Configuration constants (authorized users and database path)
├── database.py             # Database operations (initialization, saving, and retrieving letters)
├── document_parser.py      # Functions for extracting text from PDF and image files
├── excel_exporter.py       # Function to export inbox data to an Excel file
├── letter_numbering.py     # Function to generate the next letter number
├── response_generator.py    # Function to generate response messages based on letter data
├── requirements.txt        # List of project dependencies
├── data                    # Directory for storing the SQLite database
│   └── db.sqlite3         # SQLite database file for storing inbox data
└── README.md               # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. Update the `config.py` file with your authorized Telegram user IDs.
2. Run the bot using:

```
python bot.py
```

3. Use the `/start` command in Telegram to initiate interaction with the bot.

## Features

- **File Processing**: The bot can handle incoming PDF and image files, extracting relevant information such as company names, sender names, emails, and subjects.
- **Database Management**: All incoming letters are stored in an SQLite database, allowing for easy retrieval and management.
- **Response Generation**: The bot can generate formatted response messages based on the letters received.
- **Excel Export**: The contents of the inbox can be exported to an Excel file for further analysis.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.