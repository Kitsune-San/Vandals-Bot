import discord
from discord.ext import commands
from discord_components import *

class admins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='shutdown')
    @commands.is_owner()
    async def shutdown(self, ctx):
        try:
            embed = discord.Embed(name='Shutdown', color = discord.Color.red())
            embed.add_field(name="Bot shutdown?", value="Shutting down the bot will terminate any openstanding process!")

            msg = await ctx.send(embed = embed, components=[[Button(label="Yes", style  = 2, emoji="✅", custom_id="confirm"), Button(label="No", style=2, custom_id="deny", emoji="❎")]])
            while True:
                interaction = await self.bot.wait_for("button_click")


                if interaction.custom_id == "confirm":
                    await interaction.send("Okay, bot shutting down..", ephemeral  = False)
                    await self.bot.logout()
                
                if interaction.custom_id == "deny":
                    await interaction.respond(content="Alright. Cancelled shutdown", ephemeral  = False)
        
        except Exception as e:
            return await ctx.send(f"`{e}`")


        except RuntimeError:
            pass
    
    @commands.command(name='_reload')
    @commands.is_owner()
    async def _reload(self, ctx, *, module):
        try:
            embed = discord.Embed(name='Reload', color = discord.Color.blurple())
            embed.add_field(name=f"Reload cog", value=f"Are you sure you want to reload `{module} ?`")
            msg = await ctx.send(embed = embed, components=[[Button(label="Yes", style  = 2, emoji="✅", custom_id="confirm"), Button(label="No", style=2, custom_id="deny", emoji="❎")]])
            while True:
                interaction = await self.bot.wait_for("button_click")


                if interaction.custom_id == "confirm":
                    await interaction.send("Okay, reloading the module...")
                    self.bot.unload_extension(module)
                    self.bot.load_extension(module)
                    await interaction.respond(content = "Done!", ephemeral  = False)
                
                if interaction.custom_id == "deny":
                    await interaction.respond(content="Alright. Cancelled reload", ephemeral  = False)
        
        except Exception as e:
            return await ctx.send(e)
        



    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, *, module):
        try:
            embed = discord.Embed(name='load', color = discord.Color.blurple())
            embed.add_field(name=f"load cog", value=f"Are you sure you want to load `{module} ?`")
            msg = await ctx.send(embed = embed, components=[[Button(label="Yes", style  = 2, emoji="✅", custom_id="confirm"), Button(label="No", style=2, custom_id="deny", emoji="❎")]])
            while True:
                interaction = await self.bot.wait_for("button_click")


                if interaction.custom_id == "confirm":
                    await interaction.send("Okay, loading the module...", ephemeral = False)
                    self.bot.load_extension(module)
                    await interaction.respond(content = "Done!", ephemeral  = False)
                
                if interaction.custom_id == "deny":
                    await interaction.respond(content="Alright. Cancelled load", ephemeral  = False)
        
        except Exception as e:
            return await ctx.send(e)




    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, *, module):
        try:
            embed = discord.Embed(name='unload', color = discord.Color.blurple())
            embed.add_field(name=f"unload cog", value=f"Are you sure you want to unload `{module} ?`")
            msg = await ctx.send(embed = embed, components=[[Button(label="Yes", style  = 2, emoji="✅", custom_id="confirm"), Button(label="No", style=2, custom_id="deny", emoji="❎")]])
            while True:
                interaction = await self.bot.wait_for("button_click")


                if interaction.custom_id == "confirm":
                    await interaction.send("Okay, unload the module...")
                    self.bot.unload_extension(module)
                    await interaction.respond(content = "Done!", ephemeral  = False)
                
                if interaction.custom_id == "deny":
                    await interaction.respond(content="Alright. Cancelled uload",ephemeral  = False)
        
        except Exception as e:
            return await ctx.send(e)

def setup(bot):
    bot.add_cog(admins(bot))