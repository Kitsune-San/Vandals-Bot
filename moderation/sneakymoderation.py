import discord
from discord.ext import commands

class sneakymoderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='rickroll')
    @commands.has_permissions(ban_members=True)
    async def rickroll(self, ctx, member : discord.Member = None):
        await ctx.channel.purge(limit=1)
        await member.send("https://tenor.com/view/stupid-stupidity-bullies-gif-23335875")
        await member.send(f"Sent from {ctx.guild.name}")
        await ctx.send("Done")



    @commands.command(name='extendwarranty')
    @commands.has_permissions(ban_members = True)
    async def extendwarranty(self, ctx, member : discord.Member = None):
        await ctx.channel.purge(limit=1)
        await member.send("https://tenor.com/view/car-warranty-cars-extended-warranty-meme-drive-gif-22412970")
        await member.send(f"Sent from {ctx.guild.name}")
        await ctx.send("Done")








def setup(bot):
    bot.add_cog(sneakymoderation(bot))