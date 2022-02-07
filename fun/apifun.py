import discord
from discord.ext import commands
import requests
import assets
import utilities
import random
import hashlib

config = utilities.get_json(assets.config_file)
fight_results = ["and missed",
                 "and hit doing fatal damage!",
                 "and Lost",
                 "And won"]

                 
class apifun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='cat')
    async def cat(self, ctx):
        await ctx.channel.trigger_typing()
        api_key = config['cat_api']
        cat = requests.get(f"https://api.thecatapi.com/v1/images/search?api_key={api_key}")
        url = cat.json()[0]["url"]
        await ctx.send(url)

    
    @commands.command()
    async def intellect(self, ctx, *, msg:str):
        """Me, an intellectual"""
        await ctx.channel.trigger_typing()
        intellectify = ""
        for char in msg:
            intellectify += random.choice([char.upper(), char.lower()])
        await ctx.send(intellectify)
    
    @commands.command()
    async def md5(self, ctx, *, msg:str):
        """Encrypt something into MD5"""
        await ctx.send("`{}`".format(hashlib.md5(bytes(msg.encode("utf-8"))).hexdigest()))
    
    @commands.command()
    async def sha256(self, ctx, *, msg:str):
        """Encrypt something into sha256"""
        await ctx.send("`{}`".format(hashlib.sha256(bytes(msg.encode("utf-8"))).hexdigest()))

    @commands.command()
    async def sha512(self, ctx, *, msg:str):
        """Encrypt something into sha512"""
        await ctx.send("`{}`".format(hashlib.sha512(bytes(msg.encode("utf-8"))).hexdigest()))

    @commands.command()
    async def uppercase(self, ctx, *, msg:str):
        """UPPERCASE DIS"""
        await ctx.send(msg.upper())

    @commands.command()
    async def lowercase(self, ctx, *, msg:str):
        """lowercase dis"""
        await ctx.send(msg.lower())
    
    @commands.command()
    async def fight(self, ctx, user:str=None, *, weapon:str=None):
        """Fight someone with something"""
        if user is None or user.lower() == ctx.author.mention or user == ctx.author.name.lower() or ctx.guild is not None and ctx.author.nick is not None and user == ctx.author.nick.lower():
            await ctx.send("{} fought themself but only ended up in a mental hospital!".format(ctx.author.mention))
            return
        if weapon is None:
            await ctx.send("{0} tried to fight {1} with nothing so {1} beat the breaks off of them!".format(ctx.author.mention, user))
            return
        await ctx.send("{} used **{}** on **{}** {}".format(ctx.author.mention, weapon, user, random.choice(fight_results).replace("%user%", user).replace("%attacker%", ctx.author.mention)))


    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.event.start
    

    @commands.command(name='invtrack')
    async def invites(self, ctx, usr: discord.Member=None):
        guild = ctx.guild
        if usr is not None:
            user = usr
            total_invites = 0
            try:
                for i in await guild.invites():
                    if i.inviter == user:
                        total_invites += i.uses
                await ctx.send(f"{user.name} has invited {total_invites} member{'' if total_invites == 1 else 's'}!")
            except Exception as e:
                return await ctx.send(e)
        else:
            usr = ctx.author










def setup(bot):
    bot.add_cog(apifun(bot))