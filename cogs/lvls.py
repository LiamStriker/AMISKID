import discord
from discord.ext import commands
import random
import json

class levels:
    def __init__:
        self.bot = bot
    lvls = {}
    async def on_message(self, message):
        id = ctx.message.author.id
        if id not in lvls:
            lvls[id] = {'name' : f'{ctx.author.name}'}, 'xp' : 0, 'level' : {'lvlNo' : 1, 'totalxp' : 100}}
        else:
            lvls[id]['xp'] += random.randint(10, 50)
            if lvls[id]['xp'] >= lvls[id]['level']['totalexp']:
                lvls[id]['xp'] = 0
                lvls[id]['level']['lvlNo'] += 1
                lvls[id]['level']['totalxp'] += lvls[id]['level']['totalxp']/2
                await message.channel.send(content = f"congrats lvls[id]['name'] you advanced to level lvls[id]['level']['lvlNo']")
        data = json.dumps(lvls)
        file = open('data/lvls.json', 'w')
        file.write(data)
        file.close()
        
def setup(bot):
    bot.add_cog(lvls(bot))
