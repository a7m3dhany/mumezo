import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["نينجا","مازن","مطور السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/06774fa3fedc7fc8fdb75.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[《 𝗗𝗲𝗦𝗶𝗚𝗻𝗘𝗿 ➥ 𝗠𝗮𝗭𝗲𝗡 》](https://t.me/Ve_G4)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @elhyba ❫
◉ 𝙸𝙳      : ❪ `5951674553` ❫
◉ 𝙱𝙸𝙾    : ❪[#𝖱ꫀᥲ️ᥣᥣ𝗒,!Ꭵ ძ᥆ꪀ'𝗍 ᥴᥲ️𝗋ꫀ#ɪ'َᴍ 𓏺 𝗠 𝗮 𝗭 𝗲 𝗡 𓏺 ¹🦅🇪🇬](https://t.me/Fv_av)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒《 𝗗𝗲𝗦𝗶𝗚𝗻𝗘𝗿 ➥ 𝗠𝗮𝗭𝗲𝗡 》", url=f"https://t.me/Ve_G4"), 
                 ],[
                   InlineKeyboardButton(
                        "𝐍𝐈𝐍𝐉𝐀 • 𝐒𝐎𝗨𝐑𝐂𝐄", url=f"https://t.me/fv_av"),
                ],

            ]

        ),

    )
