from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ ᴛᴏ ᴇɴJᴏʏ ᴍᴜsɪᴄ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ ᴛᴏ ᴇɴJᴏʏ ᴍᴜsɪᴄ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐂ᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🍁 𝐂ʜᴀᴛ ʜᴇʀᴇ 🍁", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🎄 𝐎ᴡɴᴇʀ 🎄", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="🥂 𝐔ᴘᴅᴀᴛᴇs 🥂", url=f"https://t.me/DevanshXBots"
            )
        ],
     ]
    return buttons
