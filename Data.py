from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {} [🥀](https://te.legra.ph/file/8b94867323e64dd9c8ef8.jpg)

ɪ ᴄᴀɴ ғᴏʀᴄᴇ  ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴜsᴇʀ ᴛᴏ ᴊᴏɪɴ  ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ.
 ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ʙᴇ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ɪᴛ ᴄᴀɴ ᴘʀɪᴠᴀᴛᴇ ᴏʀ ᴘᴜʙʟɪᴄ.
 ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ʙᴀʙʏ !

Bʏ - [❥︎❥︎𝐼𝑇𝑆𝑀𝐸ت︎𝑽𝑰𝑽𝑬𝑲 亗](t.me/vivekevil)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="✰ ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ ✰", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✰ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ ✰", url="https://t.me/wariornetwork")],
        [
            InlineKeyboardButton("✰ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅ ✰", callback_data="help"),
            InlineKeyboardButton("✰ ᴀʙᴏᴜᴛ ᴍᴇ ✰", callback_data="about")
        ],
        [InlineKeyboardButton("✰ ᴀᴅᴅ ɢʀᴏᴜᴘ ᴄᴏɴᴛʀᴏʟʟᴇʀ ʙᴏᴛ ✰", url="https://t.me/ForceSubRBot?startgroup=true")],
        [InlineKeyboardButton("★ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ★", url="https://t.me/noobcreator")],
      ]
    # Help Message
    HELP = """
𝟷) ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴀ ɢʀᴏᴜᴘ.
𝟸) ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴀs ᴀᴅᴍɪɴ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ғᴏʀᴄᴇ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ. ɪᴛ ᴄᴀɴ ʙᴇ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ, ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ. 
𝟹) ᴜsᴇ /fsub chat_id /username ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ғᴜɴᴄᴛɪᴏɴᴀʟ. ᴜsᴇ /id ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴄʜᴀᴛ ɪᴅ.
 ᴇxᴀᴍᴘʟᴇ : /fsub -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 

 ✨ ᴀᴠᴀɪʟᴀʙᴇ ᴄᴍᴅs ʙᴀʙʏ  ✨ 
/start -  sᴛᴀʀᴛ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ʙᴏᴛ 
/fsub - sᴇᴇ ᴄᴜʀʀᴇɴᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀᴛ 
/fsub chat_id/username- ғᴏʀᴄᴇ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ
/settings - ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs 
/id - ɢᴇᴛ ᴛʜᴇ ᴄʜᴀᴛ ɪᴅ ᴏғ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ
/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ 
☞︎︎︎ ɴᴏᴛᴇ - ғᴏʀɢᴇᴛ ɴᴏᴛ ᴛᴏ ᴛʜᴀɴᴋs ᴏᴡɴᴇʀ : [ᴘɪʀᴏᴋɪᴅ](t.me/vivekevil)
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ  ғᴏʀᴄᴇ sᴜʙ 


ᴍʏ ᴏᴡɴᴇʀ : [❥︎❥︎𝐼𝑇𝑆𝑀𝐸ت︎𝑽𝑰𝑽𝑬𝑲 亗](t.me/vivekevil)


sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : [ɴᴏᴏʙ ᴄʀᴇᴀᴛᴏʀ](t.me/noobcreator)
    """
