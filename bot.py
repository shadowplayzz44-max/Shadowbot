import discord
from discord import app_commands
import json

config = json.load(open("config.json"))

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        guild = discord.Object(id=int(config["guild_id"]))
        await self.tree.sync(guild=guild)
        print(f"Bot is Online as {self.user}")

client = MyBot()

@client.tree.command(
    name="deploy",
    description="Deploy VPS and send server details",
    guild=discord.Object(id=int(config["guild_id"]))
)
async def deploy(interaction: discord.Interaction):

    # Change here if needed
    vps_name = "Shadow"
    ip = "103.174.247.101"
    password = "shadow"

    embed = discord.Embed(
        title="🌍 Your VPS is Ready!",
        description="Here are your premium server details:",
        color=0x8F00FF
    )

    embed.add_field(name="💻 VPS Name", value=vps_name, inline=False)
    embed.add_field(name="🌐 IP Address", value=ip, inline=False)
    embed.add_field(name="🔑 Root Password", value=password, inline=False)
    embed.add_field(name="💻 SSH Login", value=f"ssh root@{ip}", inline=False)

    embed.set_footer(text="🔥 Powered by FluidNodes")

    await interaction.response.send_message(embed=embed)

client.run(config["token"])
