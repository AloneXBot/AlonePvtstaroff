from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="💥 ⁣𓆩𝔸DD 𝕄E 𝕋O 𝕐OUƦ 𝔾ƦOUק𓆪 💥",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💥 ℂᴏᴍᴍᴀɴᴅʟᴇℝ 💥",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="💥 𝕊ᴇᴛᴛɪɴɢꜱ 💥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥 𝕌ᴘᴅᴀᴛ𝔼 💥", url=f"https://t.me/AloneXBots"),
            InlineKeyboardButton(
                text="💥 𝕊ᴜᴘᴘᴏʀ𝕋 💥", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = "https://t.me/ALONE_WAS_BOT"):
    buttons = [
        [
            InlineKeyboardButton(
                text="💥 𓆩𝔸DD 𝕄E 𝕋O 𝕐OUƦ 𝔾ƦOUק𓆪 💥",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥 ℂᴏᴍᴍᴀɴᴅʟᴇℝ 💥", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="💥 𝕌ᴘᴅᴀᴛ𝔼 💥", url=f"https://t.me/AloneXBots"),
            InlineKeyboardButton(
                text="💥 𝕊ᴜᴘᴘᴏʀ𝕋 💥", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="𓊈💥🔥𝔻eͥѵeͣlͫ𐍉קeℝ🔥💥𓊉", url=f"https://t.me/ALONE_WAS_BOT"
                )
        ],
     ]
    return buttons
