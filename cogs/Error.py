import discord
from discord.ext import commands

class Error(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(name="Error", description=f"{ctx.author.mention} you are missing required argument(s)")
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(name="Error", description=f"{ctx.author.mention} you are missing required permissions!")
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(name="Error", description=f"{ctx.author.mention} bad argument!")
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(name="Error", description=f"{ctx.author.mention} command not found!")
        else:
            embed = discord.Embed(name="Error", description=f"{ctx.author.mention} unknown error!")
        return await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Error(client))