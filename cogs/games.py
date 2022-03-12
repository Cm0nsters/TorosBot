import discord
from discord.ext import commands
import random
import asyncio

#Convert %s to f strings

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.coinSides = ['heads','tails']
        self.slotChoices = ['\U0001F352','\U0001F347','\U0001F34A','\U0001F34B','\U0001F34F']

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
        machineRows = await self.generatemachine()
        responsesWin = ["Lucky Spin!","Congrats!","Well Done!"]
        msg = await ctx.send("Please Wait...")
        for i in range(5):
            machine = f"```| {machineRows[0][0]} {machineRows[0][1]} {machineRows[0][2]} |\n|={machineRows[1][0]}={machineRows[1][1]}={machineRows[1][2]}=|\n| {machineRows[2][0]} {machineRows[2][1]} {machineRows[2][2]} |```"
            await asyncio.sleep(0.2)
            machineRows = await self.generatemachine()
            await msg.edit(content=machine)

        if machineRows[1][0] == machineRows[1][1] == machineRows[1][2]:
            await ctx.send(random.choice(responsesWin))
        else:
            await ctx.send("Better luck next time...")

    async def generatemachine(self):
        machineRows = [[],[],[]]
        for i in range(3):
            for j in range(3):
                machineRows[i].append(random.choice(self.slotChoices))

        return machineRows

def setup(client):
    client.add_cog(Games(client))