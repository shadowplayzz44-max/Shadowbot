#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Discord VPS Deploy Bot
Powered By Shadow
"""

import discord
from discord.ext import commands
import subprocess

# Discord bot token
TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Replace with your bot token

# Command prefix
bot = commands.Bot(command_prefix="!")

# Example VPS list
VPS_LIST = [
    {"ip": "192.168.1.10", "user": "root"},
    # Add more VPS here
]

# Deploy command
def deploy_vps(vps_ip, username):
    try:
        print(f"Deploying VPS {vps_ip} ...")
        # Example: Update + install packages
        cmd = f"ssh {username}@{vps_ip} 'sudo apt update -y && sudo apt upgrade -y && sudo apt install -y nginx mariadb-server git curl php8.2 php8.2-cli unzip'"
        subprocess.call(cmd, shell=True)
        return f"✅ VPS {vps_ip} deployed successfully!"
    except Exception as e:
        return f"❌ Error deploying VPS {vps_ip}: {str(e)}"

# Discord command
@bot.command()
async def deploy(ctx):
    await ctx.send("🚀 Starting VPS deployment...")
    for vps in VPS_LIST:
        result = deploy_vps(vps["ip"], vps["user"])
        await ctx.send(result)

# Ready event
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    print("Powered By Shadow")

# Run bot
bot.run(TOKEN)
