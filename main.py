
import discord
from discord.ext import commands


intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print("Hello BB I'm ready.")
    print("......................")

@client.command()
async def hello(ctx):
    print(ctx.author)
    await ctx.send(f"Hello <@{ctx.author.id}>")

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel  = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send(f"You're not in a voice channel <@{ctx.author.id}>, you fucking idiot.")
@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        channel  = ctx.message.author.voice.channel
        await channel.guild.voice_client.disconnect()
        await ctx.send("Bye Bye.")
    else:
        await ctx.send(f"I'm not in a voice channel <@{ctx.author.id}>, you fucking idiot.")




client.run('')