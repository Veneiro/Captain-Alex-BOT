import random

from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint


class variety_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_instance = giphy_client.DefaultApi()
        self.giphy_token = "cseP3QC7kHaoUXi19S3RjlPRHkyXlphR";

    async def search_gifs(self, query):
        try:
            response = self.api_instance.gifs_search_get(self.giphy_token, query, limit=3, rating='g')
            lst = list(response.data)
            gif = random.choices(lst)

            return gif[0].url

        except ApiException as e:
            return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

    @commands.command(name='8ball')
    async def magic_eight_ball(self, ctx):
        response = [
            'Without a doubt.',
            'Outlook good.',
            'Better not tell you now.',
            'Cannot predict now.',
            'My reply is no.',
            'Outlook not so good.',
        ]

        gif = await self.search_gifs('cheese')

        await ctx.send(random.choice(response))
        await ctx.send('Gif URL : ' + gif)

    @commands.command(name='gif')
    async def searchGif(self, ctx, *args):
        query = " ".join(args)
        gif = await self.search_gifs(query)

        await ctx.send('Gif URL : ' + gif)
