import discord

# TO DOWNLOAD FFMPEG: 
# ctrl+shift+s
# npm install ffmpeg-static
# node -e "console.log(require('ffmpeg-static'))"
# copy result to variable below: 

FFMPEG_PATH = '/home/runner/yourreplnamehere/node_modules/ffmpeg-static/ffmpeg'

# You must include this line for it to work

discord.opus.load_opus("./libopus.so.0.8.0")

client = discord.Client()

# good luck!
