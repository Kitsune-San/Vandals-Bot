from typing import Optional
import discord
from discord.errors import ClientException
from discord.ext import commands, tasks
from discord.ext.commands.errors import DisabledCommand
from discord.player import FFmpegOpusAudio
from discord_components import interaction
from discord_components.component import Button
from ffmpeg import * 
import asyncio
from discord import FFmpegOpusAudio
from fun import messages




class vc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='play')
    async def play(self, ctx, *, option: Optional[str]= None):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            global voice
            voice = await channel.connect()


            embed = discord.Embed(name= 'Doom songs', color = 0xff00ff)
            embed.add_field(name='Please select one of the doom songs.', value="Current songs:\n Hell on earth\nCultist base\nBlood harvesting\nbfg division", inline=False)

            if option == "Hell on earth":
                source = FFmpegOpusAudio('hell_on_earth.mp3')
                voice.play((discord.FFmpegOpusAudio('./fun/doomsongs/hell_on_earth.mp3')))
            
            elif option == "Cultist base":
                voice.play((discord.FFmpegOpusAudio('./fun/doomsongs/cultist_base.mp3')))
            
            elif option == "Blood harvesting":
                voice.play((discord.FFmpegOpusAudio('./fun/doomsongs/blood_harvesting.mp3')))

            elif option == "bfg division":
                voice.play((discord.FFmpegOpusAudio('./fun/doomsongs/bfg_division.mp3')))

               

            
            elif option == None:
                await voice.disconnect()
                await ctx.send(embed = embed)
    
    @commands.command(name='leave')
    async def leave(self, ctx):
        if ctx.guild.me.voice:
            channel = ctx.author.voice.channel
            await voice.disconnect()



    @commands.command(name='sfx')
    async def sfx(self, ctx, *, option:Optional[str]= None):
        global channel
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            try:
                voice = await channel.connect()
            except discord.errors.ClientException:
                await channel.disconnect()
                await channel.connect()
        
            embed = discord.Embed(name= 'Doom songs', color = 0xff00ff)
            embed.add_field(name=messages.embed_title, value=messages.embed_value, inline=False)
            await ctx.channel.purge(limit=1)
            if option == "boo":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/boo.mp3')))
                await asyncio.sleep(3)
                await voice.disconnect()
            elif option == "ha":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/ha.mp3')))
                await asyncio.sleep(2)
                await voice.disconnect()
            elif option =="hello":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/hello.mp3')))
                await asyncio.sleep(1)
                await voice.disconnect()
            elif option == "im-dying":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/im-dying.mp3')))
                await asyncio.sleep(2)
                await voice.disconnect()
            elif option == "jett":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/jett.mp3')))
                await asyncio.sleep(3)
                await voice.disconnect()
            elif option == "katon":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/katon.mp3')))
                await asyncio.sleep(2)
                await voice.disconnect()
            elif option == "emergency food":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/emergency food.mp3')))
                await asyncio.sleep(2)
                await voice.disconnect()
            elif option == "ricefields":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/ricefields.mp3')))
                await asyncio.sleep(4)
                await voice.disconnect()
            elif option == "rickroll":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/rickroll.mp3')))
                await asyncio.sleep(6)
                await voice.disconnect()
            elif option == "squidg":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/squidg.mp3')))
                await asyncio.sleep(24)
                await voice.disconnect()
            elif option == "instinct":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/instinct.mp3')))
                await asyncio.sleep(11)
                await voice.disconnect()
            elif option == "plantv":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/plantv.mp3')))
                await asyncio.sleep(4)
                await voice.disconnect()
            elif option == "vtheme":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/vtheme.mp3')))
                await asyncio.sleep(8)
                await voice.disconnect()
            elif option == "weak":
                voice.play((discord.FFmpegOpusAudio('./fun/sfx/weak.mp3')))
                await asyncio.sleep(4)
                await voice.disconnect()
            elif option == None:
                await voice.disconnect()
                await ctx.send(embed=embed)
            else:
                await ctx.send(messages.Not_yet_Existing)
                await ctx.send(embed = embed)


               




        
        
    


def setup(bot):
    bot.add_cog(vc(bot))