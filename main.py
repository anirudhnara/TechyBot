import discord
import os
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="t!")

@bot.event
async def on_ready():
    print('bot is on')

@bot.event
async def on_message(message):
    if "<@&791756207618260992>" in message.content:
        role = discord.utils.get(message.guild.roles, id=791756207618260992)
        await role.edit(mentionable=False)
        await message.channel.send(embed=discord.Embed(color=discord.Color.red(), description=":lock: The help role is now locked for 10 minutes."))
        await asyncio.sleep(600)
        await role.edit(mentionable=True)
        await message.channel.send(embed=discord.Embed(color=discord.Color.green(), description=":unlock: The help role is now unlocked."))

keep_alive()
bot.run(os.environ.get('BOT_TOKEN'))