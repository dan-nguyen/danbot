# danbot

A Discord bot that uses [Ollama](https://ollama.com) to run local LLMs. Responds to a configurable prefix command or direct @mentions.

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) running locally (or on a reachable host)
- A Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))

## Setup

1. **Clone the repo and create a virtual environment:**

   ```bash
   git clone https://github.com/dan-nguyen/danbot.git
   cd danbot
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your values:

   | Variable | Required | Default | Description |
   |---|---|---|---|
   | `DISCORD_TOKEN` | Yes | — | Your Discord bot token |
   | `OLLAMA_MODEL` | No | `llama3.2` | Ollama model to use |
   | `OLLAMA_HOST` | No | `http://localhost:11434` | Ollama API host |
   | `PREFIX` | No | `!ask` | Command prefix |

3. **Pull your Ollama model** (if you haven't already):

   ```bash
   ollama pull llama3.2
   ```

4. **Run the bot:**

   ```bash
   python bot.py
   ```

## Discord Bot Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2. Under **Bot**, enable the **Message Content Intent**.
3. Under **OAuth2 → URL Generator**, select the `bot` scope and the `Send Messages` and `Read Message History` permissions. Use the generated URL to invite the bot to your server.

## Usage

- `!ask <prompt>` — send a prompt using the configured prefix
- `@danbot <prompt>` — mention the bot directly

## License

MIT
