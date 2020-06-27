import discord
from discord.ext import commands
import string
import random

class Media(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def image(self,ctx):

        await ctx.send("Sorry, but this command currently does not work!")

        #LOOK AT: https://github.com/Joeclinton1/google-images-download
        #LOOK AT: https://stackoverflow.com/questions/60370799/google-image-download-with-python-cannot-download-images

        #await ctx.send("Searching for: %s" % search)
        #photoname = await Toros.search.media.image(search=search)
        #picture = "/downloads/"+search +"/1."+photoname
        #pictureLoc = str(os.getcwd() + picture)
        #print(pictureLoc)
        #await ctx.send(file=discord.File(pictureLoc))
        #shutil.rmtree("./downloads")

    @commands.command()
    async def randomyt(self,ctx):
        await ctx.send("Creating random YouTube URL...")
        fullURL = "https://www.youtube.com/watch?v="+ "".join(await self.youtube())
        await ctx.send("Heres your random URL (THIS URL MAY NOT WORK) " + "\n"+ fullURL)

    async def youtube(self):
        urlEndCreate = []
        charset = list(string.ascii_letters)+list(string.digits)+list("-")+list("_")
        for i in range(11):
            urlEndCreate.insert(i, random.choice(charset))

        return urlEndCreate    

def setup(client):
    client.add_cog(Media(client))