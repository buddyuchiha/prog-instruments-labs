import sqlite3
from datetime import datetime
from string import Template

import discord
from discord.ext import commands
import pytz

from config import acces


class Prem(commands.Cog):
    def __init__(self, client):
        """
        Initializes the Prem cog.

        Args:
            client: The client instance.
        """
        self.client = client

    @commands.command()
    async def gold(self, ctx, id: int):
        """
        Grants a gold status to a user for 30 days.

        Args:
            ctx: The context of the command.
            id (int): The guild ID for which to grant the gold status.

        Returns:
            None
        """
        user = ctx.author.id
        if user not in acces:
            return

        def first2(s):
            """Returns the first two characters of a string."""
            return s[:2]

        def end2(s):
            """Returns the substring of a string from the third character."""
            return s[3:]

        def add(id, date):
            """
            Adds a new gold status entry to the database.

            Args:
                id (int): The guild ID.
                date (str): The expiration date for the gold status.

            Returns:
                None
            """
            status = 1
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute(
                    'INSERT INTO gold(guild_id, status, date) '
                    'VALUES("{}", "{}", "{}")'.format(
                        id, status, date
                    )
                )

        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        time = moscow_time.strftime('%d.%m')
        a = time
        b = first2(a)
        c = int(b)
        v = c + 30

        if v > 30:
            v -= 30
            result_day = v
            r = end2(a)
            f = int(r)
            result_month = f + 1
            result = f'0{result_day}.0{result_month}'
        else:
            result = time 

        add(id, result)
        embed = discord.Embed(color=0xFFFAFA)
        embed.description = '👌'
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Handles command errors for the cog.

        Args:
            ctx: The context of the command.
            error: The error raised during command execution.

        Returns:
            None
        """
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='🔔 **Ошибка.**',
                color=0xA52A2A
            )
            embed.description = '**Пропущены** аргументы команды!'
            embed.set_footer(text='Error: 003')
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandOnCooldown):
            i = int(error.retry_after)
            embed = discord.Embed(title='🔔 Ошибка.', color=0xA52A2A)
            embed.description = (
                f'Бот имеет **задержку**, пожалуйста, подождите {i} сек.'
            )
            embed.set_footer(text='Error: 004')
            await ctx.send(embed=embed)


def setup(client):
    """
    Sets up the Prem cog.

    Args:
        client: The client instance.

    Returns:
        None
    """
    client.add_cog(Prem(client))
