import discord
from discord.ext import commands
import asyncio
import time
import sys
import os
import platform

try:
    from dotenv import load_dotenv
    load_dotenv("./.env")
except:
    print("Unable to load dotenv")

#Prefix

client = commands.Bot(command_prefix='^',owner_id=int(os.getenv('OWNER_ID')))

#Bot Online

@client.event
async def on_ready():
    print(f"Discord.py version: {discord.__version__}")
    print(f'Bot {client.user} is online!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=defaultGame))

def osCheck(system=platform.system()):
    if system == "Windows":
        opsys = "|| Dev Release"
        return opsys
    elif system == "Linux":
        return ""

defaultGame = f'^help {osCheck()}'

#Cogs Load

for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Commands

#Command Fail

@client.event
async def on_command_error(ctx,error):
    print(error)
    return await ctx.send(f"Uh-oh! Try using `^help`, or contact `Cm0nsters#6514` for assistance with the following:\n```{error}```")

#User Commands

@client.command()
async def hug(ctx,arg=None):
    if arg == None:
        await ctx.send(f"*virtually hugs {ctx.message.author.mention} back*")
    else:
        await ctx.send(f"*{ctx.message.author.mention} virtually hugs {arg}*")

#Admin Commands

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name='Shutting Down...'))
    await ctx.send("Shutting down...")
    print("Bot was shutdown")
    sys.exit()

@client.command(aliases=['reboot'])
@commands.is_owner()
async def restart(ctx):
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='Restarting...'))
    await ctx.send("Restarting...")
    print("Bot was restarted")
    python = sys.executable
    os.execl(python, python, * sys.argv)
    #REQUIRES POSSIBLE FIX

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog `{extension}` has been loaded!")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Cog `{extension}` has been unloaded!" % extension)

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog `{extension}` has been reloaded!")

#Token

client.run(os.getenv('TOKEN'))