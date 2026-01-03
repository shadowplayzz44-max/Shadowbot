import discord
from discord import app_commands
import json
import os

with open("config.json","r") as f:
    cfg = json.load(f)

TOKEN = cfg["TOKEN"]
GUILD_ID = int(cfg["GUILD_ID"]) if cfg["GUILD_ID"] else None

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.wait_until_ready()
        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            print("Synced Slash Commands to Guild")
        else:
            await self.tree.sync()
            print("Synced Global Slash Commands")
        print(f"Logged in as {self.user}")

client = MyBot()

@client.tree.command(name="ping", description="Check bot status")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🟢 Bot Online")

@client.tree.command(name="createvps", description="Create VPS With Tmate Session")
async def createvps(interaction: discord.Interaction):
    await interaction.response.send_message("⚙️ Creating VPS with Tmate... please wait")

    os.system("tmate -F -k > session.txt 2>/dev/null & sleep 5")

    try:
        with open("session.txt","r") as f:
            session = f.read()

        await interaction.followup.send(f"✅ VPS Ready\n```\n{session}\n```")

    except:
        await interaction.followup.send("❌ Failed to create tmate session")

client.run(TOKEN)
