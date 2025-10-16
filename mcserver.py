import discord
import asyncio
from mcstatus import JavaServer
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

token = "Your Discord Tokens"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def update_status():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            # Hypixel server address
            server = JavaServer.lookup("mc.zahar.my")
            status = server.status()
            player_count = status.players.online

            # Set the bot’s status
            await client.change_presence(
                activity=discord.Game(f"🎮 Zahar: {player_count}/100 online")
            )
        except Exception as e:
            print(f"Error updating status: {e}")

        # Wait 60 seconds before checking again
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    client.loop.create_task(update_status())

client.run(token)
