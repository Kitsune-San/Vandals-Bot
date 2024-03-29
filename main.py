import discord
from discord.ext import commands, tasks
from datetime import datetime
import json
import utilities
import assets
import argparse


dev_mode = True

parser = argparse.ArgumentParser(description="Run bot in dev mode")
parser.add_argument("--dev", action="store_true")
args = parser.parse_args()

if args.dev:
    dev_mode = True



start_date = datetime.now()
start_date_pretty =  start_date.strftime("%d/%m/%Y %H:%M:%S")
print("Bot started on: " + start_date_pretty + "\n")


#Function for prefix

def get_prefix(bot, message):
    prefixes = utilities.get_json(assets.prefix_file)
    return prefixes[str(message.guild.id)]


intents = discord.Intents.default()
intents.members=True
intents.guilds = True
bot = commands.Bot(command_prefix="vdev!", case_insenstive=True, intents = intents)

#removing default ping and help command
bot.remove_command("ping")
bot.remove_command("help")



if __name__ == "__main__":
    for extension in assets.extensions:
        bot.load_extension(extension)







@bot.event
async def on_guild_join(guild):
    global bot
    prefixes = utilities.get_json(assets.prefix_file)
    prefixes[str(guild.id)] = "v!"

    utilities.write_json(assets.prefix_file, prefixes)


# Removes the prefix for that server when the bot gets removed, kicked or banned.
@bot.event
async def on_guild_remove(guild):
    prefixes = utilities.get_json(assets.prefix_file)
    prefixes.pop(str(guild.id))

    utilities.write_json(assets.prefix_file, prefixes)



@bot.event
async def on_ready():
    config = utilities.get_json(assets.config_file)
    print(config["invite_url"])



@bot.command(name="prefix")
@commands.has_permissions(add_reactions=True)
async def prefix(ctx, _prefix=None):
    if _prefix is not None:
        prefixes = utilities.get_json(assets.prefix_file)
        prefixes[str(ctx.guild.id)] = _prefix

        utilities.write_json(assets.prefix_file, prefixes)
        await ctx.send(embed=utilities.create_simple_embed("Prefix", discord.Color.red(), "Prefix set!", f"Success! This guild's prefix is now {_prefix}"))
    else:
        # no need to load json, as this command was called with the adequate prefix
        await ctx.send(embed=utilities.create_simple_embed("Current prefix", discord.Color.red(), "Your current prefix is: ", ctx.prefix))










config = utilities.get_json(assets.config_file)
token = " "

if dev_mode:
    token = config['devtoken']
    print("Starting bot in dev mode\n")
else:
    token = config['token']
    print("Starting bot in live mode!\n")


bot.run(token)


