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

        elif message.content.startswith ("<8ball"):
            await bot.send_message(message.channel, random.choice([":8ball: | **{},** It is Certain ".format(message.author.name),
                                                                  ":8ball: | **{},** It is Decidedly, So ?".format(message.author.name),
                                                                  ":8ball: | **{},** Without a doubt ".format(message.author.name),
                                                                  ":8ball: | **{},** Yes, definitely  ".format(message.author.name),
                                                                  ":8ball: | **{},** You may rely on it ".format(message.author.name),
                                                                  ":8ball: | **{},** As I see it, yes  ".format(message.author.name),
                                                                  ":8ball: | **{},** Most likely  ".format(message.author.name),
                                                                  ":8ball: | **{},** Outlook Looks Good  ".format(message.author.name),
                                                                  ":8ball: | **{},** Yes Bro ".format(message.author.name),
                                                                  ":8ball: | **{},** Signs point to yes ".format(message.author.name),
                                                                  ":8ball: | **{},** Reply lazy try again ".format(message.author.name),
                                                                  ":8ball: | **{},** Ask again later ".format(message.author.name),
                                                                  ":8ball: | **{},** Better not tell you now ".format(message.author.name),
                                                                  ":8ball: | **{},** Cannot predict now ".format(message.author.name),
                                                                  ":8ball: | **{},** Concentrate and ask again ".format(message.author.name),
                                                                  ":8ball: | **{},** Don't count on it  ".format(message.author.name),
                                                                  ":8ball: | **{},** My reply is no ".format(message.author.name),
                                                                  ":8ball: | **{},** My sources say no ".format(message.author.name),
                                                                  ":8ball: | **{},** Outlook is Not So Good  ".format(message.author.name),
                                                                  ":8ball: | **{},** Very doubtful  ".format(message.author.name)]))

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
    await bot.change_presence(game=discord.Game(name="tAS Videos ".format(len(set(bot.get_all_members()))),type=3))

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

@bot.command(pass_context=True)
async def lovecal(ctx , user: discord.Member = None):
    if user is None:
        await bot.say(":x: Mention a User to Check The Love Percenatge")
    if user.id == ctx.message.author.id:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name=":heart: Love Calculator",value="Love Percentage between {} and {}\n **0%**".format(ctx.message.author.mention , user.mention), inline=False)
        await bot.send_message(ctx.message.channel,embed=embed)
    else:
        embed=discord.Embed(color=0xff0000)
        embed.add_field(name=":heart: Love Calculator", value="Love Percentage between {} and {}\n **{}%**".format(ctx.message.author.mention , user.mention , random.randint(1,100)), inline=False)
        await bot.send_message(ctx.message.channel,embed=embed)


@bot.command(pass_context=True)
async def link(ctx):
    embed=discord.Embed(title="Subscribe to Ma Boss!!", url="https://www.youtube.com/channel/UC0bZpIWLn_YEjkyTyvAadtQ?view_as=subscriber")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/557874110944903178/564336911293087744/social-media-and-marketing.png")
    embed.set_author(name="the AnimatedStick", icon_url="https://images-ext-1.discordapp.net/external/QTCOBVY3LPk9lQtkaKJwJ7KbSqwYakN8IMGkqs0OqdQ/https/cdn.discordapp.com/icons/554641659888140308/c38ea2979140e6b1a8f8ea30473ac7bf.jpg")
    embed.add_field(name="Discord Server", value="[Click](http://bit.ly/tASDiscord)", inline=False)
    embed.add_field(name="YouTube Channel", value="[Click](http://bit.ly/tASYouTUBE)", inline=False)
    embed.add_field(name="Twitter", value="[Click](http://bit.ly/tASTwitter)", inline=False)
    embed.add_field(name="Instagram", value="Soon!", inline=False)
    embed.set_footer(text="the AnimatedBot" , icon_url="https://images-ext-1.discordapp.net/external/QTCOBVY3LPk9lQtkaKJwJ7KbSqwYakN8IMGkqs0OqdQ/https/cdn.discordapp.com/icons/554641659888140308/c38ea2979140e6b1a8f8ea30473ac7bf.jpg")
    await bot.say(embed=embed)


bot.run(process.env.BOT_TOKEN)
