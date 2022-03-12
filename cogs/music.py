import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import asyncio

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = asyncio.Queue()
        self.play_next = asyncio.Event()

        self.ytdl_opts={
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

    #def join(self, ctx):
    #    global voice
    #    channel = ctx.message.author.voice.channel
    #    voice = get(self.client.voice_clients, guild=ctx.guild)

    #    if voice and voice.is_connected():
    #        await voice.move_to(channel)
    #    else:
    #        voice = await channel.connect()

#    def leave(self, ctx):
#        voice = get(self.client.voice_clients, guild=ctx.guild)

#        if voice and voice.is_connected():
#            await voice.disconnect()

    #Player Functions (https://stackoverflow.com/questions/53605422/discord-py-music-bot-how-to-combine-a-play-and-queue-command)

    async def player(self=None):
        while True:
            self.play_next.clear()
            current = await self.queue.get()
            current.start()
            await self.play_next.wait()

    def toggle_next(self):
        self.client.loop.call(self.play_next.set)

    @commands.command(aliases=['p'])
    async def play(self, ctx, url):
        if not self.client.is_voice_connected(ctx.message.server):
            voice = await self.client.join_voice_channel(ctx.message.author.voice_channel)
        else:
            voice = self.client.voice_client_in(ctx.message.server)

        player = await voice.create_ytdl_player(url, after=self.toggle_next)
        await self.queue.put(player)







    #@commands.is_owner()
    #@commands.command(aliases=['p'])
    #async def play(self, ctx, url):
    #    voice.play(discord.FFmpegPCMAudio(f"song{self.queuePos}.mp3"))

    #add removal of download and queue system
    #@commands.command()
    #async def skip(self, ctx):
    #    pass

def setup(client):
   client.add_cog(Music(client))
   client.loop.create_task(Music.player())