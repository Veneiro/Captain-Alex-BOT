import discord
from webserver import keep_alive
import os
from discord.ext import commands
from music_cog import music_cog
from help_cog import help_cog
from variety_cog import variety_cog
from dotenv import load_dotenv

# Load variables
load_dotenv("./TOKEN.env")
discord.opus.load_opus("./libopus.so.0.8.0")
bot = commands.Bot(command_prefix='?', intents=discord.Intents.all(), activity = discord.Game(name="Ghetto Rally"))
bot.remove_command("help")

#bot.add_cog(help_cog(bot))
#bot.add_cog(music_cog(bot))
#bot.add_cog(variety_cog(bot))

@bot.event
async def on_ready():
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(variety_cog(bot))
    await bot.add_cog(music_cog(bot))

token = os.getenv('TOKEN')

while __name__ == '__main__':
    try:
        #keep_alive()
        bot.run(token)
    except discord.errors.HTTPException:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        os.system('kill 1')
    except discord.ext.commands.errors.CommandInvokeError:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        os.system('kill 1')
    except discord.ext.commands.errors.HTTPException:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        os.system('kill 1')