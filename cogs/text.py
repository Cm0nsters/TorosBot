import discord
from discord.ext import commands

class Text(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reply(self, ctx, *, arg=None):
        if arg == None:
            await ctx.send("Nothing to reply with!")
        else:
            await ctx.send(arg)

    @commands.command()
    async def say(self, ctx, *, arg=None):
        if arg == None:
            await ctx.send("Nothing to say!")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(arg)

    @commands.command()
    async def tts(self, ctx, *,arg=None):
        if arg == None:
            await ctx.send("Nothing to say!")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(arg,tts=True)

def setup(client):
    client.add_cog(Text(client))