import discord
from discord.ext import commands
import random

#Convert %s to f strings

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.coinSides = ['heads','tails']
        self.diceList = [1,2,3,4,5,6]
        self.slotList = [1,2,3,4,5]

    #Coin

    @commands.group()
    async def coin(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid subcommand! Try `^help coin`")

    @coin.command()
    async def flip(self, ctx):
        await ctx.send("You flipped: %s" % str(random.choice(self.coinSides)))

    @coin.command(name='predict', aliases=['guess'])
    async def guessflip(self, ctx, guess):
        flip = str(random.choice(self.coinSides))

        if guess == flip:
            await ctx.send(f"The coin flipped {flip}!")
        elif guess != flip:
            await ctx.send(f"The coin flipped {flip}, not {guess}!")
        else:
            await ctx.send("Invalid choice!")

    #Dice

    @commands.group()
    async def dice(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid subcommand! Try `^help dice`")

    @dice.command()
    async def roll(self, ctx):
        await ctx.send(random.randint(1,6))

    @dice.command(name='predict', aliases=['guess'])
    async def guessroll(self, ctx, guess):
        roll = str(random.randint(1,6))

        if guess == roll:
            await ctx.send(f"The dice rolled a {roll}!")
        elif guess != roll:
            await ctx.send(f"The dice rolled a {roll}, not a {guess}!")
        else:
            await ctx.send("Invalid choice!")

    #Slots

    @commands.group()
    async def slots(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid subcommand! Try `^help slots`")

    @slots.command()
    async def pull(self, ctx):
        slotRowM = [random.choice(self.slotList),random.choice(self.slotList),random.choice(self.slotList)]
        slotRowT = [(slotRowM[0]+(await Games.numcheck(self=None,innumber=slotRowM[0],row="top"))),(slotRowM[1]+(await Games.numcheck(self=None,innumber=slotRowM[1],row="top"))),(slotRowM[2]+(await Games.numcheck(self=None,innumber=slotRowM[2],row="top")))]
        slotRowB = [(slotRowM[0]+(await Games.numcheck(self=None,innumber=slotRowM[0],row="bottom"))),(slotRowM[1]+(await Games.numcheck(self=None,innumber=slotRowM[1],row="bottom"))),(slotRowM[2]+(await Games.numcheck(self=None,innumber=slotRowM[2],row="bottom")))]
        responsesWin = ["Lucky Spin!","Congrats!","Well Done!"]
        await ctx.send(f"```|   {slotRowT[0]} {slotRowT[1]} {slotRowT[2]}   |\n|-- {slotRowM[0]} {slotRowM[1]} {slotRowM[2]} --|\n|   {slotRowB[0]} {slotRowB[1]} {slotRowB[2]}   |```")

        if slotRowM[0] == slotRowM[1]:
            if slotRowM[1] == slotRowM[2]:
                await ctx.send(random.choice(responsesWin))
            else:
                await ctx.send("Better luck next time...")
        else:
            await ctx.send("Better luck next time...")

    async def numcheck(self,innumber,row):
        num = int(innumber)
        rowPick = str(row)
        if rowPick == "top":
            if num == 1:
                return 4
            elif num == 5:
                return -1
            else:
                return -1
        elif rowPick == "bottom":
            if num == 1:
                return 1
            elif num == 5:
                return -4
            else:
                return 1

def setup(client):
    client.add_cog(Games(client))