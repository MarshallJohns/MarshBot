
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
    print(ctx.author.global_name)
    await ctx.send(f"Hello @{ctx.author.name}")



client.run('MTIxNTc5MzQ4NDkxMzU3ODEyNg.GWKkPj.n-X32WjVT9YsjmOuL4jBnGGxebjhJx_NFtSTZg')