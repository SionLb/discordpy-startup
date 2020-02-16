from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def say_hello(ctx):
    await ctx.send('よー。お疲れ！')
    
@bot.command()
async def kick(ctx):
    await ctx.send('ほらほらこんなとこで長居すんなよ')

@bot.command()
async def bye(ctx):
    await ctx.send('また来いよな')

bot.run(token)
