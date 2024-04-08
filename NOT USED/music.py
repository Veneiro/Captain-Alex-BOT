import discord
import yt_dlp
from discord.ext import commands

class MusicBot(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.voice_client = None
        self.playlist = []
        self.current_song = None
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': False,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'auto'
        }

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')

    async def play_song(self, ctx):
        if not self.playlist:
            return await ctx.send("La lista de reproducción está vacía, añade algunas canciones primero!")

        song_url = self.playlist[0]
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(song_url, download=False)
            url = info['formats'][0]['url']
            title = info['title']
            self.current_song = {'title': title, 'url': url}

        if not self.voice_client.is_playing():
            self.voice_client.play(discord.FFmpegPCMAudio(self.current_song['url'], executable='ffmpeg'), after=lambda e: self.play_next_song(ctx))

        await ctx.send(f"Reproduciendo: {self.current_song['title']}")

    def play_next_song(self, ctx):
        if self.playlist:
            self.playlist.pop(0)
            self.play_song(ctx)
        else:
            self.current_song = None
            self.voice_client.stop()

    @staticmethod
    def get_url(query):
        with yt_dlp.YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
            try:
                info = ydl.extract_info(query, download=False)
                return {'title': info['title'], 'url': info['formats'][0]['url']}
            except:
                return None

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!play'):
            query = message.content.split(' ', 1)[1]
            song = self.get_url(query)
            if song:
                self.playlist.append(song['url'])
                if not self.voice_client.is_playing():
                    self.voice_client = await discord.VoiceChannel.connect(message.author.voice.channel)
                    await self.play_song(message.channel)
            else:
                await message.channel.send("No se ha podido encontrar la canción.")

        elif message.content.startswith('!queue'):
            if not self.playlist:
                await message.channel.send("La lista de reproducción está vacía.")
            else:
                queue_list = "\n".join([f"{i+1}. {song}" for i, song in enumerate(self.playlist)])
                await message.channel.send(f"Lista de reproducción:\n{queue_list}")

        elif message.content.startswith('!skip'):
            if self.voice_client.is_playing():
                self.voice_client.stop()
                await self.play_song(message.channel)

        elif message.content.startswith('!stop'):
            self.playlist = []