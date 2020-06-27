import discord
from discord.ext import commands

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    defaultGame = '^help'
    defaultStreamURL = "https://twitch.tv/Cm0nsters"
    currentStreamURL = defaultStreamURL

    #Rewrite commands to be grouped under gamestate()
    #Fix issue of "Command raised an exception: AttributeError: 'Status' object has no attribute 'ws'"

    @commands.group()
    @commands.is_owner()
    async def botstate(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid subcommand! Try `^help botstate`")

    #edit to readd status on state change
    @botstate.command()
    async def state(self, ctx, arg):
        if arg == "online":
            await self.client.change_presence(status=discord.Status.online)
            await ctx.send("State set to `Online`")
        elif arg == "idle":
            await self.client.change_presence(status=discord.Status.idle)
            await ctx.send("State set to `Idle`")
        elif arg == "dnd":
            await self.client.change_presence(status=discord.Status.do_not_disturb)
            await ctx.send("State set to `Do Not Disturb`")
        elif arg == "invisible" or arg == "offline":
            await self.client.change_presence(status=discord.Status.offline)
            await ctx.send("State set to `Invisible/Offline`")
        else:
            await ctx.send("Invalid state!")

    @botstate.command()
    async def status(self, ctx, arg):
        await self.client.change_presence(activity=discord.Game(name=arg))
        await ctx.send("Status is now `%s`" % arg)

    @commands.command()
    @commands.is_owner()
    async def streamurl(self, ctx, arg=None):
        global currentStreamURL
        if arg != None:
            if arg[:7]=="http://" or arg[:8]=="https://":
                currentStreamURL = arg
                await ctx.send("Toros will now use `%s` when set to streaming" % currentStreamURL)
            #logging.info('Bot stream URL set to `%s`' % currentStreamURL)
            else:
            #logging.error("Invalid URL of `%s`" % arg)
                await ctx.send("Please use a valid URL!")
        else:
        #logging.error("URL not specified")
            await ctx.send("Please specify a stream URL!")

def setup(client):
    client.add_cog(Status(client))