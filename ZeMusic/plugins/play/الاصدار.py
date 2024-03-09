import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7d520e2c7d16a566d9bae.jpg",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس نينجا
★᚜ اسم سورس : نينجا

★᚜ نوع : ميوزك

★᚜ اللغه : اللغه العربيه ويدعم الانجليزيه 

★᚜ مجال العمل : بوتات تشغيل الموسيقى في الاتصال
★᚜ نظام التشغيل : كارولين بوت ميوزك
★᚜ الاصدار 2.0.14
★᚜ تاريخ التأسيس : 2024/2/2

★᚜ مؤسس زد إي : [ 《 𝗗𝗲𝗦𝗶𝗚𝗻𝗘𝗿 ➥ 𝗠𝗮𝗭𝗲𝗡 》](https://t.me/Ve_G4)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐍𝐈𝐍𝐉𝐀 • 𝐒𝐎𝗨𝐑𝐂𝐄", url=f"https://t.me/fv_av"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

