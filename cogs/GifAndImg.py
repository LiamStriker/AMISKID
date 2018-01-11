import discord
import asyncio
from discord.ext import commands
import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import io
from ext import embedtobox
import requests
import json
import random



class GIF:

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def gif(self, ctx, *, args):
        ''' Get a random gif. Usage: gif <tag>'''
        try:
            args = args.lower()
            quary = args
            quary = quary.replace(' ', '+')
            contents = requests.get("http://api.giphy.com/v1/gifs/search?q="+quary+"&api_key=hhtmbhqwnLUGMNlyfmMQY2O2ZcM78IQX")
            jsonContent = json.loads(contents.content)
            r = random.randint(0,19)
            author = ctx.message.author
            em = discord.Embed(title = "Link", url = jsonContent['data'][r]['images']['fixed_height']['url'])
            em.color = await ctx.get_dominant_color(url=author.avatar_url)
            em.set_image(url= jsonContent['data'][r]['images']['fixed_height']['url'])
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                em_list = await embedtobox.etb(em)
                for page in em_list:
                    await ctx.send(page)

        except Exception as e:
            await ctx.send("Gif not found")



def setup(bot):
	bot.add_cog(GIF(bot))
