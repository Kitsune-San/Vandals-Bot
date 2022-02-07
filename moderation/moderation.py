from typing import MutableMapping, Optional
import discord
from discord import mentions
from discord.embeds import Embed
from discord.errors import ConnectionClosed
from discord.ext import commands
import sqlite3
import aiofiles
import asyncio
import re
import aiosqlite
import time
i = 1
time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}





class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                raise commands.BadArgument("{} is not a number!".format(v))
        return time


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member : discord.Member, time: TimeConverter, *, reason = None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(("Muted {} for {}s" if time else "Muted {}").format(member, time))
        type = "Mute"
        warndb = sqlite3.connect("./moderation/logs/logs.db")
        warndb.execute("CREATE TABLE IF NOT EXISTS logs (guild_id int, admin_id int, user_id int, reason text, duration text, logtype text)")
        warndb.execute('INSERT OR IGNORE INTO logs (guild_id, admin_id, user_id, reason, duration, logtype) VALUES (?,?,?,?,?,?)', (ctx.guild.id, ctx.author.id, member.id, reason, time,  type))
        warndb.commit()
        if time:
            await asyncio.sleep(time)
            await member.remove_roles(role)
        else:
            return



     #Warning sys 
    @commands.command(name='warn')
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member : discord.Member, *, reason):
        type = "warn"
        duration = "None"
        warndb = await aiosqlite.connect("./moderation/logs/logs.db")
        await warndb.execute("CREATE TABLE IF NOT EXISTS logs (guild_id int, admin_id int, user_id int, reason text, duration text, logtype text)")
        await warndb.execute('INSERT OR IGNORE INTO logs (guild_id, admin_id, user_id, reason, duration, logtype) VALUES (?,?,?,?,?,?)', (ctx.guild.id, ctx.author.id, member.id, reason, duration ,  type))
        await warndb.commit()
        await ctx.reply(f"Warned user {member.display_name}! ", mention_author=True)
        try:
            await warndb.close()
        except ConnectionClosed:
            pass


#Modlogs
    @commands.command(name='modlogs')
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def modlogs(self, ctx, member: discord.Member ):
        warndb = await aiosqlite.connect('./moderation/logs/logs.db')
        index = 0
        embed = discord.Embed(name=f"Showing modlogs for {member.id}", description = "___ ___", color = discord.Color.red())
        msg = await ctx.send(embed=embed)
        try:
            async with warndb.execute('SELECT admin_id, reason, logtype, duration FROM logs WHERE guild_id = ? AND user_id = ?', (ctx.guild.id, member.id,)) as cursor:
                async for entry in cursor:
                    admin_id, reason, logtype, duration = entry
                    admin_name = self.bot.get_user(admin_id)
                    index += 1
                    embed.add_field(name=f"**Case:**{index}", value=f"**User:**({member.id}){member.mention}\n **Type:**{logtype}\n **Admin:**{admin_name.name}#{admin_name.discriminator}\n **Reason:**{reason}\n **Duration:**{duration}", inline=False)
                    await msg.edit(embed=embed)
                await warndb.close()
        except ConnectionClosed:
            pass



    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member = None, *, reason):
        logchannel = self.bot.get_channel(894251500392570881)
        type = "Ban"

        if member is not None:
            if member is not ctx.author:
                await member.ban(reason=reason)

                warndb = sqlite3.connect("./moderation/logs/logs.db")
                warndb.execute("CREATE TABLE IF NOT EXISTS logs (guild_id int, admin_id int, user_id int, reason text, duration text, logtype text)")
                warndb.execute('INSERT OR IGNORE INTO logs (guild_id, admin_id, user_id, reason, duration, logtype) VALUES (?,?,?,?,?,?)', (ctx.guild.id, ctx.author.id, member.id, reason, None,  type))
                embed = discord.Embed(description =f" **Banned user✅ **  {member.mention} Moderator: {ctx.author.mention} Reason: {reason} ")
                await logchannel.send(embed=embed)
            else:
                await ctx.reply("You can't ban yourself!")
        else:
            await ctx.reply("The member is either not found or something went wrong!")
    
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick (self, ctx, member : discord.Member = None, *, reason):
        type = "Kick"
        logchannel = self.bot.get_channel(894251500392570881)

        if member is not None:
            if member is not ctx.author:
                await member.kick(reason=reason)
                warndb = sqlite3.connect("./moderation/logs/logs.db")
                warndb.execute("CREATE TABLE IF NOT EXISTS logs (guild_id int, admin_id int, user_id int, reason text, duration text, logtype text)")
                warndb.execute('INSERT OR IGNORE INTO logs (guild_id, admin_id, user_id, reason, duration, logtype) VALUES (?,?,?,?,?,?)', (ctx.guild.id, ctx.author.id, member.id, reason, None,  type))
                embed = discord.Embed(description =f" **Kicked user✅ **  {member.mention} Moderator: {ctx.author.mention} Reason: {reason} ")
                await ctx.send(embed=embed)
                await logchannel.send(embed=embed)
            else:
                return await ctx.reply("You can not kick yourself!")
        else:
            await ctx.reply("Either the member was not found or something went wrong!")



    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear (self, ctx, amount = 100):
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit = amount)
        await ctx.send("Channel Cleared!")
    


    @commands.command(name='delchannel')
    @commands.has_permissions(kick_members=True)
    async def remove_channel(self, ctx, channel : discord.TextChannel):
        await channel.delete()
        await ctx.send("Channel deleted!")
    
    @commands.command(name='ping')
    async def ping(self, ctx):
        msg  = await ctx.send("Getting Ping....")
        await asyncio.sleep(2)
        await msg.edit(content='Pong! `{0} ms `'.format(round(self.bot.latency * 1000)))
    

    @commands.command(name='apr')
    @commands.has_permissions(ban_members = True)
    async def apr(self, ctx):
        embed = discord.Embed(name='**#Apply channel rules and instructions!**', color = discord.Color.red())

        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.add_field(name='***Rules and instructions***', value="Instructions on how to apply and what to/ not to do.", inline=False)
        embed.add_field(name='**How to apply?**', value="To apply goto <#911671525277569044> and type v!apply")
        embed.add_field(name='**What will happen once I typed v!apply?**', value="The bot will dm you asking you if you wish to start. To start type v!answer. The bot will load all questions and then sends them one by one. With every question you are allowed to type your answer (With spaces) before it sends the next one. Do that until a confirmation screen pops up with a review of your questions. There will be two buttons under that screen with a ✅ or❌. Pressing the checkmark will confirm your application and send it. Pressing the cross mark will cancel it. You'll need to type v!answer again.", inline=False)
        embed.add_field(name="**What happens once I sent the application?**", value="The application will be reviewed and you will get a dm from the bot once you are accepted or denied. Depending on the result a staff team member will contact you about it.", inline=False)
        embed.add_field(name="**Why did my message get deleted in  ☄˚˚✎apply「📝」 ?**", value="Messages in #apply will be instantly deleted to prevent clutter and for these rules to stay visible. This **DOES NOT** mean the command will not work!", inline=False)
        embed.add_field(name="**It says my application got deleted because something was wrong?**", value="It seens you either failed to answer the questions correctly or entered false or spamming answers. Please re-apply again with the correct format!", inline=False)
        embed.add_field(name="**NOTE:**", value="Do **NOT** apply more then once. this messes up the application system and will cause your application to be deleted straight away. If it encounters any error dm <@521028748829786134> with the error code instead!", inline=False)
        embed.set_footer(text="Made by Senpai_Desi#4108")
        await ctx.send(embed=embed)

























def setup(bot):
    bot.add_cog(moderation(bot))