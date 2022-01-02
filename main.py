import discord
from discord.ext import commands
import smtplib
import os

token = "token"

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

import json
try:
    with open('premium.json') as f:
        premium = json.load(f)
except:
    pass

@client.event
async def on_ready():
    print(f"{client.user.name}#{client.user.discriminator} -> Turned on")
    print(f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot -> Invite link")

async def sendembed(ctx,*,content):
    colorx = 0x3498db
    embed=discord.Embed(title=f"-> {ctx.message.author}", color=colorx)
    embed.add_field(name=f"-" * len(content), value=f"{content}", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    ping_ = client.latency
    ping = round(ping_ * 1000)
    await sendembed(ctx=ctx, content=f"My ping is {ping}ms")

import subprocess



@client.command()
async def spam(ctx,sender,threads):
    if ctx.message.author.id in premium['users']:
        x = subprocess.Popen(['python','spammer.py',sender,threads],shell=True)
        await sendembed(ctx=ctx, content=f"Started spamming\nOn: {sender}\nThreads: {threads}")
        x.wait()
    else:
        await sendembed(ctx=ctx, content=f"Failed spamming\nYou are not premium!")

@client.command()
async def stats(ctx):
    total = len(os.listdir('database/'))
    valid = 0
    for gmail in os.listdir('database/'):

        with open("database/" + gmail, 'r', encoding='utf-8') as f:
            password = f.readlines()
            fstep = f'{gmail[:-4]}'
            sender = f"{fstep}@gmail.com"
            for gmail_password in password:
                finalpass = gmail_password
                gmail_user = sender
                try:
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(gmail_user, finalpass)
                        server.close()
                        valid += 1
                except:
                    pass

    await sendembed(ctx=ctx, content=f"Stats for spammer:\n\nTotal: {total}\nValid: {valid}")

@client.command()
async def prem(ctx, way, arg: discord.Member=None):
    if ctx.message.author.id == 774156404897611776:
        if way == "add":
            x = premium["users"]
            x.append(arg.id)
            premium["users"] = x
            await sendembed(ctx=ctx, content=f"Gave premium access for {arg.id}")
            _saveconfig()
        elif way == "view" and arg is None:
            x = premium["users"]
            await sendembed(ctx=ctx, content=f"Premium: {x}")
        else:
            await sendembed(ctx=ctx, content="Way is not correct")
    else:
        await sendembed(ctx=ctx, content="You must be humanot to execute that command")
        
def _saveconfig():
    with open('premium.json', 'w+') as f:
        json.dump(premium, f)

client.run(token)