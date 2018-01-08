import discord
import asyncio
from discord.ext import commands
import safygiphy
import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import io
from ext import embedtobox
import requests
import json


class GIF:

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def gif(self, ctx, *, args):
        ''' Get a random gif. Usage: gif <tag>'''
        apikey = "hhtmbhqwnLUGMNlyfmMQY2O2ZcM78IQX"
        args = args.lower()
        quary = args
        quary = quary.replace(' ', '+')
        contents = requests.get("http://api.giphy.com/v1/gifs/search?q="+quary+"&api_key="+apikey)
        jsonContent = json.loads(contents.content)
        em = discord.Embed()
        em.set_image(url=jsonContent['data'][0]['images']['fixed_height']['url'])
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)



def setup(bot):
	bot.add_cog(GIF(bot))
