import discord
from discord.ext import commands

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.defaultGame = '^help'
        self.currentGame = self.defaultGame
        self.defaultStreamURL = "https://twitch.tv/Cm0nsters"
        self.currentStreamURL = self.defaultStreamURL

    #Rewrite commands to be grouped under gamestate()
    
    @commands.group()
    @commands.is_owner()
    async def botstate(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid subcommand! Try `^help botstate`")

    #edit to read status on state change
    @botstate.command()
    async def state(self, ctx, arg):
        if arg == "online":
            await self.client.change_presence(status=discord.Status.online,activity=discord.Game(name=self.currentGame))
            await ctx.send("State set to `Online`")
        elif arg == "idle":
            await self.client.change_presence(status=discord.Status.idle,activity=discord.Game(name=self.currentGame))
            await ctx.send("State set to `Idle`")
        elif arg == "dnd":
            await self.client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game(name=self.currentGame))
            await ctx.send("State set to `Do Not Disturb`")
        elif arg == "invisible" or arg == "offline":
            await self.client.change_presence(status=discord.Status.offline,activity=discord.Game(name=self.currentGame))
            await ctx.send("State set to `Invisible/Offline`")
        else:
            await ctx.send("Invalid state!")

    @botstate.command()
    async def status(self, ctx, arg):
        self.currentGame = arg
        await self.client.change_presence(activity=discord.Game(name=arg))
        await ctx.send(f"Status is now `{arg}`")

    @botstate.command()
    @commands.is_owner()
    async def streamurl(self, ctx, arg=None):
        if arg != None:
            if arg[:7]=="http://" or arg[:8]=="https://":
                self.currentStreamURL = arg
                await ctx.send(f"Toros will now use `{self.currentStreamURL}` when set to streaming")
            else:
                await ctx.send("Please use a valid URL!")
        else:
            await ctx.send("Please specify a stream URL!")

def setup(client):
    client.add_cog(Status(client))