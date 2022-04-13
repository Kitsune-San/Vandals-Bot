import asyncio
from os import name
from typing import Optional
import discord 
from discord.errors import ConnectionClosed
from discord.ext import commands
import sqlite3
import aiosqlite
from discord.ext.commands.errors import CommandInvokeError, CommandOnCooldown
from discord_components import DiscordComponents, ComponentsBot, Button, interaction



class application(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        DiscordComponents(bot)
        
    

    @commands.Cog.listener()
    async def on_command_error(ctx,  error):
        if isinstance(error, CommandOnCooldown):
            msg = f'**This command is still on cooldown. You can try again in{.2.f}s**'.format(error.retry_after)
            await ctx.send(msg)



    @commands.command(name='apply')
    @commands.cooldown(1,21600, commands.BucketType.user)
    async def apply(self, ctx):
        if ctx.channel.id != 911671525277569044:
            await ctx.message.delete()
            return await ctx.send(f"Applications are not handled here. Use <#911671525277569044> Instead! {ctx.author.mention}")
        else:
            try:
                await ctx.message.delete()
                msg = await ctx.send(f"Starting Application.... {ctx.author.mention}")
                appdb = sqlite3.connect("./applications/applications/applications.db")
                appdb.execute("CREATE TABLE IF NOT EXISTS logs (userid int, q1 int, q2 text, q3 text, q4 text, q5 int, q6 int, q7 int, q8 text, q9 int, q10 text, q11 text, q12 text)")

                embed = discord.Embed(name='Application', color = discord.Color.red())
                embed.add_field(name="**Welcome:** ", value= "Welcome to the application for the vandals clan. Use v!answer to start the application.")
                await ctx.author.send(embed = embed)
                await msg.edit(content=f"Sent Applications in dms {ctx.author.mention}")
                await asyncio.sleep(2)
                await msg.delete()
                appdb.close()
            except Exception as e:
                return await ctx.send(f"Oh no I encountered an error while starting the application module. Please forward this to <@521028748829786134> with the code\n `{e}` ")




    @commands.command(name='answer')
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def answer(self, ctx):
        application_chan = self.bot.get_channel(899087952385294406)
        message_init = await ctx.author.send("Loading questions....")
        member = ctx.author
        await asyncio.sleep(2)
        await message_init.edit(content="Get ready!")

        # Question progress
        await ctx.send("**Question 1:** What is your age?")
        a1 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q1 = a1.content
        await ctx.send("**Question 2:** What is your device? ")
        a2 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q2 = a2.content
        await ctx.send("**Question 3:** What is your Gaming style? {signle, double, paw, claw}?")
        a3 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q3 = a3.content
        await ctx.send("**Question 4:** What is your region? (EU, AS, NA)?**")
        a4 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q4 = a4.content
        await ctx.send("**Question 5: ** How active are you on C-OPS (1-10)?")
        a5 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q5 = a5.content
        await ctx.send("**Question 6: ** How active are you on discord? (1-10)?")
        a6 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q6 = a6.content
        await ctx.send("**Question 7 : ** How toxic are you from 1-10 (Be honest)?")
        a7 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q7 = a7.content
        await ctx.send("**Question 8: ** Are you able to vc or atleast listen? {yes or no}?")
        a8 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q8 = a8.content
        await ctx.send("**Question 9: ** How loyal are you from 1-10?")
        a9 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q9 = a9.content
        await ctx.send("**Question 10:** If you do not make it to comp do you want to be a casual player {yes / no}?")
        a10 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q10 = a10.content
        await ctx.send("**Question 11:** How long have you been playing for? ")
        a11 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q11 = a11.content
        await ctx.send("**Question 12:** What is your ign?")
        a12 = await self.bot.wait_for("message", check = lambda message: message.author == member)
        q12 = a12.content

        await ctx.send("All questions answered! Here is an overview")

        embed = discord.Embed(name="Your application", color = discord.Color.orange())
        embed.add_field(name = "Question one:", value= q1, inline=False)
        embed.add_field(name = "Question two:", value= q2, inline=False)
        embed.add_field(name='Question three:', value=q3, inline=False)
        embed.add_field(name="Question four:", value=q4, inline=False)
        embed.add_field(name = "Question five:", value = q5, inline=False)
        embed.add_field(name="Question six:", value=q6, inline=False)
        embed.add_field(name="Question seven:", value=q7, inline=False)
        embed.add_field(name="Question eight:", value=q8, inline=False)
        embed.add_field(name="Question nine:", value=q9, inline=False)
        embed.add_field(name="Question ten:", value=q10, inline=False)
        embed.add_field(name="Question eleven:", value=q11, inline=False)
        embed.add_field(name="Question twelve:", value=q12, inline=False)
        embed.set_footer(text="Use the buttons below to submit your application or cancel it!")
        confirm = await ctx.send(embed = embed, components= [[Button(label = "Submit", custom_id="submit", emoji = "✅"), Button(label="Cancel", custom_id="Cancel", emoji="❎")]])
        while True:
            interaction = await self.bot.wait_for("button_click", check = lambda i: i.message.id == confirm.id)

            if interaction.custom_id == "submit":
                process = await interaction.send("Processing....")


                    
                try:
                    appdb = sqlite3.connect("./applications/applications/applications.db")
                    appdb.execute("CREATE TABLE IF NOT EXISTS logs (userid int, q1 int, q2 text, q3 text, q4 text, q5 int, q6 int, q7 int, q8 text, q9 int, q10 text, q11 text, q12 text)")
                    appdb.execute('INSERT OR IGNORE INTO logs (userid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', (ctx.author.id, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12))
                    appdb.commit()
                    appdb.close()
                    await interaction.send("Processed your application. Thank you for applying!")
                    await application_chan.send(f"@here new application from {ctx.author.mention}! use v!review {ctx.author.mention} to review it!")
                except ConnectionClosed:
                    pass
                except Exception as e:
                    await interaction.send(f"Sorry I encountered an error while saving your application. If this happens multiple times please dm Senpai_Desi#4108 with the following information: \n `Exception occured in application fron {ctx.author.name}#{ctx.author.discriminator} {e}`` ")

            if interaction.custom_id == "Cancel":
                process = await interaction.send("Canceling your application...")
                asyncio.sleep(3)
                await interaction.send(content = "Done!")
        


        


    @commands.command(name='review')
    @commands.has_permissions(manage_messages=True)
    async def review(self, ctx, member : discord.Member):
        appdb = await aiosqlite.connect("./applications/applications/applications.db")
        index = 0
        async with appdb.execute('SELECT q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12 FROM logs WHERE userid = ?', (member.id,)) as cursor:
            async for entry in cursor:
                index += 1
                q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12= entry

                embed = discord.Embed(name='Applications', color = discord.Color.gold())
                embed.add_field(name=f"Showing Application from **{member.id}", value="use v!accept or v!deny with reason to acept or deny!")
                embed.add_field(name="**What is your age?**", value= q1, inline=False)
                embed.add_field(name="**What is your device? (use - to define spaces otherwise it will not work!)**", value=q2, inline=False)
                embed.add_field(name='**What is your Gaming style? {signle, double, paw, claw}?**', value=q3, inline=False)
                embed.add_field(name="**What is your region? (EU, AS, NA)**", value=q4, inline=False)
                embed.add_field(name="**How active are you on C-OPS (1-10)?**", value=q5, inline=False)
                embed.add_field(name="**How active are you on discord 1-10?**", value=q6)
                embed.add_field(name="**How toxic are you from 1-10 (Be honest)?**", value=q7, inline=False)
                embed.add_field(name="**Are you able to vc or atleast listen? {yes or no}?**", value=q8, inline=False)
                embed.add_field(name="**How loyal are you from 1-10?**", value=q9,  inline=False)
                embed.add_field(name="**If you do not make it to comp do you want to be a casual player {yes / no}?**", value=q10, inline=False)
                embed.add_field(name='**How long have you been playing for? {use - for spaces otherwise it will not work!!**', value=q11, inline=False)
                embed.add_field(name="**What is your ign? SPACES ALLOWED!**", value=q12, inline=False)

                await ctx.send(embed=embed)
                appdb.close()


    @commands.command(name='accept')
    @commands.has_permissions(kick_members=True)
    async def accept(self, ctx, member : discord.Member, *, reason : Optional[str] = None):
        msg = await ctx.send("Accepting user...")
        if reason is not None:
            await member.send(f"Hello {member.mention}! I am glad to inform you that you have been accepted into Vandals! Congratulations. Reason for this being {reason}")
        else:
            await member.send(f"Hello {member.mention}! I am glad to inform you that you have been accepted into Vandals! Congratulations")

        await msg.edit(content="Done!")


    @commands.command(name='delete')
    @commands.has_permissions(kick_members=True)
    async def delete(self, ctx, member : discord.Member):
        appdb = await aiosqlite.connect("./applications/applications/applications.db")
        async with appdb.execute('SELECT q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12 FROM logs WHERE userid = ?', (member.id,)) as cursor:
            async for entry in cursor:
               q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12= entry
               async with  appdb.execute(f'DELETE FROM logs WHERE userid = {member.id}'):
                await appdb.commit()
                await ctx.reply(f"Deleted the application for {member.mention}")     
                await member.send("Hey your application got deleted because it contained invalid answers or something else was wrong with it!")
    
    @commands.command(name='deny')
    @commands.has_permissions(kick_members=True)
    async def deny(self, ctx, member : discord.Member, *, reason=None):
        if reason is not None:
            msg = await ctx.send("Removing application....")
            appdb = await aiosqlite.connect("./applications/applications/applications.db")
            async with appdb.execute('SELECT q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12 FROM logs WHERE userid = ?', (member.id,)) as cursor:
                async for entry in cursor:
                    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12= entry
                    async with  appdb.execute(f'DELETE FROM logs WHERE userid = {member.id}'):
                        await appdb.commit()
                    await msg.edit(content = "Deletion complete")
                    asyncio.sleep(2)
                    await msg.edit(content = "Informing user...")
                    await member.send(f"Hey, Unfortunately your application got denied with the reason : **{reason}**\n Your stored application got removed. You are always welcome to re apply!")
                    await msg.edit(content = "Done!")













def setup(bot):
    bot.add_cog(application(bot))