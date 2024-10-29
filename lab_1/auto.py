import asyncio
import json
import random
import sqlite3
from datetime import datetime
from string import Template

import discord
from discord.ext import commands
import pytz

from config import piar


url = []
with open('url.json', 'r') as f: 
    url = json.load(f)
timeout = 60 * 60


class Auto(commands.Cog):
    def __init__(self, client):
        """
        Initializes the Auto class.

        Args:
            client (discord.Client): The Discord client instance.
        """
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):    
        """Called when the bot is ready."""
        channels_m = [] 
        check_m = [] 

        def check_meme(channels_m):
            """
            Checks and retrieves the list of meme channels from the database.

            Args:
                channels_m (list): List to store meme channels.
            """
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute('SELECT meme FROM auto')
                for result in cur:
                    channels_m.append(result[0])
                return channels_m
        
        def check_time(time):
            """
            Checks the database for the existence of a record.

            Args:
                time (str): The date in 'dd.mm' format.

            Returns:
                str or None: The date if found, otherwise None.
            """
            a = None
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute(
                    'SELECT date FROM gold WHERE date = "{}"'.format(
                        time
                    )
                )
                for result in cur:
                    a = result[0]
                return a

        def get_server(time):
            """
            Retrieves the server ID associated with the given date.

            Args:
                time (str): The date in 'dd.mm' format.

            Returns:
                str or None: The server ID if found, otherwise None.
            """
            a = None
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute(
                    'SELECT guild_id FROM gold WHERE date = "{}"'.format(
                        time
                    )
                )
                for result in cur:
                    a = result[0]
                return a

        def check_gold(guild):
            """
            Checks the status of the guild in the database.

            Args:
                guild (str): The guild ID to check.

            Returns:
                str or None: The status if found, otherwise None.
            """
            a = None
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute(
                    'SELECT status FROM gold WHERE channel_id = "{}"'.format(
                        guild
                    )
                )
                for result in cur:
                    a = result[0]
                return a

        def delete(time, delete):
            """
            Deletes a record from the gold table based on the given date.

            Args:
                time (str): The date record to delete.
                delete (str): The value to delete.
            """
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute(
                    'DELETE from gold where date= "{}"'.format(
                        time
                    )
                )

        def prem():
            """Checks and removes records from the gold table."""
            moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
            time = moscow_time.strftime('%d.%m')
            result = check_time(time)
            
            if result is not None:
                delete_result = get_server(time)
                delete(time, delete_result)


        await self.client.change_presence(
            activity=discord.Game('m!meme | m!help')
        )
        channels_mem = check_meme(channels_m)
        chance = [1, 2]
        
        while True:
            prem()
            meme = url["meme"]
            check_m = check_meme(check_m)
            
            for element in check_m:
                if element not in channels_mem:
                    channels_mem.append(element)
                    
            for channel_id in channels_mem:
                await self.client.wait_until_ready()
                try:
                    channel = self.client.get_channel(int(channel_id))
                except:
                    pass
                
                result_gold = check_gold(channel_id)
                result_chance = random.choice(chance)
                result_piar = random.choice(piar)
                result_meme = random.choice(meme)
                ran = result_meme
                emb = discord.Embed(
                    title='**Auto memes**', color=0xFFFAFA
                )
                emb.set_image(url=ran)
                
                if result_chance == 1 and result_gold != 1:
                    emb.set_footer(text=f'{result_piar}')
                try:
                    await channel.send(embed=emb)
                except:
                    pass
            await asyncio.sleep(timeout)
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def meme(self, ctx):
        """
        Command to send a random meme in the current channel.

        Args:
            ctx (commands.Context): The context in which command is invoked.
        """
        def check_gold(guild):
            """Checks the status of the guild."""
            a = None
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute(
                    'SELECT status FROM gold WHERE guild_id = "{}"'.format(
                        guild
                    )
                )
                for result in cur:
                    a = result[0]
                return a
            
        result_gold = check_gold(ctx.message.guild.id)
        chance = [1, 2]
        result_chance = random.choice(chance)
        result_piar = random.choice(piar)
        meme = url["meme"]
        result_meme = random.choice(meme)
        emb = discord.Embed(title='**Memes**', color=0xFFFAFA)
        emb.set_image(url=result_meme)
        
        if result_chance == 1 and result_gold != 1:
            emb.set_footer(text=f'{result_piar}')
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def automemes(self, ctx, arg):
        """
        Command to set up automatic meme posting in a specified channel.

        Args:
            ctx (commands.Context): The context in which command is invoked.
            arg (str): The channel ID where memes will be posted.
        """
        def add(arg):
            """Adds a new channel for automatic meme posting."""
            with sqlite3.connect('base.db') as bd:
                guild_id = ctx.message.guild.id
                user = ctx.message.author.id
                moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
                date = moscow_time.strftime('%d.%m.%y | %H:%M')
                cur = bd.cursor()
                cur.execute(
                    'INSERT INTO auto(guild_id, user_id, meme, date)'
                    'VALUES("{}", "{}", "{}", "{}")'.format(
                        guild_id, user, arg, date
                    )
                )

        def change(arg):
            """Changes the channel for automatic meme posting."""
            with sqlite3.connect('base.db') as bd:
                guild_id = ctx.message.guild.id
                cur = bd.cursor()
                cur.execute(
                    'UPDATE auto SET meme = {} WHERE guild_id = {}'.format(
                        arg, guild_id
                    )
                )

        status = None
        
        def check(arg, status):
            """
            Checks the database for an existing meme channel.

            Args:
                arg (str): The channel ID to check.
                status (None): A placeholder for status.

            Returns:
                str or None: The existing meme channel found, otherwise None.
            """
            guild_id = ctx.message.guild.id
            with sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute(
                    'SELECT meme FROM auto WHERE guild_id = {}'.format(
                        guild_id
                    )
                ) 
                for result in cur:
                    status = result[0]
                return status
            
        result_meme = check(arg, status)

        members = ctx.guild.member_count
        hentai_list = [None, 'None']

        if len(arg) < 18:
            embed = discord.Embed(title='🔔 Ошибка.', color=0xA52A2A)
            embed.description = 'Вы ввели **некоректный** id канала.'
            embed.set_footer(text='Error: 005')
            await ctx.send(embed=embed)
            return
        elif not arg.isdigit():
            embed = discord.Embed(title='🔔 Ошибка.', color=0xA52A2A)
            embed.description = 'Вы ввели **некоректный** id канала.'
            embed.set_footer(text='Error: 005')
            await ctx.send(embed=embed)
            return
        elif members > 15:
            if result_meme in hentai_list:
                add(arg)
            else:
                change(arg)
            embed = discord.Embed(title='✅ Успешно.', color=0xFFFAFA)
            embed.description = (
                f'Автопубликация **успешна подключена**'
                f'участником {ctx.message.author.mention} на канал `{arg}`.'
            )
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title='🔔 Ошибка.', color=0xFFFAFA)
            embed.description = (
                'Для **подключения** автопубликации на вашем сервере должно'
                'быть **более 15 участников** или вы можете оформить' 
                '**золотой сервер** к автопубликации на нашем тех. сервере.'
                '[Оформить подписку (кликабельно)]'
                '(https://discord.gg/8BnEfUq99j).'
            )
            embed.set_footer(text='Error: 005')
            await ctx.send(embed=embed)
            return


def setup(client):
    """
    Sets up the Auto cog in the client.

    Args:
        client (discord.Client): The Discord client instance.
    """
    client.add_cog(Auto(client))
