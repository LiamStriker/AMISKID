''' By Liam '''
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



class FUN:

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
            await ctx.send("```Gif not found```")

    @commands.command()
    async def ratewaifu(self,ctx,*,member : discord.Member=None):
        '''ratewaifu for fun'''
        user = member or ctx.message.author
        rating = str(random.randint(1,101))
        em = discord.Embed()
        em.set_author(name = "Waifu Rating", icon_url = user.avatar_url)
        em.description = (user.name)+" is a "+rating+" out of 100 on my waifu meter!"
        em.set_thumbnail(url = "https://media.discordapp.net/attachments/395529348217700357/401670968411422731/20180113_150637.png?width=324&height=421")
        em.color = await ctx.get_dominant_color(url=user.avatar_url)
        em.set_footer(text = "AMi", icon_url = self.bot.user.avatar_url)
        await ctx.send(content = "**Waifu rating for** " +(user.mention), embed = em)

    @commands.command()
    async def say(self,ctx,*,args=None):
        if args is None:
            await ctx.send('Type something you want me to say first!')
        else:
            await ctx.send(args)

    @commands.command()
    async def rem(self,ctx):
        with open('data/rem.json') as f:
            image = json.load(f) #image credits to Deadman
        i = random.choice(image)
        em = discord.Embed(title = "Link", url = i)
        #em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
        em.colour = discord.Colour.blue()
        em.set_image(url = i)

        await ctx.send(embed=em)

    @commands.command()
    async def rin(self,ctx):
        with open('data/rin.json') as f:
            image = json.load(f) #image credits to obeonix
        i = random.choice(image)
        em = discord.Embed(title = "Link", url = i)
        #em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
        em.colour = discord.Colour.red()
        em.set_image(url = i)

        await ctx.send(embed=em)







def setup(bot):
	bot.add_cog(FUN(bot))
