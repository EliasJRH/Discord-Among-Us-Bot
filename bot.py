
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def silence_all(ctx):
    await ctx.send('Hush child')

@client.command(aliases=['sus', 'ws'])
async def whosus(ctx):
    colors = ['Red', 'Blue', 'Green', 'Pink', 'Orange',
              'Yellow', 'Black', 'White', 'Purple', 'Brown',
              'Cyan', 'Lime', 'Tan']
    await ctx.send(f'{random.choice(colors)} sus')

@client.command(aliases=['d', 'shush'])
@commands.has_role('sus')
async def deafen(ctx):
    command_origin = ctx.author.voice.channel.id
    channel_to_deafen = client.get_channel(command_origin)
    members = channel_to_deafen.members
    for member in members:
        if (not member.voice.deaf or not member.voice.self_deaf):
            await member.edit(deafen=True)

@client.command(aliases=['ud'])
@commands.has_role('sus')
async def undeafen(ctx):
    command_origin = ctx.author.voice.channel.id
    channel_to_deafen = client.get_channel(command_origin)
    members = channel_to_deafen.members
    for member in members:
        if (member.voice.deaf or member.voice.self_deaf):
            await member.edit(deafen=False)


client.run('NzU5MTY2NDYxOTcyMzE2MTgx.X25i3Q.7Pt2M56HlVDgVyHItpFL3vVPLMc')