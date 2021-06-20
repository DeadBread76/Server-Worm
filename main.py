import discord
import asyncio

token = 'BOT TOKEN HERE'


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Ready.')
    print('------------')

@client.event
async def on_server_join(server):
    print ("Connected to " +server.name)
    memberdmlist = []
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            chan = channel
    for member in server.members:
        memberdmlist.append(member)
    for member in memberdmlist:
        perms = chan.permissions_for(member)
        if member.bot == True:
            continue
        if perms.kick_members:
            print (str(member)+ " can kick, not DMing.")
            continue
        if perms.ban_members:
            print (str(member)+ " can ban, not DMing.")
            continue
        if perms.administrator:
            print (str(member)+ " is admin, not DMing.")
            continue
        else:
            print ("DMing "+str(member))
            dmcontent = ('MESSAGE HERE')
            try:
                await client.send_message(member, dmcontent)
            except Exception as e:
                print ("Unable to DM " + str(member))
    try:
        await client.leave_server(server)
        print ("Left " +server.name)
    except Exception:
        print ("Unable to Leave the server.")
client.run(token)
