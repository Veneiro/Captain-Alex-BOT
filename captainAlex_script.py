import asyncio
import discord
import os
import youtube_dl
from discord.ext import commands
from music_cog import music_cog
from help_cog import help_cog
from dotenv import load_dotenv



# Load variables
load_dotenv("./TOKEN.env")
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

token = os.getenv('TOKEN')



bot.run(token)
