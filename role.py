import discord
import asyncio
import random
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

TOKEN = "Your Discord Tokens"
GUILD_ID = 1363040679953170502  # replace with your server ID
ROLE_ID = 1421475734681030677   # replace with your role ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def rainbow_role():
    await client.wait_until_ready()
    guild = client.get_guild(GUILD_ID)
    role = guild.get_role(ROLE_ID)
    print(f"🌈 Started rainbow color changer for role: {role.name}")

    while not client.is_closed():
        color = discord.Color.from_rgb(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        try:
            await role.edit(color=color)
        except Exception as e:
            print(f"Error changing color: {e}")
        await asyncio.sleep(0.1)  # change speed here (0.5s)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    client.loop.create_task(rainbow_role())

client.run(TOKEN)
