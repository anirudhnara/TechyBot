import discord
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="t!")

@bot.event
async def on_ready():
    print('bot is on')

keep_alive()
bot.run('Nzg4NjE1OTcxMzc1Mjg0MjM1.X9mF2w.Le0-Qlgin-JCciadX3ivNQRuQRU')