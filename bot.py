import os
import discord
import ollama
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", "!ask")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
ollama_client = ollama.Client(host=OLLAMA_HOST)


def split_response(text: str, limit: int = 1900) -> list[str]:
    """Split text into chunks that fit within Discord's message limit."""
    if len(text) <= limit:
        return [text]
    chunks = []
    while text:
        chunk = text[:limit]
        last_newline = chunk.rfind("\n")
        if last_newline > limit // 2:
            chunk = text[:last_newline]
        chunks.append(chunk)
        text = text[len(chunk):]
    return chunks


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print(f"Model: {OLLAMA_MODEL} | Host: {OLLAMA_HOST}")
    print(f"Prefix: '{PREFIX}' | Mention: @{client.user.name}")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    content = message.content.strip()
    prompt = None

    # Check for prefix
    if content.lower().startswith(PREFIX.lower()):
        prompt = content[len(PREFIX):].strip()

    # Check for @mention
    elif client.user in message.mentions:
        prompt = content.replace(f"<@{client.user.id}>", "").strip()

    if not prompt:
        return

    async with message.channel.typing():
        try:
            response = ollama_client.chat(
                model=OLLAMA_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            reply = response.message.content
        except Exception as e:
            reply = f"Error contacting Ollama: {e}"

    for chunk in split_response(reply):
        await message.reply(chunk)


client.run(TOKEN)
