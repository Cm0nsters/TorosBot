import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        #Fix download options
        self.ytdl_opts = {
            'outtmpl' : './song.%(ext)s',
            'audio-format' : 'mp3',
            'extract-audio' : True,
            'format' : 'worst',
        }

    @commands.command()
    async def join(self, ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()

    @commands.is_owner()
    @commands.command(aliases=['p'])
    async def play(self, ctx, url):
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        with youtube_dl.YoutubeDL(self.ytdl_opts) as ydl:
            ydl.download([url])

        voice.play(discord.FFmpegPCMAudio("song.mp4"))

        #add removal of download and queue system
    @commands.command()
    async def skip(self, ctx):
        if voice and voice.is_connected():
            os.remove('song.mp4')
        else:
            pass

def setup(client):
    client.add_cog(Music(client))