import discord
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Enable message intents
token = "Your Discord Tokens"
intents = discord.Intents.default()
intents.message_content = True

# Create the client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot is online as {client.user}")

# Run the bot
client.run(token)
