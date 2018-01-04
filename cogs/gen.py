''' A rewritten cog, consisting of old personal commands (just for fun) also has kiss, hug, slap commands.
PS: THIS ISNT CUSTOM COMMANDS

Originally by Liam, Rewritten by Quanta#5556 (N)

'''
import os
import discord
import json
import random
from discord.ext import commands
from cleverwrap import CleverWrap


class Gen:
    def __init__(self, bot):
        self.bot = bot

    @property
    def cmds(self):
        '''loading the commands'''
        with open("data/personals.json") as f:
            cmds = json.load(f)

        return cmds
    @property
    def kiss_gif(self):
        links = ["http://i.imgur.com/0D0Mijk.gif", "http://i.imgur.com/TNhivqs.gif", "http://i.imgur.com/3wv088f.gif", "http://i.imgur.com/7mkRzr1.gif", "http://i.imgur.com/8fEyFHe.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def slap_gif(self):
        links = ["http://imgur.com/Lv5m6cb.gif", "http://i.imgur.com/BsbFQtz.gif", "http://i.imgur.com/hyygFya.gif", "http://i.imgur.com/XoHjIlP.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def hug_gif(self):
        links = ["http://i.imgur.com/sW3RvRN.gif", "http://i.imgur.com/gdE2w1x.gif", "http://i.imgur.com/zpbtWVE.gif", "http://i.imgur.com/ZQivdm1.gif", "http://i.imgur.com/MWZUMNX.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def bite_gif(self):
        links = ["https://cdn.discordapp.com/attachments/383492139901911044/391156012754796544/bite.gif","https://cdn.discordapp.com/attachments/383492139901911044/384283524355719168/hmmsu.gif", "https://cdn.discordapp.com/attachments/383492139901911044/384293280898088960/bitesu.gif"]
        choice_made= random.choice(links)
        return choice_made

    @property
    def cleverbot_Key(self):
        '''loading the api key'''
        with open("data/config.json") as f:
            cl_key = json.load(f)
            if cl_key["cleverbot_key"] == "api_key_here":
                key_cl = os.environ.get("cleverbot_key")
            else:
                key_cl = cl_key["cleverbot_key"]

        return key_cl

    @commands.command()
    async def cmd(self, ctx, *, args):
        '''using the loaded the commands'''
        try:
            personal = self.cmds
            if args == None:
                await ctx.send(content = "`Missing Args`")
            args = args.lower()
            loaded_command = personal["{}".format(args)]
            if "https" not in loaded_command:
                await ctx.send("```"+loaded_command+"```")
            else:
                em = discord.Embed()
                em.set_image(url = "{}".format(loaded_command))
                await ctx.send(embed = em)
        except discord.ext.commands.errors.MissingRequiredArgument as e:
            await ctx.send("`Missing args`")

    @commands.command()
    async def kiss(self, ctx, *, args):
        '''Kissing gif send, PS: missing args will show up at logs'''
        kiss = self.kiss_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(kiss))
        await ctx.send(content = "**{0} got kissed by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def bite(self, ctx, *, args):
        '''bitting gif send, PS: missing args will show up at logs'''
        kiss = self.bite_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(kiss))
        await ctx.send(content = "**{0} got bitten by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def slap(self, ctx, *, args):
        '''slapping gif send, PS: missing args will show up at logs'''
        kiss = self.slap_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(kiss))
        await ctx.send(content = "**{0} got slapped by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def hug(self, ctx, *, args):
        '''hugging gif send, PS: missing args will show up at logs'''
        kiss = self.hug_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(kiss))
        await ctx.send(content = "**{0} got hugged by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def mi(self, ctx, *, args):
         '''No point in doing this, can be made better, but will be like this for the moment'''
         cl_key = self.cleverbot_Key
         cl_load = CleverWrap("{}".format(cl_key))
         cl_resp = cl_load.say("{}".format(args))
         await ctx.send(content = cl_resp)
         cl_load.reset()

    @commands.command()
    async def invite(self,ctx):
        '''invite the bot'''

        em = discord.Embed()

        em = discord.Embed(title = "My Invite Link", url = "https://discordapp.com/oauth2/authorize?client_id=381111258172227585&scope=bot&permissions=305196166")
        em.set_author(name = "You Can get Me From Here", icon_url = ctx.author.avatar_url)
        em.colour = discord.Colour.green()
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390726053561368577/images_23.jpg")
        em.add_field(name = "Thank You For Using Me", value = "(^~^)", inline = True)
        em.set_footer(text = "AMi",icon_url = self.bot.user.avatar_url)

        await ctx.send(embed = em)



def setup(bot):
	bot.add_cog(Gen(bot))
