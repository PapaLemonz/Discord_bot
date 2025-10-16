import discord
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
TOKEN = "Your tokens"
GUILD_ID = 1363040679953170502  # replace with your server ID
USER_ID = 1059091535582462092  # your Discord user ID

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

async def nickname_animation():
    await client.wait_until_ready()
    guild = client.get_guild(GUILD_ID)
    member = guild.get_member(USER_ID)

    if member is None:
        print("❌ Cannot find member. Is the bot in the same server?")
        return

    frames = ["F", "FU", "FUC", "FUCK", "FUCK Y", "FUCK YO", "FUCK YOU", "FUCK YOU!", "FUCK YOU!!"]
    print(f"🎬 Starting nickname animation for {member.display_name}")

    while not client.is_closed():
        for frame in frames:
            try:
                await member.edit(nick=frame)
                await asyncio.sleep(0.25)  # animation speed
            except Exception as e:
                print(f"⚠️ Error changing nickname: {e}")
                await asyncio.sleep(5)
                break  # stop if missing permission

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    client.loop.create_task(nickname_animation())

client.run(TOKEN)
