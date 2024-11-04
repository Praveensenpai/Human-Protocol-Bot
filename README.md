# Human Protocol Telegram Bot Automation

Automate your interactions with the Human Protocol Telegram Bot! This script is designed to handle daily claims, ensuring you never miss out on your rewards. Currently, the bot supports daily claims every 6 hours, with more features coming soon.

## Features

- **Daily Claim Automation**: Automatically claims rewards every 6 hours.
- **Easy Configuration**: Set your environment variables easily.
- **Cross-Platform Support**: Works on both Linux and Windows.

## Installation

Before running the script, ensure you have the necessary dependencies installed.

### Step 1: Install `uv`

#### For Linux

Run the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### For Windows

Run this command in PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/Praveensenpai/humanprotocolbot
cd humanprotocolbot
```

### Step 3: Install Required Packages

```bash
uv sync
```

## Configuration

You'll need to set the following environment variables for the bot to work correctly:

- `REF_ID`: Your reference ID.
- `SESSION_NAME`: The name of your session.
- `API_ID`: Your Telegram API ID.
- `API_HASH`: Your Telegram API hash.
- `PHONE`: Your phone number associated with the Telegram account.

## Usage

Run the bot with the following command:

```bash
uv run main.py
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [httpx](https://www.python-httpx.org/) for making HTTP requests easy.
- [Pyrogram](https://pyrogram.org/) for providing a great interface for the Telegram API.
- [Loguru](https://loguru.readthedocs.io/en/stable/) for easy logging.
