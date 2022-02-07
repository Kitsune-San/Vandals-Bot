import discord
from discord.ext import commands
import sqlite3
from PIL import Image
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
import aiofiles
import aiosqlite
from better_profanity import profanity
import asyncio
from discord.ext.commands.errors import MessageNotFound

from discord.message import Message


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

        
  

    @commands.Cog.listener()
    async def on_member_join(self, member):
        community_role = member.guild.get_role(894015808680906783)
        guild = self.bot.get_guild(893945437587931136)
        welcomeChaannel = self.bot.get_channel(893981833367273483)
        log_channel = self.bot.get_channel(894251500392570881)
        await member.add_roles(community_role)

        await member.send(f"Hey {member.mention} Welcome to {member.guild}! Enjoy your time! ")
        await log_channel.send(f"Gave {member.mention} the {community_role.name} Role")
    


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = self.bot.get_guild(893945437587931136)
        welcomeChaannel = self.bot.get_channel(893982020290629652)
        await welcomeChaannel.send(f"Rip {member.mention} left. We now have {guild.member_count} Vandal members!")

        
#size = 132 x 132
#location 48, 104
    


    @commands.Cog.listener()
    async def on_message(self, message):

        bot_info = self.bot.get_user(898504638674903060)
        emoji = self.bot.get_emoji(910655847091306517)
        if message.author == self.bot.user:
            return
        elif message.content.startswith("Hello"):
            await message.add_reaction("👋")
        elif message.content.startswith("hi"):
            await message.add_reaction("👋")
        elif message.content.startswith("hello"):
            await message.add_reaction("👋")
        elif message.content.startswith("Hi"):
            await message.add_reaction("👋")
        else:
            if "wobble" in message.content.lower():
                await message.channel.send(emoji)
            else:
                return


def setup(bot):
    bot.add_cog(events(bot))