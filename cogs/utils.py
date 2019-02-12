'''
Actual Cog from Selfbot, edited by Liam and Nub
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
        equivalent to a restart if you are hosting the bot on heroku.
        '''
        await ctx.send('`Ami Logging out...`')
        await self.bot.logout()

    @commands.command(name='help')
    async def help(self, ctx, *, args = None):

        if args is None:

            general = "`user`,`server`,`avatar`,`servericon`,`about`,`invite`,`help`"
            miscellaneous = "`cmd`,`8ball`,`gif`,`Talk to me`,`ratewaifu @mention`,`say [sentence]`\nActions:`kiss`,`hug`,`bite`,`slap`"
            mod = """__**Note**__:For these commands to work both bot and user needs the permissions as well as the bot's role needs to be above the role the command is being used upon.\n\n`kick`,`ban`,`hban`,`unban`,`baninfo`,`banlist`,`purge`,`mute`,`unmute`,`addrole`,`removerole`"""
            music = "__**Note**__: **Prefix** for music is /.\n\n`summon`,`play`,`repeat`,`queue`,`promote[number]`,`disconnect`"
            expand = "To know more about commands.\n`ophelp Category`\nExample~ `ophelp general`"
            support = "Support Server: https://discord.gg/k3PKut6 \nIf you need more help with commands."
            waifu = "**Waifu Commands**:`rem`,`rin`"


            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390477398287843329/images_5.jpg")
            em.set_author(name = 'Help Menu~',icon_url = ctx.author.avatar_url )
            em.description = "My **Prefix** is **op**.To use the commands do op[command]"
            em.add_field(name = '**1.General:**', value = general, inline = False)
            em.add_field(name = '**2.Fun:**', value = miscellaneous, inline = False)
            em.add_field(name = '**3.Mod:**', value = mod, inline = False)
            em.add_field(name = '**4.Music:**', value = music, inline = False)
            em.add_field(name = '**5.Anime:**', value = waifu, inline = False)
            em.add_field(name = '**6.Expanded Help:**', value = expand, inline = False)
            em.add_field(name = '**7.Support Me~**', value = support, inline = False)
            em.colour = discord.Colour.teal()
            em.set_footer(text = "AMi (^~^)",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed = em)
        elif args.lower() == 'music':

            lol = """`/summon`:Summons The Bot To VC\n`/play [song]`: Play's The Song.\n`/repeat`: Cycle Repeat Modes-All,Single,Off.\n`/queue`:See Songs In Queue.\n`/promote [number]`: Put's Song To Position 1 Of Queue.\n`/disconnect`: Disconnects The Bot."""
            hmmsu = "`op` **For All Commands** `/`** For Music Commands**"

            em = discord.Embed()
            em.set_thumbnail(url = "https://media.discordapp.net/attachments/388676126383276032/390729312715800586/20171214_102413.jpg")
            em.set_author(name = 'Music Help~',icon_url = ctx.author.avatar_url )
            em.add_field(name = '**Prefix:**', value = hmmsu, inline = False)
            em.add_field(name = '**Music Commands Are:**', value = lol, inline = False)
            em.colour = discord.Colour.teal()
            em.set_footer(text = "AMi (^~^)",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed = em)

        elif args.lower() == 'general':

            user = "Get the user info.[Aliases:`ui`]\n**Uses:** `opuser` or `opuser @mention`"
            invite = "Invite me to your server.\n**Uses:** `opinvite`"
            avatar = "Get your avatar.\n**Uses:** `opavatar`,`opavatar @mention`"
            servericon = "Get servers icon.\n**Uses:** `opservericon`"
            server = "Get server info.\n**Uses:** `opserver`"
            about = "Get more info about me.\n**Uses:** `opabout`"
            help = "Shows the list of commands and their expanded category.\n**Uses:** `ophelp` or `ophelp [Category]`"


            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390477398287843329/images_5.jpg")
            em.set_author(name = 'General Help~',icon_url = ctx.author.avatar_url )
            em.description = "These are general commands for various infos."
            em.add_field(name = '**1.User Info:**', value = user, inline = False)
            em.add_field(name = '**2.Server Info:**', value = server, inline = False)
            em.add_field(name = '**3.Avatar:**', value = avatar, inline = False)
            em.add_field(name = '**4.Server Icon:**', value = servericon, inline = False)
            em.add_field(name = '**5.About:**', value = about, inline = False)
            em.add_field(name = '**6.Invite:**', value = invite, inline = False)
            em.add_field(name = '**7.Help:**', value = help, inline = False)
            em.colour = discord.Colour.teal()
            em.set_footer(text = "AMi (^~^)",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=em)

        elif args.lower() == 'fun':

            cmd = "(Secret)Personal Commands.\n**Uses:** `opcmd [commad]`"
            eightball = "Predict your future.\n**Uses:** `op8ball [Question]`"
            gif = "Get a gif form Giphy.\n**User:** `opgif [Search query]`"
            ami = "Talk to me if you are bored.Start sentence with Ami/ami.\n**Uses Example:** Ami how are you."
            say = "Type something you want me to say maybe tease your friends and I'll say it\n**Uses:**`opsay [sentence]`"
            rate = "Rate yourself or someone else on my waifu meter and see how good waifu they will be.\n**Uses:** `opratewaifu` or `opratewaifu @mention`"
            actions = "Actions TO Make The Chat Even More Fun And Interactive.\n**Uses:Action@metion**\n**Actions Are:** `opkiss`, `opslap`, `opbite`, `ophug`"

            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390477398287843329/images_5.jpg")
            em.set_author(name = 'Fun Commands Help~',icon_url = ctx.author.avatar_url )
            em.description = "Fun Commands To make the Day Better"
            em.add_field(name = '**1.Personal Commands:**', value = cmd, inline = False)
            em.add_field(name = '**2.Eightball:**', value = eightball, inline = False)
            em.add_field(name = '**3.Gif:**', value = gif, inline = False)
            em.add_field(name = '**4.Actions:**', value = actions, inline = False)
            em.add_field(name = '**5.Talk to me:**', value = ami, inline = False)
            em.add_field(name = '**6.Rate Waifu:**', value = rate, inline = False)
            em.add_field(name = '**7.Say:**', value = say, inline = False)
            em.colour = discord.Colour.teal()
            em.set_footer(text = "AMi (^~^)",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=em)

        elif args.lower() == 'mod':

            kick = "Kick someone from the server.\n**Uses:** `opkick [User]`"
            ban = "Ban someone from the server.\n**Uses:** `opban [User] [Reason(optional)]`"
            hban = "Ban someone who is not already in the server.\n**Uses:**`ophban [User Id]  [Reason(optional)]`"
            unban = "Unban Someone.\n**Uses:** `opunban [User or User Id]`"
            baninfo = "Get the info about a ban from audit log.\n **Uses:** `opbaninfo [User]`"
            banlist = "Get the list of banned members in the server.\n**User:** `opbanlist`"
            purge = "Delete/purge a certain nummber of messages in a channel or of a specific person.[Aliases:`p`,`prune`,`del`]\n**Uses:** `oppurge [No. of messages]` or `oppruge [No. of messages] [User]`"
            mute = """Mute a member making them unable to send messages as well as server mute for VC.**Note:** Duration is important.\n\n**User:** `opmute [User] [Duration(In s,m,h)]`\nExample opmute @member 1h(Mutes member for 1 hour)"""
            unmute = "Unmute a muted member.\n**Uses:**`opunmute [User]`"
            addrole = "Add role to a person.Aliases=[`adrl`,`giverole`]\n**Uses:**`opaddrole [User] [Role name]` "
            removerole = "Remove role from a person.Aliases=[`rmrl`,`rmrole`]\n**Uses:**`opremoverole [User] [Role name]`"

            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390477398287843329/images_5.jpg")
            em.set_author(name = 'Mod Help~',icon_url = ctx.author.avatar_url )
            em.description = "Mod Commands to make managing a server easier."
            em.add_field(name = '**1.Kick**', value = kick, inline = False)
            em.add_field(name = '**2.Ban:**', value = ban, inline = False)
            em.add_field(name = '**3.Hban:**', value = hban, inline = False)
            em.add_field(name = '**4.unban:**', value = unban, inline = False)
            em.add_field(name = '**5.Baninfo:**', value = baninfo, inline = False)
            em.add_field(name = '**6.Banlist:**', value = banlist, inline = False)
            em.add_field(name = '**7.Purge Message:**', value = purge, inline = False)
            em.add_field(name = '**8.Mute:**', value = mute, inline = False)
            em.add_field(name = '**9.Unmute:**', value = unmute, inline = False)
            em.add_field(name = '**10:Addrole.**', value =addrole, inline = False)
            em.add_field(name = '**11.Removerole:**', value = removerole, inline = False)
            em.colour = discord.Colour.teal()
            em.set_footer(text = "AMi (^~^)",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=em)

        elif args.lower() == 'anime':
            rem = "Get random images of Rem.(Because the owner loves rem get over it)\n**Uses:** `oprem`"
            rin = "Get random images of Rin.\n**Uses:** `oprin`"

            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/408893267527335937/408916180485668864/7fa8580d8fbd2717ba4c3a6254b290e0.jpg")
            em.set_author(name = 'Anime Help~',icon_url = ctx.author.avatar_url )
            em.description = "Anime commands for all the anime fans out there.**Under development**(Only waifu commands available at the moment)"
            em.add_field(name = '**Rem:**', value = rem, inline = False)
            em.add_field(name = '**Rin Tohsaka:**', value = rin, inline = False)
            em.colour = discord.Colour.blue()
            em.set_footer(text = "AMi (^~^)",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=em)


        else:
            await ctx.send('That **Category** does not exist. Check your **spelling!**')



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
