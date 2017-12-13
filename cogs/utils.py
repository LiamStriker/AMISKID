'''
Actual Cog from Selfbot, edited by Quanta#5556 (N)
'''
import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from lxml import etree
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import unicodedata
import traceback
import textwrap
import aiohttp
import inspect
import asyncio
import time
import re
import io
import os
import random

class Utility:
    '''Useful commands to make your life easier'''
    def __init__(self, bot):
        self.bot = bot
        self.lang_conv = load_json('data/langs.json')
        self._last_embed = None
        self._rtfm_cache = None
        self._last_google = None
        self._last_result = None

    async def is_owner(ctx):
       return ctx.author.id == 300944772971888640


    @commands.command(name='logout')
    @commands.check(is_owner)
    async def _logout(self, ctx):
        '''
        Shuts down the selfbot,
        equivalent to a restart if you are hosting the bot on heroku.
        '''
        await ctx.send('`Selfbot Logging out...`')
        await self.bot.logout()

    @commands.command(name='help')
    async def help(self, ctx):

        user = "Get The User Info.\n**Uses:** `opuser` or `opuser @mention`"
        invite = "Invite Me To Your Server .\n**Uses:** `opinvite` "
        music = "**DO** `opmusic` **for the music commands**(Added Soon I'm Lazy) :slight_smile:"
        about = "Get Info About Me . \n**Uses:** `opabout` "
        avatar = "Get Your Or Server's Avatar.\n**Uses:** `opavatar`,  `opservericon`, `opavatar @mention`"
        actions = "Actions TO Make The Chat Even More Fun.\n**Uses:Action@metion**\n**Actions Are:** `opkiss`, `opslap`, `opbite`, `ophug`"
        server = "Get Server Info.\n**Uses:** `opserver` "
        cmd = "(Secret)Personal Commands.\n**Uses:** `opcmd` <commad>"
        eightball = "Predict Your future.\n**Uses:** `op8ball + Question`"
        ami = "Talk To Me If You Are Bored.\n**Uses:** Start Sentence With `Ami` or `ami`"
        lala = "`op` **For All Commands** `/`** For Music Commands**"

        em = discord.Embed()
        am.set_thumbnail(icon_url = Self.bot.user.avatar_url)
        em.set_author(name = 'Help Menu~',icon_url = https://cdn.discordapp.com/attachments/388676126383276032/390477398287843329/images_5.jpg)
        em.add_field(name = '**Prefix:**', value = lala, inline = False)
        em.add_field(name = '**1.User:**', value = user, inline = False)
        em.add_field(name = '**2.Avatar:**', value = avatar, inline = False)
        em.add_field(name = '**3.Server:**', value = server, inline = False)
        em.add_field(name = '**4.Fun Actions:**', value = actions, inline = False)
        em.add_field(name = '**5.About:**', value = about, inline = False)
        em.add_field(name = '**6.Personal Commands:**', value = cmd, inline = False)
        em.add_field(name = '**7.8Ball:**', value = eightball, inline = False)
        em.add_field(name = '**8.Ami:**', value = ami, inline = False)
        em.add_field(name = '**9.Invite Me:**', value = invite, inline = False)
        em.add_field(name = '**10.Music:**', value = music, inline = False)
        em.colour = discord.Colour.teal()
        em.set_footer(text = "AMi (^~^)",icon_url = self.bot.user.avatar_url)

        await ctx.send(embed = em)

    @commands.command(pass_context=True, hidden=True, name='eval')
    @commands.check(is_owner)
    async def _eval(self, ctx, *, body: str):
        """Evaluates python code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result,
            'source': inspect.getsource
        }

        env.update(globals())

        body = self.cleanup_code(body)
        #await self.edit_to_codeblock(ctx, body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await err.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try:
                        out = await ctx.send(f'```py\n{value}\n```')
                    except:
                        paginated_text = ctx.paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            else:
                self._last_result = ret
                try:
                    out = await ctx.send(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = ctx.paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')

        if out:
            await out.add_reaction('\u2705') #tick
        if err:
            await err.add_reaction('\u2049') #x


    #async def edit_to_codeblock(self, ctx, body):
        #msg = f'{ctx.prefix}eval\n```py\n{body}\n```'
        #await ctx.message.edit(content=msg)


    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

def setup(bot):
    bot.add_cog(Utility(bot))
