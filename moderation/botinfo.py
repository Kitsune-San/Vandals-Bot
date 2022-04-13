


from logging import StrFormatStyle
from os import name
import discord
from discord.errors import HTTPException
from discord.ext import commands
import platform
import assets
import utilities
watermark  = utilities.get_json(assets.watermark_file)

class botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name='botinfo')
    async def botinfo(self, ctx):

        discord_version = discord.__version__
        python_version = platform.python_build
        total_guilds = len(self.bot.guilds)
        total_members = len(set(self.bot.get_all_members()))
        ping = 'Pong! `{0} ms `'.format(round(self.bot.latency * 1000))
        dev_version = "V3.0: Dev-006"
        live_version = "V2.3"

        embed = discord.Embed(name='Bot information', color = discord.Color.green())
        embed.set_author(name=watermark["Watermark"])
        embed.add_field(name="**Discord version:**", value= discord_version, inline=False)
        embed.add_field(name="**Python version:**", value=platform.python_version(), inline=False)
        embed.add_field(name="**Bot Dev Version:**", value=dev_version, inline=False)
        embed.add_field(name="Live bot version:", value=live_version, inline=False)
        embed.add_field(name="**Total guilds:**", value=total_guilds, inline=False)
        embed.add_field(name="**Total members:**", value=total_members, inline=False)
        embed.add_field(name="**Latency:**", value=ping, inline=False)

        try:
            await ctx.send(embed = embed)
        except HTTPException as e:
            await ctx.send(f"Python version: {python_version}\nDiscord Version: {discord_version}\nTotal Guilds: {total_guilds}\nTotal members: {total_members}")



    @commands.command(name='av')
    async def av(self, ctx, member : discord.Member = None):
        if member != None:
            await ctx.send(member.avatar_url)
        else:
            await ctx.send(ctx.author.avatar_url)

    
    @commands.command(name='whois')
    async def whois(self, ctx, member : discord.Member = None):
        if  member is not None:
            embed = discord.Embed(name='User information.', color = discord.Color.green())
            date_format = "%a, %d %b %Y %I:%M %p"
            embed.set_author(name=member.display_name, url = member.avatar_url)
            embed.set_thumbnail(url = member.avatar_url)
            embed.add_field(name="Joined at:", value= member.joined_at.strftime(date_format))
            members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
            embed.add_field(name="Join position", value=str(members.index(member) +1 ))
            embed.add_field(name="Registered at:", value=member.created_at.strftime(members))

            if len(member.roles) > 1:
                role_string = ' '.join([r.mention for r in member.roles][1:])
                embed.add_field(name="Roles [{}]".format(len(member.roles) -1 ), value=role_string, inline=False)
                return await ctx.send(embed=embed)
            else:
                embed.add_field(name="Roles:", value="None")
                return await ctx.send(embed=embed)
        else:
            member  = ctx.author
            embed = discord.Embed(name='User information.', color = discord.Color.green())
            date_format = "%a, %d %b %Y %I:%M %p"
            embed.set_author(name=member.display_name, url = member.avatar_url)
            embed.set_thumbnail(url = member.avatar_url)
            embed.add_field(name="Joined at:", value= member.joined_at.strftime(date_format))
            members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
            embed.add_field(name="Join position", value=str(members.index(member) +1 ))
            embed.add_field(name="Registered at:", value=member.created_at.strftime(date_format))

            if len(member.roles) > 1:
                role_string = ' '.join([r.mention for r in member.roles][1:])
                embed.add_field(name="Roles [{}]".format(len(member.roles) -1 ), value=role_string, inline=False)
                return await ctx.send(embed=embed)
            else:
                embed.add_field(name="Roles:", value="None")
                return await ctx.send(embed=embed)














def setup(bot):
    bot.add_cog(botinfo(bot))

