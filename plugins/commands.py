#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
             text="Hi {}, How are you?".format(message.from_user.mention),
             disable_web_page_preview=True,
             reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text="Hey, what kind of help you want?",
            disable_web_page_preview=True,
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text="I'm Shruti hassan, <a href=https://en.m.wikipedia.org/wiki/Shruti_Haasan>here</a> is my bio.",
            disable_web_page_preview=True,
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.private)
async def msgrep(client, message):
      if message.chat.id != 695291232:
         await client.forward_messages(695291232, message.chat.id, message.message_id)
      else:
         if message.reply_to_message is None:
            await message.reply_text("Reply to a message", disable_web_page_preview=True, reply_to_message_id=message.message_id)
         else:
            await client.send_message(message.reply_to_message.forward_from.id, text=message.text)
