import discord
from discord.ext import commands
import random
import json

class levels:
    def __init__(self, bot):
        self.bot = bot
        self.lvls = {}
    async def on_message(self, message):
        id = message.author.id
        if id not in self.lvls and message.author.bot == False:
            self.lvls[id] = {'name' : message.author.name, 'xp' : 0, 'level' : {'lvlNo' : 1, 'totalxp' : 100}}
        elif message.author.bot == False:
            self.lvls[id]['xp'] += random.randint(10, 50)
            if self.lvls[id]['xp'] >= self.lvls[id]['level']['totalxp']:
                self.lvls[id]['xp'] = 0
                self.lvls[id]['level']['lvlNo'] += 1
                self.lvls[id]['level']['totalxp'] += self.lvls[id]['level']['totalxp']/2
                await message.channel.send(content = f"congrats {self.lvls[id]['name']} you advanced to level {self.lvls[id]['level']['lvlNo']}")
        data = json.dumps(self.lvls)
        file = open('data/lvls.json', 'w')
        file.write(data)
        file.close()
        
def setup(bot):
    bot.add_cog(levels(bot))
