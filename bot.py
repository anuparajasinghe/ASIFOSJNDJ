import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import random
import time
import datetime
import io

bot = discord.Client()
bot_prefix= "<"
bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")

#startup_extensions = ['cogs.info','cogs.other','cogs.mod']
@bot.event
async def on_message(message):
        if message.author.bot:
            return
 
        elif message.content.startswith("<tell"):
            if message.author.id == "429118689367949322":
                text = message.content[len('<tell'):].strip()
                if "efnejifn" in text:
                    return
                elif "discord." in text:
                    return
                elif "@here" in text:
                    return
                elif "@everyone" in text:
                    return
                else:
                    await bot.send_message(message.channel ,"{}".format(text))
                    await bot.delete_message(message)
            else:
                return

        await bot.process_commands(message)




@bot.event
async def on_command_error(error, ctx):
    channelid = bot.get_channel("564325241657229313")
    if isinstance(error, commands.BadArgument):
        await bot.send_message(ctx.message.channel," :x: Bad Argument")
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        return

@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Users: {}".format(len(set(bot.get_all_members()))))
    await bot.change_presence(game=discord.Game(name="the AnimatedStick".format(len(set(bot.get_all_members()))),type=3))

@bot.command(pass_context = True)
async def ping(ctx):
    pingtime = time.time()
    embed=discord.Embed(description="**Pong !**")
    pingms = await bot.send_message(ctx.message.channel, embed=embed)
    await asyncio.sleep(2)
    ping = (time.time() - pingtime) * 1000
    embed.add_field(name=":ping_pong:", value="It Took Me :-\n**%d Micro Seconds**" % ping , inline=True)
    await bot.edit_message(pingms,embed=embed)

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member = None):
    if not user:
        embed=discord.Embed()
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
        embed=discord.Embed(title="Your Avatar Link", url="{}".format(ctx.message.author.avatar_url))
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
        embed.set_image(url=ctx.message.author.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.server.name),icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)
    else:
        embed=discord.Embed()
        embed.set_author(name="{}".format(user.name), icon_url="{}".format(user.avatar_url))
        embed=discord.Embed(title="{}'s Avatar Link".format(user.name), url="{}".format(user.avatar_url))
        embed.set_author(name="{}".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text="{} | Requested By {}".format(ctx.message.server.name ,ctx.message.author.name) ,icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member = None):
    if user is None:
        embed=discord.Embed(title="{}'s Information".format(ctx.message.author.name), url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="User Name", value=ctx.message.author.name, inline=True)
        embed.add_field(name="User Tag", value="#" + ctx.message.author.discriminator, inline=True)
        embed.add_field(name="User ID", value=ctx.message.author.id, inline=True)
        embed.add_field(name="User Status", value=ctx.message.author.status, inline=True)
        embed.add_field(name="User Top Role", value=ctx.message.author.top_role, inline=True)
        embed.add_field(name="User Mention", value=ctx.message.author.mention, inline=True)
        embed.add_field(name="User Joined On", value=ctx.message.author.joined_at, inline=True)
        embed.set_footer(text="{}".format(ctx.message.server.name) ,icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)

    else:
        embed=discord.Embed(title="{}'s Information".format(user.name), url=user.avatar_url)
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User Name", value=user.name, inline=True)
        embed.add_field(name="User Tag", value="#" + user.discriminator, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="User Status", value=user.status, inline=True)
        embed.add_field(name="User Top Role", value=user.top_role, inline=True)
        embed.add_field(name="User Link", value=user.mention, inline=True)
        embed.add_field(name="User Joined On", value=user.joined_at, inline=True)
        embed.set_footer(text="{}".format(ctx.message.server.name) ,icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    server = ctx.message.server
    embed=discord.Embed(title="Server Information")
    embed.set_author(name=server.name , icon_url=server.icon_url)
    embed.add_field(name="Server Name", value=server.name, inline=True)
    embed.add_field(name="Server ID", value=server.id , inline=True)
    embed.add_field(name="Server Owner", value=server.owner, inline=False)
    embed.add_field(name="Server Region", value=server.region, inline=True)
    embed.add_field(name="Member Count", value=server.member_count, inline=False)
    embed.add_field(name="Creation Date", value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
    embed.set_footer(text="the AnimatedBot" , icon_url=server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def troll(ctx, user: discord.Member = None):
    if user is None:
        await bot.send_message(ctx.message.author,":x: Mention a User to Troll !")

    else:
        await bot.send_message(ctx.message.channel,"**{} WAS BANNED** <:verified:560383768372838400>  ".format(user))
        await bot.delete_message(ctx.message)

bot.run(process.env.BOT_TOKEN)
