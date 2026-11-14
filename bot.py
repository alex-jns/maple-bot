import os
from pathlib import Path
from dotenv import load_dotenv
import getpass
import discord
from discord import app_commands

# Use Discord's standard set of events
# These are enough to connect the bot without reading message contents
intents = discord.Intents.default()

class MapleClient(discord.Client):
    async def setup_hook(self):
        # Register our slash commands with Discord when the bot starts.
        await tree.sync()

# Create our client using the startup behavior defined above.
client = MapleClient(intents=intents)

# A command tree holds the slash commands available through this bot.
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    # Discord.py calls this function when the bot is connected and ready
    print(f"Connected as {client.user}!")


# Find the .env file beside this Python file.
env_path = Path(__file__).resolve().parent / ".env"

# Load its settings into this program's environment variables
load_dotenv(env_path)

# Read the token using the same name we used in .env
token = os.getenv("DISCORD_TOKEN")

# Stop with a helpful message if the token is missing or empty
if not token:
    raise ValueError("DISCORD_TOKEN is missing. Check your .env file.")

@tree.command(name="hello", description="Say hello to the bot.")
async def hello(interaction: discord.Interaction):
    # An interaction represents someone using our slash command.
    # Respond in the channel where they used it.
    await interaction.response.send_message("Hello, world!")

# Log in and keep the bot running until we stop the program
client.run(token)