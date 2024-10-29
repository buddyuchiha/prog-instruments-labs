import asyncio
import discord
from discord.ext import commands


from config import prefix


class Help(commands.Cog):
    def __init__(self, client):
        """
        Initializes the Help cog.

        Args:
            client: The client instance.
        """
        self.client = client

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def help(self, ctx):
        """
        Displays a help message with available commands.

        Args:
            ctx: The context of the command.

        Returns:
            None
        """
        emb = discord.Embed(
            title=':clipboard: Навигация по командам.',
            color=0xFFFAFA
        )
        emb.add_field(
            name=f"`{prefix}meme`", 
            value="- рандомный мем.", 
            inline=False
        )
        emb.add_field(
            name=f"`{prefix}automemes <id канала>`",
            value="- подключение автопубликации на канал.",
            inline=False
        )
        emb.add_field(
            name=f"`{prefix}gs`",
            value="- информация о золотом сервере.",
            inline=False
        )
        emb.add_field(
            name=f"`{prefix}piar`", 
            value="- информация о заказе рекламы.",
            inline=False
        )
        emb.add_field(
            name=f"`{prefix}about`",
            value="- информация о боте.",
            inline=False
        )
        emb.add_field(
            name=f"`{prefix}idea`",
            value="- отправка идеи на тех. сервер.",
            inline=False
        )
        emb.add_field(
            name=f"`{prefix}bag`",
            value="- отправка бага на тех. сервер.",
            inline=False
        )
        emb.add_field(
            name=f"`{prefix}invite`", 
            value="- инвайт на бота и тех. сервер.", 
            inline=False
        )
        emb.set_footer(
            text='Пригласи меня к себе на сервер m!invite'
        )
        await ctx.send(embed=emb)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def about(self, ctx):
        """
        Displays information about the bot.

        Args:
            ctx: The context of the command.

        Returns:
            None
        """
        guild_count = len(self.client.guilds)
        embed = discord.Embed(
            title="**Internet Memes Info**",
            color=0xFFFAFA
        )
        embed.set_thumbnail(
            url=self.client.user.avatar_url
        )
        embed.add_field(
            name="Создатель:", 
            value="`ванильныйчекист#3775`",
            inline=False
        )
        embed.add_field(
            name="Сервера:",
            value='`{}`'.format(guild_count),
            inline=False
        )
        embed.add_field(
            name="Каналов:",
            value='`{}`'.format(len(list(self.client.get_all_channels()))),
            inline=False
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite(self, ctx):
        """
        Provides an invite link for the bot and the support server.

        Args:
            ctx: The context of the command.

        Returns:
            None
        """
        emb = discord.Embed(
            title='📢 Пригласи бота к себе на сервер!',
            color=0xFFFAFA
        )
        emb.add_field(
            name='Инвайт ссылка на бота:',
            value='[Пригласить бота (кликабельно)]\
                (https://discord.com/oauth2/authorize?client_id=\
                    773895453494214676&permissions=1074134088&scope=bot)',
            inline=False
        )
        emb.add_field(
            name='Сервер тех. поддержки бота:', 
            value='[Сервер тех. поддержки (кликабельно)]\
                (https://discord.gg/8BnEfUq99j)'
        )
        await ctx.send(embed=emb)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gs(self, ctx):
        """
        Displays information about the gold server benefits.

        Args:
            ctx: The context of the command.

        Returns:
            None
        """
        emb = discord.Embed(color=0xFFD700)
        emb.description = (
            f'**Подключи возможности золотого сервера!**\n```'
            '1. Мемы без рекламы!```\n```'
            '2. Кастом роль на тех. сервере!```\n'
            '[Приобрести премиум/заказать рекламу в мемах (кликабельно)]'
            '(https://discord.gg/8BnEfUq99j) '
        )
        await ctx.send(embed=emb)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def piar(self, ctx):
        """
        Displays information on how to order advertising for content.

        Args:
            ctx: The context of the command.

        Returns:
            None
        """
        emb = discord.Embed(color=0xFFFAFA)
        emb.description = (
            f'**Закажи рекламу своего контента!**\n `Более 2.000 серверов`\n'
            'Для заказа рекламы перейдите на наш тех. сервер.' 
            '[Тех. сервер (кликабельно)](https://discord.gg/8BnEfUq99j)'
        )
        await ctx.send(embed=emb)


def setup(client):
    """
    Sets up the Help cog.

    Args:
        client: The client instance.

    Returns:
        None
    """
    client.add_cog(Help(client))
