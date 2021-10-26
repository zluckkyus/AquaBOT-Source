# PACOTES
import discord
import random
import contextlib
import io
import discord, time
import datetime
import pyfiglet
import os
from dotenv import load_dotenv
import json
import asyncio
from asyncio import sleep, gather
from keep_alive import keep_alive
from asyncio import sleep
from discord.utils import get
from discord import Webhook, AsyncWebhookAdapter
from discord_webhook import DiscordWebhook
import aiohttp
from discord.ext import commands
import inspect
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure, when_mentioned_or, AutoShardedBot, CommandNotFound

from PIL import Image
from io import BytesIO
from aiohttp import ClientSession

m = {}




# MODULO
modulos = ["cogs.comando"]
start_time = time.time()

# Modulo Warning
with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

# PREFIXO
def get_prefix(client,message):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command("help")

# SHOP
mainshop = [{"name":"Relogio","price":100,"description":"Veja a hora"},{"name":"Laptop","price":1900,"description":"Trabalhar!"},{"name":"Vip","price":100000,"description":"O Dono do servidor, lhe dará beneficios! ao comprar peça para ele lhe setar o cargo!!"}]


# EVENTO bot
async def status():
	while True:
		await bot.wait_until_ready()
		await bot.change_presence(activity=discord.Game(name="Aqua BOT"))
		await sleep(5)
		await bot.change_presence(
		    activity=discord.Game(name="Criador @! ๖ۣۜζ͜͡$rLuckkyz.py 🐊#2006"))
		await sleep(5)
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.watching,
		        name=f"{len(bot.guilds)} | Servidores"))
		await sleep(5)
		await bot.change_presence(
		    activity=discord.Activity(
		        type=discord.ActivityType.watching,
		        name=f"{len(bot.users)} | Membros!"))
		await sleep(5)

@bot.event
async def on_ready():
	print(f"{bot.user} Está online!\nServidores {len(bot.guilds)}\nMembros {len(bot.users)}")
bot.loop.create_task(status())


# COMANDOS INVISIVEIS
@bot.command()
async def help(ctx):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
    
  pre = prefixes[str(ctx.guild.id)] 

  embed=discord.Embed(title="", description=f"<:zencool:779774350731640892> Olá {ctx.author.mention} aqui estão as Categorias de comandos! Espero que goste.", color=0x00fbff)
  embed.set_thumbnail(url=f"{bot.user.avatar_url}")
  embed.set_author(name="Painel de Comandos - AquaBOT", icon_url="https://cdn.discordapp.com/avatars/775027437695664160/02ff31c667ab610686a49195a809909e.webp?size=1024")
  embed.add_field(name="<a:01_171:779776412122742795> **Categoria de Comandos Randoms**", value=f"`{pre}categoria-random`")
  embed.add_field(name="<a:02_171:779776343767384074> **Categoria de Comandos Administrador**", value=f"`{pre}categoria-adm`")
  embed.add_field(name="<a:03_171:779776373219655731> **Categoria de Comandos Diversão**", value=f"`{pre}categoria-fun`")
  embed.add_field(name="<a:04_171:779779063002562560> **Categoria de Comandos Economia**", value=f"`{pre}categoria-economia`")
  embed.add_field(name="<a:05_171:779779557988368384> **Categoria de Comandos Sorteio**", value=f"`{pre}categoria-sorteio`")
  embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Comando executado por {ctx.author.name} | Me adicione! {pre}invite")
  await ctx.send(embed=embed)

@bot.command(name='categoria-random')
async def categoria(ctx):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)]

  embed=discord.Embed(title=f"<a:aaalerta:779758882754134037> Olá {ctx.author.name} aqui estão Meus comandos da categoria `Random`!", color=0x3df2ff)
  embed.set_thumbnail(url=f"{bot.user.avatar_url}")
  embed.set_author(icon_url=f"{bot.user.avatar_url}", name="Painel de Comandos - Random")
  embed.add_field(name="<a:napo2:772906112122748929> Comandos Random", value=f"<:setaroxa:779207810990080010> `{pre}invite, {pre}help, {pre}say, {pre}botinfo, {pre}avatar, {pre}serverinfo, {pre}leaderboard, {pre}level`", inline=False)
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text=f"Executado por: {ctx.author.name} - {ctx.author.id}")
  await ctx.send(embed=embed)

@bot.command(name='categoria-adm')
async def categoria(ctx):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)]

  embed=discord.Embed(title=f"<a:aaalerta:779758882754134037> Olá {ctx.author.name} aqui estão Meus comandos da categoria `Adminstrador`!", color=0x3df2ff)
  embed.set_thumbnail(url=f"{bot.user.avatar_url}")
  embed.set_author(icon_url=f"{bot.user.avatar_url}", name="Painel de Comandos - Adminstrador")
  embed.add_field(name="<a:napo2:772906112122748929> Comandos Adminstrador", value=f"<:setaroxa:779207810990080010> `{pre}clear, {pre}kick, {pre}ban, {pre}unban, {pre}lock, {pre}unlock, {pre}mute, {pre}unmute, {pre}warn, {pre}warnings, {pre}invites, {pre}changeprefix, {pre}embed, {pre}setwelcome, {pre}setlogs, {pre}tempmute, {pre}nick`", inline=False)
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text=f"Executado por: {ctx.author.name} - {ctx.author.id}")
  await ctx.send(embed=embed)

@bot.command(name='categoria-sorteio')
async def categoria(ctx):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)]

  embed=discord.Embed(title=f"<a:aaalerta:779758882754134037> Olá {ctx.author.name} aqui estão Meus comandos da categoria `Sorteio`!", color=0x3df2ff)
  embed.set_thumbnail(url=f"{bot.user.avatar_url}")
  embed.set_author(icon_url=f"{bot.user.avatar_url}", name="Painel de Comandos - Sorteio")
  embed.add_field(name="<a:napo2:772906112122748929> Comandos Sorteio", value=f"<:setaroxa:779207810990080010> `{pre}giveaway, {pre}reroll`", inline=False)
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text=f"Executado por: {ctx.author.name} - {ctx.author.id}")
  await ctx.send(embed=embed)

@bot.command(name='categoria-fun')
async def categoria(ctx):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)]

  embed=discord.Embed(title=f"<a:aaalerta:779758882754134037> Olá {ctx.author.name} aqui estão Meus comandos da categoria `Diversão`!", color=0x3df2ff)
  embed.set_thumbnail(url=f"{bot.user.avatar_url}")
  embed.set_author(icon_url=f"{bot.user.avatar_url}", name="Painel de Comandos - Diversão")
  embed.add_field(name="<a:napo2:772906112122748929> Comandos Diversão", value=f"<:setaroxa:779207810990080010> `{pre}dance, {pre}hug, {pre}kiss, {pre}jokenpo, {pre}porta, {pre}tableflip, {pre}stonks, {pre}poze, {pre}supreme, {pre}blur`", inline=False)
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text=f"Executado por: {ctx.author.name} - {ctx.author.id}")
  await ctx.send(embed=embed)

@bot.command(name='categoria-economia')
async def categoria(ctx):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)

  pre = prefixes[str(ctx.guild.id)]

  embed=discord.Embed(title=f"<a:aaalerta:779758882754134037> Olá {ctx.author.name} aqui estão Meus comandos da categoria `Economia`!", color=0x3df2ff)
  embed.set_thumbnail(url=f"{bot.user.avatar_url}")
  embed.set_author(icon_url=f"{bot.user.avatar_url}", name="Painel de Comandos - Economia")
  embed.add_field(name="<a:napo2:772906112122748929> Comandos Economia", value=f"<:setaroxa:779207810990080010> `{pre}work, {pre}balance, {pre}pagar, {pre}roubar, {pre}shop, {pre}buy, {pre}bolsa`", inline=False)
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text=f"Executado por: {ctx.author.name} - {ctx.author.id}")
  await ctx.send(embed=embed)


@bot.command()
async def roletarussa(ctx):
  arma = ['Você Sobreviveu! :tada:','Você Morreu! R.I.P :skull:','a Arma falhou! :gun:']
  await ctx.send("Você colocou uma bala e girou o tambor... :gun:")
  await sleep(3)
  await ctx.send(random.choice(arma))

@commands.is_owner()
@bot.command()
async def eval(ctx, *, code):
    str_obj = io.StringIO() #Retrieves a stream of data
    try:
        with contextlib.redirect_stdout(str_obj):
            exec(code)
    except Exception as e:
      embed=discord.Embed(description=f"**<:red_seta:787390025012084767> | Saida**\n```{e.__class__.__name__}: {e}```")
      embed.set_author(icon_url=f"{ctx.author.avatar_url}", name="Eval | Error!!")
      embed.add_field(name="<:simbolo_adicionar:784902965566767124> | Entrada", value=f"```{code}```")
      await ctx.send(embed=embed)
      return
    embed=discord.Embed(description=f"**<:red_seta:787390025012084767> | Saida**\n```{str_obj.getvalue()}```")
    embed.set_author(icon_url=f"{ctx.author.avatar_url}", name="Eval | Sucesso!!")
    embed.add_field(name="<:simbolo_adicionar:784902965566767124> | Entrada", value=f"```{code}```")
    await ctx.send(embed=embed)

@bot.command(aliases = ["lb"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        nome = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = nome
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Usuarios Ricos" , description = "Isto é decidido com o dinheiro em mãos e do banco!",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        nome = member.name
        em.add_field(name = f"{index}. {nome}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

@bot.event
async def on_member_join(member):
  with open('guilds.json', 'r', encoding='utf-8') as f:
    guilds_dict = json.load(f)

  print(f"Canal de Boas-vindas não Setado - {member.guild.id}")
  channel_id = guilds_dict[str(member.guild.id)]
  embed=discord.Embed(title=f"<a:yay:777976563400441877> | {member.name}", description=f"{member.mention} Bem-Vindo(a), ao servidor `{member.guild.name}`! Divirta-se e leia as regras para não ser punido! Estamos com `{member.guild.member_count}` Membros!", color=0x00fbff)
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_footer(icon_url=f"{member.avatar_url}", text=f"{member.name} Entrou no servidor!")
  await bot.get_channel(int(channel_id)).send(embed=embed)

@bot.event
async def on_member_remove(member):
  with open('guilds.json', 'r', encoding='utf-8') as f:
    guilds_dict = json.load(f)

  print(f"Canal de Boas-vindas não Setado - {member.guild.id}")
  channel_id = guilds_dict[str(member.guild.id)]
  embed=discord.Embed(title=f"<a:A_peppo_sad:777976250299580437> | {member.name}", description=f"{member.mention} Saiu do servidor. Espero que ele volte! Estamos com `{member.guild.member_count}` Membros...", color=0x00fbff)
  embed.set_thumbnail(url=f"{member.avatar_url}")
  embed.set_footer(icon_url=f"{member.avatar_url}", text=f"{member.name} Saiu do servidor...")
  await bot.get_channel(int(channel_id)).send(embed=embed)

@bot.command(name='setwelcome')
@commands.has_permissions(administrator=True)
async def set_welcome_channel(ctx, channel: discord.TextChannel):
  with open('guilds.json', 'r', encoding='utf-8') as f:
    guilds_dict = json.load(f)

    guilds_dict[str(ctx.guild.id)] = str(channel.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
    
    await ctx.send(f'Canal de boas vindas `{ctx.message.guild.name}` setado para `{channel.name}`')

@set_welcome_channel.error
async def set_welcome_channel_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `Administrator` ")

@bot.event
async def on_guild_remove(guild):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict.pop(guild.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)

@bot.command(name='setlogs')
@commands.has_permissions(administrator=True)
async def set_logs_channel(ctx, channel: discord.TextChannel):
  with open('logs.json', 'r', encoding='utf-8') as f:
    guilds_dict = json.load(f)

    guilds_dict[str(ctx.guild.id)] = str(channel.id)
    with open('logs.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
    
    await ctx.send(f'Canal de Logs `{ctx.message.guild.name}` setado para `{channel.name}`')

@set_logs_channel.error
async def set_logs_channel_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `Administrator` ")

@bot.event
async def on_message_delete(message):
  with open('logs.json', 'r', encoding='utf-8') as f:
    guilds_dict = json.load(f)
    
  print("Mensagem deletada")
  fields = [("content", message.content, False)]
  channel_id = guilds_dict[str(message.guild.id)]
  print(f"ID - {message.guild.id}")
  if not message.author.bot:
    em = discord.Embed(title="<a:2668_Siren:772951749182095420> | Logs", description=f"Ação por {message.author.display_name}.", color=discord.Color.red())
    em.add_field(name="Mensagem Deletada", value=f"`{message.content}`", inline=False)
    await bot.get_channel(int(channel_id)).send(embed=em)
    print("Mensagem deletada")

@bot.event
async def on_message_delete(contextlib):
  print("mensagem deletada")
  pass

@bot.command(name="kick", pass_context=True)
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	embed = discord.Embed(title="Membro Expulso", description=f"Ixii, parece que {member.mention} Fez alguma coisa")
	embed.add_field(name="Motivo", value=f"{reason}")
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await member.kick(reason=reason)
	await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `kick_members` ")

@bot.command(name="ban", pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	embed = discord.Embed(
	    title="Membro Banido!",
	    description=f"Ixii, parece que {member.mention} Fez alguma coisa")
	embed.add_field(name="Motivo", value=f"{reason}")
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await member.ban(reason=reason)
	await ctx.send(embed=embed)

@ban.error
async def ban(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `ban_members` ")

@bot.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
	user = await bot.fetch_user(id)
	await ctx.guild.unban(user)
	embed = discord.Embed(
	    title="Desbanimento",
	    description=f"O Id `{id}` Foi perdoado por {ctx.author.mention}")
	embed.set_thumbnail(url=f"{bot.user.avatar_url}")
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await ctx.send(embed=embed)


@bot.command()
@commands.guild_only()
async def serverinfo(ctx):
	embed1=discord.Embed(title=f"<:discord:772926614371172383> {ctx.guild.name}", color=0x00fbff)
	embed1.set_thumbnail(url=f"{ctx.guild.icon_url}")
	embed1.add_field(name="Região", value=f"{ctx.guild.region}")
	embed1.add_field(name="Criado", value=f"{ctx.guild.created_at}")
	embed1.add_field(name="Membros", value=f"{ctx.guild.member_count}")
	embed1.add_field(name="ID", value=f"{ctx.guild.id}")
	embed1.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Comando executado por {ctx.author.name}")
	await ctx.send(embed=embed1)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
    
  pre = prefixes[str(ctx.guild.id)]

  overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = False
  await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  embed=discord.Embed(title="<a:2668_Siren:772951749182095420> Canal Trancado", description=f"Canal trancado por {ctx.author.mention}, para destrancar utilize `{pre}unlock`", color=0x00fbff)
  embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Comando executado por {ctx.author.name}")
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  await ctx.send(embed=embed)

@lock.error
async def lock_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `manage_channels` ")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
  with open("prefixes.json", "r") as f:
   prefixes = json.load(f)
   
  pre = prefixes[str(ctx.guild.id)] 
  
  overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = True
  await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  embed = discord.Embed(title="<a:2668_Siren:772951749182095420> Canal Destrancado", description=f"Canal trancado por {ctx.author.mention}, para trancar utilize `{pre}lock`", color=0x00fbff)
  embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Comando executado por {ctx.author.name}")
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  await ctx.send(embed=embed)

@unlock.error
async def unlock_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `manage_channels` ")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear(ctx, amount: int):
  await ctx.channel.purge(limit=amount+1)
  embed=discord.Embed(title="Clear", description=f":tada: | **Eu deletei {amount} Mensagens!**")
  embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Comando executado por {ctx.author.name}")
  await ctx.send(embed=embed)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = ":x: | **Espere {:.2f}s para executar este comando! **".format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error
      
@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `manage_messages` ")



@bot.command(pass_context=True, aliases=['abraço'])
async def hug(ctx, *, usuario: discord.Member = None):
	if usuario is None:
		await ctx.send(
		    f"**{ctx.author.mention}, Mencione alguem para abraçar**")
		return
	links1 = [
	    "https://loritta.website/assets/img/actions/hug/female_x_male/gif_154.gif",
	    "https://loritta.website/assets/img/actions/hug/female_x_female/gif_143.gif",
	    "https://loritta.website/assets/img/actions/hug/female_x_female/gif_132.gif"
	]
	embed = discord.Embed(
	    title="<a:vanhelsing_hug:774012542279876648>  Abraço",
	    description=f"{ctx.author.mention} Abraçou, {usuario.mention}")
	embed.set_image(url=(random.choice(links1)))
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await ctx.send(embed=embed)


@bot.command()
async def dance(ctx):
	links = [
	    "https://media.tenor.com/images/0be4033d4b361127f4990add85864c5e/tenor.gif",
	    "https://i2.kym-cdn.com/photos/images/original/001/115/816/936.gif"
	]
	embed = discord.Embed(title="<a:Dance:772934417026121730> Dançando")
	embed.set_image(url=(random.choice(links)))
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
	guild = ctx.guild
	mutedRole = discord.utils.get(ctx.guild.roles, name="Mutado")

	if not mutedRole:
		mutedRole = await guild.create_role(name="Mutado")

		for channel in guild.channels:
			await channel.set_permissions(
			    mutedRole,
			    speak=False,
			    send_messages=False,
			    read_message_history=True)

	await member.add_roles(mutedRole, reason=reason)
	embed = discord.Embed(
	    title="Mutado!",
	    description=f"{ctx.author.mention}, Mutou {member}.",
	    color=0xff0000)
	embed.set_thumbnail(url=f"{member.avatar_url}")
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await ctx.send(embed=embed)
	embed1 = discord.Embed(
	    title="Mutado!",
	    description=
	    f"{member.mention} Você foi mutado! por {ctx.author.name}, Motivo: \n`{reason}`.",
	    color=0xff0000)
	embed1.set_thumbnail(url=f"{ctx.author.avatar_url}")
	embed1.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await member.send(embed=embed1)

@mute.error
async def mute_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `manage_messages` ")

def convert(tempo):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

@bot.command()
@commands.has_permissions(administrator=True)
async def tempmute(ctx, member: discord.Member, tempo: int, *, reason=None):
  guild = ctx.guild
  mutedRole = discord.utils.get(ctx.guild.roles, name="Mutado")

  if not mutedRole:
    mutedRole = await guild.create_role(name="Mutado")
    
    for channel in guild.channels:
      await channel.set_permissions(
			    mutedRole,
			    speak=False,
			    send_messages=False,
			    read_message_history=True)
  if reason is None:
    await ctx.send("porfavor tente `a.tempmute @usuario [tempo em segundos] motivo`")
    return
  await member.add_roles(mutedRole, reason=reason)
  await ctx.send(f":white_check_mark: | Usuario mutado com sucesso o tempo é de `{tempo}`!")
  await asyncio.sleep(tempo)
  await member.remove_roles(mutedRole)
  await ctx.send(":white_check_mark: | Usuario desmutado com sucesso!")

@tempmute.error
async def tempmute_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `administrator` ")

@bot.command()
async def unmute(ctx, member: discord.Member):
	mutedRole = discord.utils.get(ctx.guild.roles, name="Mutado")

	await member.remove_roles(mutedRole)
	embed = discord.Embed(
	    title="Desmutado!",
	    description=f"{ctx.author.mention}, Desmutou {member.mention}.",
	    color=0x00ff33)
	embed.set_thumbnail(url=f"{member.avatar_url}")
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await ctx.send(embed=embed)
	embed1 = discord.Embed(
	    title="Desmutado!",
	    description=
	    f"{ctx.author.name}, Desmutou você no servidor `{ctx.guild.name}`",
	    color=0x00ff33)
	embed1.set_thumbnail(url=f"{member.avatar_url}")
	embed1.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await member.send(embed=embed1)

@unmute.error
async def unmute_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `administrator` ")

@bot.command()
async def kiss(ctx, *, usuario: discord.Member = None):
	if usuario is None:
		await ctx.send("Mencione, alguem para beijar!")
		return
	beijos = [
	    "https://loritta.website/assets/img/actions/kiss/both/gif_285.gif",
	    "https://loritta.website/assets/img/actions/kiss/female_x_male/gif_0.gif",
	    "https://loritta.website/assets/img/actions/kiss/both/gif_281.gif"
	]
	embed = discord.Embed(
	    title="Beijo",
	    description=f"{ctx.author.mention} Beijou {usuario.mention}")
	embed.set_image(url=(random.choice(beijos)))
	embed.set_footer(
	    icon_url=f"{ctx.author.avatar_url}",
	    text=f"Comando executado por {ctx.author.name}")
	await ctx.send(embed=embed)
	
@bot.command(pass_context=True, aliases=['upt'])
async def uptime(ctx):
  current_time = time.time()
  difference = int(round(current_time - start_time))
  text = str(datetime.timedelta(seconds=difference))
  embed = discord.Embed(colour=ctx.message.author.top_role.colour)
  embed.add_field(name="Uptime", value=text)
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
  await ctx.send(embed=embed)
  await ctx.message.delete()

@bot.command()
async def botinfo(ctx):
  current_time = time.time()
  difference = int(round(current_time - start_time))
  text = str(datetime.timedelta(seconds=difference))
  embed = discord.Embed(colour=ctx.message.author.top_role.colour)
  embed.set_author(icon_url=f"{ctx.author.avatar_url}", name=f"{ctx.author.name}")
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  embed.add_field(name="<:dnd:556678417018257408> Uptime", value=f"`{text}`", inline=True)
  embed.add_field(name="<:bot:538163542260580352> Biblioteca", value="`Discord.py`", inline=True)
  embed.add_field(name="<:hypesquad:556680458411311114> Criado", value=f"`Dia 8 Mês 11 Ano 2020`", inline=True)
  embed.add_field(name="<:owner:556682207532679189> Dono", value="`! $rLuckkyz#6666`", inline=True)
  embed.add_field(name="<:vazio:769315661746536469>Meu ID", value=f"`{bot.user.id}`", inline=True)
  embed.add_field(name="<:server:775912981560033281> Guilds & Membros", value=f"Servidores: `{len(bot.guilds)}`\nMembros: `{len(bot.users)}`")
  embed.add_field(name="<:partner2:767235399943979038> Site", value="[Clique aqui](https://aquabot-website.glitch.me/)", inline=False)
  embed.add_field(name="<:partner2:767235399943979038> Bot List", value="[Clique aqui](https://zuraaa.com/bots/775027437695664160)", inline=False)
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
  await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['jk'])
async def jokenpo(ctx, user_choice):
    rpsGame = ['pedra', 'papel', 'tesoura']
    if user_choice.lower() in rpsGame: # Better use this, its easier. [lower to prevent the bot from checking a word like this "pedra or papel"
        bot_choice = random.choice(rpsGame)
        embed=discord.Embed(title="<:Papel:775816958176002059> JokenPô", description=f"<a:among3:775817348438818826> Sua Escolha: `{user_choice}`\n<:bot:775817471348572205> Escolha do Bot: `{bot_choice}`", color=0x0aefff)
        await ctx.send(embed=embed)
        await sleep(2)
        user_choice = user_choice.lower() # Also prevent a random word such as "pedra"
        if user_choice == bot_choice:
            embed=discord.Embed(title="<a:FAX_moedinha:775819248722771979>  Empate!", description=f"{ctx.author.mention} Empate!!", color=0xffde0a)
            await ctx.send(embed=embed)
        # pedra Win Conditions #
        if user_choice == 'pedra' and bot_choice == 'papel':
            embed=discord.Embed(title="<:uau:775816826948812851> Derrota!", description=f"{ctx.author.mention} Você Perdeu!", color=0xff0000)
            await ctx.send(embed=embed)
        if user_choice == 'pedra' and bot_choice == 'tesoura':
            embed=discord.Embed(title="<a:coroa:772904784926605322> Vitoria!", description=f"{ctx.author.mention} Você venceu!", color=0x44ff00)
            await ctx.send(embed=embed)
        # papel Win Conditions #
        if user_choice == 'papel' and bot_choice == 'pedra':
            embed=discord.Embed(title="<a:coroa:772904784926605322> Vitoria!", description=f"{ctx.author.mention} Você venceu!", color=0x44ff00)
            await ctx.send(embed=embed)
        if user_choice == 'papel' and bot_choice == 'tesoura':
            embed=discord.Embed(title="<:uau:775816826948812851> Derrota!", description=f"{ctx.author.mention} Você Perdeu!", color=0xff0000)
            await ctx.send(embed=embed)
        # Scissor Win Conditions #
        if user_choice == 'tesoura' and bot_choice == 'papel':
            embed=discord.Embed(title="<a:coroa:772904784926605322> Vitoria!", description=f"{ctx.author.mention} Você venceu!", color=0x44ff00)
            await ctx.send(embed=embed)
        if user_choice == 'tesoura' and bot_choice == 'pedra':
            embed=discord.Embed(title="<:uau:775816826948812851> Derrota!", description=f"{ctx.author.mention} Você Perdeu!", color=0xff0000)
            await ctx.send(embed=embed)
    else:
        await ctx.send('**Error** Este comando funciona apenas com pedra, papel, or tesoura.')


@bot.command()
async def invites(ctx, usr=None):
    if usr is None:
       user = ctx.author
    else:
       user = usr
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            totalInvites += i.uses
    await ctx.send(f"{user.mention} Convidou {totalInvites} Membro{'' if totalInvites == 1 else 's'}!")

@bot.command(pass_context = True)
@has_permissions(manage_roles=True, ban_members=True)
async def warn(message,user:discord.User,*reason:str):
  if not reason:
    await message.channel.send(f":clown: | **Coloque o motivo para eu punir este usuario!**")
    return
    await message.channel.send(f":tada: | **{message.author.mention} Usuario punido. Espero que ele não faça mais nada de errado. `a.warnings @usuario`**")
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    await message.channel.send(f":tada: | **{message.author.mention} Usuario punido. Espero que ele não faça mais nada de errado. `a.warnings @usuario**")
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)
  
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
    
  pre = prefixes[str(message.guild.id)] 

@warn.error
async def warn_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `manage_roles, ban_members` ")

@bot.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      embed=discord.Embed(description=f":tada: | {user.mention} Foi avisado {len(current_user['reasons'])} Vezes: \n{', '.join(current_user['reasons'])}", color=0x00fbff)
      embed.set_author(icon_url=f"{user.avatar_url}", name="| Avisos")
      embed.set_thumbnail(url=f"{user.avatar_url}")
      embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
      await ctx.channel.send(embed=embed)
      break
  else:
    await ctx.channel.send(f"{user.mention} Nunca foi reportado(a)!")

@warnings.error
async def warnings_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f":x: {ctx.author.mention} Mencione um usuario para verificar! ")

@bot.command()
async def porta(ctx, *, usr:discord.Member=None):
  if usr is None:
    embed=discord.Embed(title="<:aqua_ok:775896608742441000> Aqua BOT!", color=0x00fbff)
    embed.set_image(url=f"https://useless-api.vierofernando.repl.co/door?image={ctx.author.avatar_url}")
    embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
    await ctx.send(embed=embed)
    return
  embed=discord.Embed(title="<:aqua_ok:775896608742441000> Aqua BOT!", color=0x00fbff)
  embed.set_image(url=f"https://useless-api.vierofernando.repl.co/door?image={usr.avatar_url}")
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
  await ctx.send(embed=embed)

@bot.command()
async def avatar1(ctx, *, usr:discord.Member):
  await ctx.send(f"{usr.avatar_url}")

@bot.command()
async def supreme(ctx, *, palavra=None):
    embed=discord.Embed(title="<:aqua_ok:775896608742441000> Aqua BOT!", color=0x00fbff)
    embed.set_image(url=f"https://api.alexflipnote.dev/supreme?text={palavra}")
    embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
    await ctx.send(embed=embed)

@bot.command()
async def stonks(ctx, *, usuario: discord.Member = None):
  if usuario is None:
    embed=discord.Embed(title="<:aqua_ok:775896608742441000> Aqua BOT!", color=0x00fbff)
    embed.set_image(url=f"https://vacefron.nl/api/stonks?user={ctx.author.avatar_url}?size=4096")
    embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
    await ctx.send(embed=embed)
    return
  embed=discord.Embed(title="<:aqua_ok:775896608742441000> Aqua BOT!", color=0x00fbff)
  embed.set_image(url=f"https://vacefron.nl/api/stonks?user={usuario.avatar_url}?size=4096")
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
  await ctx.send(embed=embed)

@bot.command()
async def poze(ctx, *, palavra):
  if palavra is None:
    embed=discord.Embed(title="<:aqua_ok:775896608742441000> Aqua BOT!", color=0x00fbff)
    embed.set_image(url=f"https://atersetw.sirv.com/2020_11_10_111703.png?text.0.text={palavra}&text.0.position.y=7%25&text.0.size=100&text.0.color=00e3fd")
    embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
    await ctx.send(embed=embed)
    return
  embed=discord.Embed(title="<:aqua_ok:775896608742441000> Aqua BOT!", color=0x00fbff)
  embed.set_image(url=f"https://atersetw.sirv.com/2020_11_10_111703.png?text.0.text={palavra}&text.0.position.y=7%25&text.0.size=100&text.0.color=00e3fd")
  embed.set_footer(icon_url=f"{bot.user.avatar_url}", text="Aqua BOT! | Vote em mim na Zuraaa List!")
  await ctx.send(embed=embed)

# SISTEMA DE ECONOMIA
@bot.command(pass_context=True, aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s Balance", color=discord.Color.red())
    em.set_thumbnail(url=f"{ctx.author.avatar_url}")
    em.add_field(name="Dinheiro", value=wallet_amt)
    em.add_field(name="Banco", value=bank_amt)
    em.set_footer(icon_url=f"{bot.user.avatar_url}", text="Espere 1 Hora par Trabalhar Novamente!")
    await ctx.send(embed=em)



@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author

    earnings = random.randrange(101)

    await ctx.send(f":moneybag: | **Você Trabalhou um pouco e ganhou R${earnings}!**")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = ":money_with_wings: | **Espere {:.2f}s para executar este comando! **".format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error
                 
@bot.command(pass_context=True, aliases=['dep'])
async def depositar(ctx, amount = None):
  await open_account(ctx.author)

  if amount == None:
    await ctx.send(f":moneybag: | **Coloque um valor para depositar!**")
    return
  
  bal = await update_bank(ctx.author)
  
  amount = int(amount)
  if amount>bal[0]:
    await ctx.send(":x: | **Você não tem tanto dinheiro assim!**")
    return
  if amount<0:
    await ctx.send(":x: | **Coloque uma quantidade Positiva**")
    return
  
  await update_bank(ctx.author,-1*amount)
  await update_bank(ctx.author,amount,"bank")

  await ctx.send(f":tada: | **{ctx.author.mention} Pronto! você depositou `R${amount}` Em sua conta com sucesso!**")

@bot.command()
@commands.is_owner()
async def addmoney(ctx,member:discord.Member, amount = None):
  await open_account(ctx.author)
  await open_account(member)

  if amount == None:
    await ctx.send(f":moneybag: | **Coloque um valor para depositar!**")
    return
  
  bal = await update_bank(ctx.author)
  if amount == "all":
    amount = bal[0]
  
  amount = int(amount)
  if amount<0:
    await ctx.send(":x: | **Coloque uma quantidade Positiva**")
    return
  
  await update_bank(member,amount,"bank")

  await ctx.send(f":tada: | **{ctx.author.mention} Pronto! você pagou {member.mention} `R${amount}` Na conta dele com sucesso!**")


@bot.command(pass_context=True, aliases=['pay'])
async def pagar(ctx,member:discord.Member, amount = None):
  await open_account(ctx.author)
  await open_account(member)

  if amount == None:
    await ctx.send(f":moneybag: | **Coloque um valor para depositar!**")
    return
  
  bal = await update_bank(ctx.author)
  if amount == "all":
    amount = bal[0]
  
  amount = int(amount)
  if amount>bal[1]:
    await ctx.send(":x: | **Você não tem tanto dinheiro assim! no seu banco**")
    return
  if amount<0:
    await ctx.send(":x: | **Coloque uma quantidade Positiva**")
    return
  
  await update_bank(ctx.author,-1*amount,"bank")
  await update_bank(member,amount,"bank")

  await ctx.send(f":tada: | **{ctx.author.mention} Pronto! você pagou {member.mention} `R${amount}` Na conta dele com sucesso!**")

@bot.command(pass_context=True, aliases=['rob'])
async def roubar(ctx,member:discord.Member):
  await open_account(ctx.author)
  await open_account(member)
  
  bal = await update_bank(member)
  
  if bal[0]<100:
    await ctx.send(":x: | **Ele não tem dinheiro suficiente**")
    return
  
  earnings = random.randrange(0, bal[0])
  
  await update_bank(ctx.author,earnings)
  await update_bank(member,-1*earnings)

  await ctx.send(f":tada: | **{ctx.author.mention} Você roubou {member.mention} e ganhou `R${earnings}`!**")

@bot.command(pass_context=True, aliases=['casino'])
@commands.cooldown(1, 3600, commands.BucketType.user)
async def slots(ctx, amount=None):
  await open_account(ctx.author)

  if amount == None:
    await ctx.send(f":moneybag: | **Coloque um valor para depositar!**")
    return
  
  bal = await update_bank(ctx.author)
  
  amount = int(amount)
  if amount>bal[0]:
    await ctx.send(":x: | **Você não tem tanto dinheiro assim!**")
    return
  if amount<0:
    await ctx.send(":x: | **Coloque uma quantidade Positiva**")
    return

  final = []
  for i in range(3):
    a = random.choice(["X", "O", "Q"])

    final.append(a)
  
  await ctx.send(str(final))

  if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
    await update_bank(ctx.author,2*amount)
    await ctx.send(":tada: | **Você venceu!**")
  else:
    await update_bank(ctx.author,-1*amount)
    await ctx.send(":money_with_wings: | **Você Perdeu!**")


@slots.error
async def slots_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = ":money_with_wings: | **Espere {:.2f}s para jogar novamente**".format(error.retry_after)
    await ctx.send(msg)
  else:
    raise error

@bot.command(pass_context=True, aliases=['with'])
async def withdraw(ctx, amount = None):
  await open_account(ctx.author)

  if amount == None:
    await ctx.send(f":moneybag: | **Coloque um valor para depositar!**")
    return
  
  bal = await update_bank(ctx.author)
  
  amount = int(amount)
  if amount>bal[1]:
    await ctx.send(":x: | **Você não tem tanto dinheiro assim!**")
    return
  if amount<0:
    await ctx.send(":x: | **Coloque uma quantidade Positiva**")
    return
  
  await update_bank(ctx.author,amount)
  await update_bank(ctx.author,-1*amount,"bank")

  await ctx.send(f":tada: | **{ctx.author.mention} Pronto! você depositou `R${amount}` Em sua carteira com sucesso!**")

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json","w") as f:
      json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users
    
async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

# COMANDOS PARA O COG
def setup(client):
	client.add_cog(comando(client))


class comando(commands.Cog):
	def __init__(self, client):
		self.client = client

# SORTEIO
def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

@bot.command(pass_context=True, aliases=['gstart', 'sorteio'])
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx):
    await ctx.send("Vamos iniciar um sorteio!! Responda as perguntas com 15 Segundos!")

    questions = ["Qual canal deseja fazer o sorteio?", 
                "Qual será a duração do sorteio? (s|m|h|d)",
                "Qual eo premio do sorteio?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Você não, respondeu, tente ser mais rapido na proxima!!')
            return
        else:
            answers.append(msg.content)
        try:
          c_id = int(answers[0][2:-1])
        except:
          await ctx.send(f"Você não mencionou o canal, na proxima tente isto {ctx.channel.mention}.")
          return

    channel = bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"Você não respondeu. Use (s|m|h|d) na proxima vez!")
        return
    elif time == -2:
        await ctx.send(f":x: | O tempo deve ser inteiro. Por favor, entre em um inteiro da próxima vez")
        return            

    prize = answers[2]

    await ctx.send(f":tada: | Sorteio será em {channel.mention} e vai durar {answers[1]}!")


    embed = discord.Embed(title = ":tada: Sorteio!!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosteado por:", value = ctx.author.mention)

    embed.set_footer(text = f"Acaba em {answers[1]}!")

    my_msg = await channel.send(embed = embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Parabéns! {winner.mention} ganhou `{prize}`!")

@giveaway.error
async def giveaway_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `manage_messages` ")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("Você colocou o id errado!.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f":tada: | Parabéns o novo vencedor eo {winner.mention}.!")

@reroll.error
async def reroll_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `manage_messages` ")

# PREFIXO CONFIG


@bot.event
async def on_guild_join(guild):


    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "a."

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)




@bot.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix=None):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
    
  if prefix is None:
    await ctx.send(":x: Coloque o Prefixo! `a.changeprefix prefixo`")
    return
  
  prefixes[str(ctx.guild.id)] = prefix
  
  with open("prefixes.json", "w") as f:
    json.dump(prefixes,f)

  await ctx.send(f"<a:discord:777297811666239498> | O prefixo foi mudado para `{prefix}`")

@changeprefix.error
async def changeprefix_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f":x: {ctx.author.mention} Você Prescisa da permissão de `Administrator` ")

@bot.event
async def on_message(msg):
  try:
    if msg.content == '<@!775027437695664160>' :
      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
      pre = prefixes[str(msg.guild.id)] 
      
      await msg.channel.send(f"Olá {msg.author.mention}, meu prefixo neste servidor é `{pre}`")
      
  except:
    pass

  await bot.process_commands(msg)

# shop
@bot.command()
async def shop(ctx):
  em = discord.Embed(title = "Shop")
  em.set_thumbnail(url=f"{bot.user.avatar_url}")
  for item in mainshop:
      name = item["name"]
      price = item["price"]
      desc = item["description"]
      em.add_field(name=name, value=f"R${price} | {desc}")
  await ctx.send(embed=em)

@bot.command()
async def embed1(ctx):
  embed=discord.Embed(title="Titulo", description="Descrição", color=0x080808)
  embed.add_field(name="Nome", value="Valor")
  embed.set_thumbnail(url="https://am23.akamaized.net/tms/cnt/uploads/2019/11/discord-fandoms-exodus-1200x675.jpeg")
  embed.set_image(url="https://am23.akamaized.net/tms/cnt/uploads/2019/11/discord-fandoms-exodus-1200x675.jpeg")
  embed.set_footer(icon_url="https://am23.akamaized.net/tms/cnt/uploads/2019/11/discord-fandoms-exodus-1200x675.jpeg", text="Texto Footer")
  await ctx.send(embed=embed)

@bot.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)
    
    res = await buy_this(ctx.author,item,amount)
    
    if not res[0]:
        if res[1]==1:
            await ctx.send(":x: | Este item não existe!")
            return
        if res[1]==2:
          await ctx.send(f"Você não tem dinheiro suficiente para comprar isto! {amount} {item}!!")
          return
            
    await ctx.send(f"<a:FAX_moedinha:775819248722771979> | Você comprou {item} com sucesso! Quantidade `{amount}`")

@bot.command(pass_context=True, aliases=['bag'])
async def bolsa(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    
    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []
        
    em = discord.Embed(title = "<a:FAX_moedinha:775819248722771979> | Bolsa")
    em.set_thumbnail(url=f"{ctx.author.avatar_url}")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
        
        em.add_field(name= name, value = amount)
        
    await ctx.send(embed=em)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@bot.command(pass_context=True, aliases=['vender'])
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send(":x: | Este item não existe!")
            return
        if res[1]==2:
            await ctx.send(f":x: | Você não tem {amount} {item} Em sua bolsa")
            return
        if res[1]==3:
            await ctx.send(f":x: | Você não possui {item} em sua bolsa.")
            return

    await ctx.send(f":white_check_mark: | Você vendeu {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

# SISTEMA

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def nick(ctx, member: discord.Member, *, nick):
  embed=discord.Embed(color=0x00ff9d)
  embed.set_author(icon_url=f"{member.avatar_url}", name=f"{member.name}'s Mudou seu Nick!")
  embed.add_field(name="Novo Nick:", value=f"{member.mention}")
  await member.edit(nick=nick)
  await ctx.send(embed=embed)

# MANIPULÇÃO DE IMAGEM
@bot.command()
async def ola(ctx, usr: discord.Member=None):
    if usr == None:
        usr = ctx.author
    
    wanted = Image.open("welcome.jpg")
    
    asset = usr.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    
    pfp = pfp.resize((186,159))
    
    wanted.paste(pfp, (20,50))
    
    wanted.save("profile.jpg")
    
    await ctx.send(file = discord.File("profile.jpg"))

@bot.command()
async def ascii(ctx, *, txt):
  word=pyfiglet.figlet_format(f"{txt}")
  await ctx.send(f"```{word}```")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"<:white_yuno_nao:783362129189142588> **Error! {error}**")
        return
    raise error

@bot.command(name="setwebhook", aliases=["setweb"], pass_context=True)
async def webhookpy(ctx, *, link=None):
    with open('webhook.json', 'r', encoding='utf-8') as f:
        web_dict = json.load(f)

    if link is None:
      await ctx.send("**Erro! Você não colocou o link certo! tente `a.setwebhook <link>`**")
    else:
      web_dict[str(ctx.author.id)] = str(link)
      with open('webhook.json', 'w', encoding='utf-8') as f:
        json.dump(web_dict, f, indent=4, ensure_ascii=False)
        await ctx.send(f"<:white_yuno_sim:783362165184528445> **Sucesso! Você setou o webhook com sucesso!")
    

@bot.command(name="fake", pass_context=True)
@commands.has_permissions(manage_messages=True)
async def fake_bot(ctx, *, msg):
    chan=bot.get_channel(int(ctx.channel.id))
    web=await chan.create_webhook(name=str(ctx.author.name))
    DiscordWebhook(url=f"{web.url}", content=msg)
    await ctx.message.delete()
    response = await web.send(msg, avatar_url=ctx.author.avatar_url)
    print(web.url)

@fake_bot.error
async def fake_bot_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f"<:white_yuno_nao:783362129189142588> Error, você não tem permissão de `{error}`")

@fake_bot.error
async def fake_bot_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f"<:white_yuno_nao:783362129189142588> Error, estou sem permissão! {error}`")

@fake_bot.error
async def fake_bot_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:white_yuno_nao:783362129189142588> Erro, está faltando algum argumento!")

# FUNCIONAMENTO DO BOT
if __name__ == "__main__":
	for modulo in modulos:
		bot.load_extension(modulo)

keep_alive() # WEB-PAGINA PARA UPTIME
bot.run('token')