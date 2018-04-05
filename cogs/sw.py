'''for Ami bot by Noble .-.'''
import os
import discord
import asyncio
import requests
import json
from discord.ext import commands
from bs4 import BeautifulSoup

class SoulWorker:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def swlogin(self, ctx):
        '''login status'''
        try:
            url = "{}".format(os.environ.get("login_sw"))
            r = requests.get(url)
            j = json.loads(r.content)

            o = j[0]
            t = j[1]
            tt = j[2]
            f = j[3]
            ff = j[4]
            s = j[5]
            if o["current_status"] == "ONLINE":
                status0 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status0 = ":red_circle: [OFFLINE]"

            if t["current_status"] == "ONLINE":
                status1 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status1 = ":red_circle: [OFFLINE]"

            if tt["current_status"] == "ONLINE":
                status2 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status2 = ":red_circle: [OFFLINE]"

            if f["current_status"] == "ONLINE":
                status3 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status3 = ":red_circle: [OFFLINE]"

            if ff["current_status"] == "ONLINE":
                status4 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status4 = ":red_circle: [OFFLINE]"

            if s["current_status"] == "ONLINE":
                status5 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status5 = ":red_circle: [OFFLINE]"
            #passed = (time - o["last_offline"]).days

            data_o = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(o["name"],o["last_offline"][0:10] ,status0)
            data_t = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(t["name"],t["last_offline"][0:10] ,status1)
            data_tt = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(tt["name"],tt["last_offline"][0:10] ,status2)
            data_f = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(f["name"],f["last_offline"][0:10] ,status3)
            data_ff = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(ff["name"],ff["last_offline"][0:10] ,status4)
            data_s = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(s["name"],s["last_offline"][0:10] ,status5)

            em = discord.Embed(color = 0000)
            em.set_thumbnail(url = "https://image.ibb.co/kUL9px/soulworker_screenshot_2.jpg")
            em.set_author(name = "Login Status: ", icon_url = "https://image.ibb.co/hXojNH/soul_worker.jpg")
            em.add_field(name = "1.", value = data_o, inline = True)
            em.add_field(name = "2.", value = data_t, inline = True)
            em.add_field(name = "3.", value = data_tt, inline = True)
            em.add_field(name = "4.", value = data_f, inline = True)
            em.add_field(name = "5.", value = data_ff, inline = True)
            em.add_field(name = "6.", value = data_s, inline = True)
            em.set_footer(text='|Soul Worker|', icon_url = self.bot.user.avatar_url)
            await ctx.send(content = "**For Game status, use swgame**", embed = em)
        except Exception as e:
            print(e)
            await ctx.send(f"Some error keppo <@280271578850263040> <@300944772971888640> `{e}`")
    @commands.command()
    async def swgame(self, ctx):
        '''game status'''
        try:
            url = "{}".format(os.environ.get("game_sw"))
            r = requests.get(url)
            j = json.loads(r.content)
            o = j[0]
            t = j[1]
            tt = j[2]
            f = j[3]
            ff = j[4]
            s = j[5]
            if o["current_status"] == "ONLINE":
                status0 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status0 = ":red_circle: [OFFLINE]"

            if t["current_status"] == "ONLINE":
                status1 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status1 = ":red_circle: [OFFLINE]"

            if tt["current_status"] == "ONLINE":
                status2 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status2 = ":red_circle: [OFFLINE]"

            if f["current_status"] == "ONLINE":
                status3 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status3 = ":red_circle: [OFFLINE]"

            if ff["current_status"] == "ONLINE":
                status4 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status4 = ":red_circle: [OFFLINE]"

            if s["current_status"] == "ONLINE":
                status5 = "<:greencircle:431340659165888534> [ONLINE]"
            else:
                status5 = ":red_circle: [OFFLINE]"

            data_o = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(o["name"],o["last_offline"][0:10] ,status0)
            data_t = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(t["name"],t["last_offline"][0:10] ,status1)
            data_tt = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(tt["name"],tt["last_offline"][0:10] ,status2)
            data_f = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(f["name"],f["last_offline"][0:10] ,status3)
            data_ff = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(ff["name"],ff["last_offline"][0:10] ,status4)
            data_s = "**Name:** {0}\n**Last offline:** {1}\n**Status:** {2}".format(s["name"],s["last_offline"][0:10] ,status5)

            em = discord.Embed(color = 0000)
            em.set_thumbnail(url = "https://image.ibb.co/kUL9px/soulworker_screenshot_2.jpg")
            em.set_author(name = "Game Status: ", icon_url = "https://image.ibb.co/hXojNH/soul_worker.jpg")
            em.add_field(name = "1.", value = data_o, inline = True)
            em.add_field(name = "2.", value = data_t, inline = True)
            em.add_field(name = "3.", value = data_tt, inline = True)
            em.add_field(name = "4.", value = data_f, inline = True)
            em.add_field(name = "5.", value = data_ff, inline = True)
            em.add_field(name = "6.", value = data_s, inline = True)
            em.set_footer(text='|Soul Worker|', icon_url = self.bot.user.avatar_url)
            await ctx.send(content = "**For Login status, use swlogin**", embed = em)
        except Exception as e:
            print(e)
            await ctx.send(f"Some error keppo <@280271578850263040> <@300944772971888640> `{e}`")


def setup(bot):
	bot.add_cog(SoulWorker(bot))
