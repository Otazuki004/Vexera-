from pyrogram import filters, enums
from Vexera.__init__ import BOT as bot
from pyrogram.types import *
import os, io, time


@bot.on_message(filters.command("ban"))
async def ban(_, message):
    if message.chat.type == "private":
        await message.reply_text("Work only on groups!")
    else:
        try:
            if not message.reply_to_message:
                  return await message.reply("**Reply someone to ban.**")
            get = await bot.get_chat_member(message.chat.id, message.from_user.id) 
            chat_id = message.chat.id
            reply = message.reply_to_message
            if not get.privileges:
                return await message.reply("**You Needs Admin Rights to Control Me (~_^)!**")
            if get.privileges.can_restrict_members:
                chat_id = message.chat.id
                user_id  = message.reply_to_message.from_user.id
                await bot.ban_chat_member(chat_id, user_id)
                await message.reply_text(text= "**Ban Successfully**")
            else:
                await message.reply_text(text = "**Your missing the admin rights `can_restrict_members`**")
        except Exception as errors:
           await message.reply(f"**Error**: {errors}")


@bot.on_message(filters.command("unban"))
async def unban(_, message):
    if message.chat.type == "private":
        await message.reply_text("Work only on groups!")
    else:
        try:
            if not message.reply_to_message:
                  return await message.reply("**Reply someone to unban.**")
            get = await bot.get_chat_member(message.chat.id,message.from_user.id)  
            chat_id = message.chat.id
            reply = message.reply_to_message
            if not get.privileges:
                return await message.reply("**You Needs Admin Rights to Control Me (~_^)!**")
            if get.privileges.can_restrict_members:
                chat_id = message.chat.id
                user_id  = message.reply_to_message.from_user.id
                await bot.unban_chat_member(chat_id, user_id)
                await message.reply_text(text= "**Unban Successfully**")
            else:
                await message.reply_text(text = "**Your missing the admin rights `can_restrict_members`**")
        except Exception as errors:
           await message.reply(f"**Error**: {errors}")


@bot.on_message(filters.command("demote"))
async def demotes(_, message):
   try:
       if not message.reply_to_message:
             return await message.reply("Reply to Someone")
       chat_id = message.chat.id
       admin = message.from_user
       user = message.reply_to_message.from_user
       check = await bot.get_chat_member(chat_id, admin.id)
       if check.privileges.can_promote_members:
            msg = await message.reply("Demoting...")
            await message.chat.promote_member(
               user_id=user.id,
               privileges=pyrogram.types.ChatPrivileges(
               can_change_info=False,
               can_invite_users=False,
               can_delete_messages=False,
               can_restrict_members=False,
               can_pin_messages=False,
               can_promote_members=False,
               can_manage_chat=False,
               can_manage_video_chats=False    
))
            await msg.edit(f"""**Demoted by Admin**:\n**{admin.mention}**
**Demoted User:** **{user.mention}**""")
   except Exception as errors:
           await message.reply(f"**Error**: {errors}")
       

      
      
@bot.on_message(filters.command("promote"))
async def promoting(_, message):
     global new_admin
     if not message.reply_to_message:
         return await message.reply("Reply someone To Promoting")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user
     user_stats = await bot.get_chat_member(chat_id, admin.id)
     bot_stats = await bot.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await message.reply("When Make Me Admin?")
     elif not user_stats.privileges:
         return await message.reply("**You Needs Admin Rights to Control Me (~_^)!**")
     elif not bot_stats.privileges.can_promote_members:
         return await message.reply("**I'm missing the admin rights `can_promote_members`**")
     elif not user_stats.privileges.can_promote_members:
         return await message.reply("**Your missing the admin rights `can_promote_members`**")
     elif user_stats.privileges.can_promote_members:
          msg = await message.reply_text("Promoting...")
          await bot.promote_chat_member(
            chat_id,
            new_admin.id,
            privileges=pyrogram.types.ChatPrivileges(
            can_change_info=True,
            can_delete_messages=True,
            can_pin_messages=True,
            can_invite_users=True,
            can_manage_video_chats=True,
            can_restrict_members=True
))
          await msg.edit(f"""**Promoted Admin**:\n**{admin.mention}**
          **New Admin:**\n**{new_admin.mention}** """,
              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Demote", callback_data="demote"),
                                                        InlineKeyboardButton(text="Delete", callback_data="close")]]))
                               
     
                     
@bot.on_callback_query(filters.regex("demote"))
async def demoting(_, query):
         chat_id = query.message.chat.id
         stats = await bot.get_chat_member(query.message.chat.id, query.from_user.id)
         if stats.privileges.can_promote_members:
                  await bot.promote_chat_member(
                     chat_id,
            new_admin.id,
            privileges=pyrogram.types.ChatPrivileges(
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_video_chats=False    
))
                  await query.message.edit(f"""**Demote by Admin:**\n** {query.from_user.mention}**
**Demoted Admin:**\n**{new_admin.mention}**""")    
         else:
               await query.answer("You can't Demote!", show_alert=True )
                    
        
@bot.on_message(filters.command("del"))
async def delete(_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
           return await m.reply_text("Make Me Admin!")
     elif not user_stats.privileges:
            return await m.reply_text("Only Admins are allowed to use this command!")    
     elif not reply:
            return  await m.reply_text("reply to message for deleting")
     elif not bot_stats.privileges.can_delete_messages:
              return await m.reply_text("**I'm missing the permission of**:\n`can_delete_messages`")
     elif not user_stats.privileges.can_delete_messages:
              return await m.reply_text("**your are missing the permission of**:\n`can_delete_messages`")
     elif user_stats.privileges.can_delete_messages:
               await reply.delete()
               await m.delete()
               
                     
@bot.on_message(filters.command(["setgtitle","setchattitle"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     new_title = m.text.split(None, 1)[1]
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
           return await m.reply_text("Make Me Admin REEE!!")
     elif not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     elif not bot_stats.privileges.can_manage_chat:
               await m.reply_text("**I'm missing the permission of**:\n`can_manage_chat`")
               return 
     elif not user_stats.privileges.can_manage_chat:
               await m.reply_text("**your are missing the permission of**:\n`can_manage_chat`")
               return 
     elif user_stats.privileges.can_manage_chat:
               await m.chat.set_title(new_title)
               await m.reply_text(f"Successfully set {new_title} as new chat title!")

@bot.on_message(filters.command(["setgpic","setchatpic"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     
     if not reply:
              return await m.reply_text("reply only document or photo")
      
     elif not bot_stats.privileges:
            return await m.reply_text("Make Me Admin REEE!!")
             
     elif not user_stats.privileges:
           return await m.reply_text("Only Admins are allowed to use this command!")
             
     elif not bot_stats.privileges.can_change_info:
             return await m.reply_text("**I'm missing the permission of**:\n`can_change_info`")
                
     elif not user_stats.privileges.can_change_info:
               return await m.reply_text("**your are missing the permission of**:\n`can_change_info`")
                
     elif user_stats.privileges.can_change_info:
               msg = await m.reply("**New Group Photo Process.**")
               photo = await reply.download()
               await bot.set_chat_photo(chat.id, photo=photo)
               await msg.edit_text("**Successfully group photo Applied**")
