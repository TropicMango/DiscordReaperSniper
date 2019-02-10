import discord

description = '''An bot designed to snipe'''
client = discord.Client()


@client.event
async def on_ready():  # when ready it prints the username, id, and starts the status update
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_typing(channel, user, when):
    print(user)
    if str(user.id) == '191597928090042369':  # 191597928090042369 is Excalibur's id
        time_status = str(
            channel.server.get_member('538078061682229258').game)  # a bit efficient but i'm pretty lazy :3
        current_hours = int(time_status.split(' ')[1][:-1])  # only gets the hours
        current_minutes = int(time_status.split(' ')[2][:-1])  # only gets the hours
        total_minutes = current_hours * 60 + current_minutes
        if total_minutes > 90:
            await client.send_message(channel, 't!reap')


client.run('email@email.email', 'password')  # typing in a user info here~
