import discord
from discord.ext import commands
import datetime
import time

token = #add your discord token here
client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(str(bot.user) + " is online!")


async def logi(message):
    with open("logi_bota_PL/logs.txt", 'a') as file:
        file.write(f'{message}\n')
    file.close()

@bot.command(pass_context=True)
async def send_message(ctx , mess):
    await logi("[{}] [LOG_DISCORD_SEND] {}".format(datetime.datetime.now(), mess))
    await ctx.send(mess)

async def printing(text):
    await logi("[{}] [LOG_IN_CMD] {}".format(datetime.datetime.now(), text))
    print("[{}] [LOG_IN_CMD] {}".format(datetime.datetime.now(), text))


async def create_txt(user, amount, accounts, country):
    file_name = "{}_{}_{}_{}.txt".format(user, country, amount, time.strftime('%d-%m-%Y_%H-%M-%S'))
    with open("LOGS_PL/"+file_name, 'w') as file:
        for i in range(amount):
            file.write(f'{accounts[i][0]}\n')
            file.write(f'{accounts[i][1]}\n')
        file.close()


async def remove(amount, csv):
    for i in range(amount):
        with open(csv, 'r+') as fp:
            await printing("REMOVING")
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:])
    await printing("REMOVING DONE")


@bot.command(pass_context=True)
async def gen(ctx, amount, country):
        user = ctx.message.author
        if discord.utils.get(ctx.guild.roles, name = "customer") not in user.roles:
            await send_message(ctx , "@{} You are not able to use this command!".format(user))
        else:
            try:
                if amount.isdigit():
                    amount = int(amount)
                    if 11 > amount > 0:
                        if country.lower() == "pl":
                            csv = #path to csv file
                            await send_message(ctx, "GENERATING {} PL ACC FOR USER {}".format(amount, user))
                            await printing("{} GENERATED {} - ACC PL".format(user, amount))

                            f = open(csv , "r")
                            lines = f.readlines()
                            accounts = []
                            for line in lines:
                                items = line.strip().split(",")
                                accounts.append(items)
                            await remove(amount, csv)
                            await create_txt(user, amount, accounts, country)
                            await user.send("DATETIME: [{}] - AMOUNT: {} - COUNTRY: {}".format(datetime.datetime.now(), amount, country.upper()))
                            for i in range(amount):
                                time.sleep(1)
                                await user.send(accounts[i][0])
                                await user.send(accounts[i][1])
                            await printing("DONE FOR {} - {} ACC PL ".format(user, amount))
                        else:
                            await send_message(ctx, "WRONG COUNTRY!")
                            await printing("{} CHOOSED WRONG COUNTRY".format(user))
                    else:
                        await send_message(ctx, "The minimum quantity per command is 1 and maximum is 10")

                else:
                    await send_message(ctx, "Wrong quantity")
            except Exception as e:
                await send_message(ctx, "Something went wrong")
                print(e)




bot.run(token)
