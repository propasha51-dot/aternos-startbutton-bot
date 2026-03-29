from keep_alive import keep_alive
keep_alive()
import discord
from discord.ext import commands

# --- ТВОИ ДАННЫЕ ---
DISCORD_TOKEN = ''

# Настройка прав (интентов)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Сообщение в консоли при запуске
    print(f'✅ Бот {bot.user} запущен и готов раздавать доступы!')
    print('Используй команду !panel в Discord.')

@bot.command()
async def panel(ctx):
    # 1. Создаем красивую карточку (Embed)
    embed = discord.Embed(
        title="🎮 Доступ к серверу Tidegrief2",
        description=(
            "Нажми на логин или пароль ниже, чтобы **скопировать**, "
            "а затем нажми кнопку для перехода на сайт."
        ),
        color=discord.Color.green() # Зеленый цвет для успеха
    )

    # Добавляем данные. Текст внутри ` ` в Дискорде копируется очень легко.
    embed.add_field(name="👤 Логин (нажми чтобы скопировать)", value="`tg_start`", inline=False)
    embed.add_field(name="🔑 Пароль (нажми чтобы скопировать)", value="`123321`", inline=False)
    
    # Добавляем полезный совет внизу
    embed.set_footer(text="💡 Совет: при входе нажми «Запомнить меня», чтобы не вводить данные каждый раз.")

    # 2. Создаем кнопку-ссылку
    view = discord.ui.View()
    button = discord.ui.Button(
        label="🚀 Открыть панель Aternos", 
        url="https://aternos.org",
        style=discord.ButtonStyle.link
    )
    view.add_item(button)

    # 3. Отправляем сообщение в чат
    await ctx.send(embed=embed, view=view)
# Запуск бота
bot.run(DISCORD_TOKEN)
