import discord
import os
from discord.ext import commands
from music_cog import music_cog
from help_cog import help_cog
from variety_cog import variety_cog
from dotenv import load_dotenv

# Load variables
load_dotenv("./TOKEN.env")
discord.opus.load_opus("./lib/libopus.so.0.8.0")
bot = commands.Bot(command_prefix='?', intents=discord.Intents.all(), activity = discord.Game(name="Ghetto Rally"))
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(variety_cog(bot))
    await bot.add_cog(music_cog(bot))

token = os.getenv('TOKEN')
bot.run(token)