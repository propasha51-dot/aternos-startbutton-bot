import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

# Запускаем веб-сервер, чтобы бот не засыпал
keep_alive()

# Бот берет токен из Environment Variables на Render
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} запущен и готов!')

@bot.command()
async def panel(ctx):
    embed = discord.Embed(
        title="🎮 Доступ к серверу Tidegrief2",
        description="Нажми на логин или пароль, чтобы **скопировать**.",
        color=discord.Color.green()
    )
    embed.add_field(name="👤 Логин", value="`tg_start`", inline=False)
    embed.add_field(name="🔑 Пароль", value="`123321`", inline=False)
    embed.set_footer(text="Совет: нажми «Запомнить меня» при входе.")

    view = discord.ui.View()
    button = discord.ui.Button(
        label="🚀 Открыть панель Aternos", 
        url="https://aternos.org",
        style=discord.ButtonStyle.link
    )
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

bot.run(DISCORD_TOKEN)
