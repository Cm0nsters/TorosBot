import discord
from discord.ext import commands
import bs4
from bs4 import BeautifulSoup
import asyncio
from googlesearch import search

class Search(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def search(self,ctx,*,args:str):
        results = []
        searchResult = search(query=args,lang='en',num=3,start=0,stop=3, pause=2)

        for i in searchResult: 
            results.append(i)
        
        await ctx.send(f"Here's the top 3 results found for `{args}`:")

        for j in range(3):
            await ctx.send(f"<{results[j]}>")
            

    @commands.command()
    async def image(self,ctx,*,args:str):
        pass

    #https://stackoverflow.com/questions/35439110/scraping-google-images-with-python3-requests-beautifulsoup

def setup(client):
    client.add_cog(Search(client))