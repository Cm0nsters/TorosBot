import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = []
        self.queuePos = 1

        self.ytdl_opts={
            'outtmpl': f'./song{self.queuePos}.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
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
        self.queue.append(f"song{self.queuePos}.mp3")
        self.ytdl_opts.update({'outtmpl': f'./song{self.queuePos}.%(ext)s'})
        
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        with youtube_dl.YoutubeDL(self.ytdl_opts) as ydl:
            #ydl.download([url])
            songMeta = ydl.extract_info(url,download=True)
            print(songMeta['duration'])

        if voice.is_playing():
            pass
        else:
            voice.play(discord.FFmpegPCMAudio(f"song{self.queuePos}.mp3"))

        #add removal of download and queue system
    @commands.command()
    async def skip(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            self.queue.remove(f'song{self.queuePos}.mp3')
            os.remove(f'song{self.queuePos}.mp3')
            self.queuePos += 1
        else:
            pass

def setup(client):
    client.add_cog(Music(client))