from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIPMUSIC import app
from config import BOT_USERNAME
from VIPMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝚂𝚝𝚛𝚊𝚗𝚐𝚎𝚛 яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/ur_support07"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Rishu1286"),
          ],
               [
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/vip_robotz"),

],
[
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/RADHE_MUSIC_ROBOT"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/vip_music_vc_bot"),
              ],
              [
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/RishuXmusicXbot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-CHATBOT"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://t.me/RishuStringBot"),
InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧", url=f"https://github.com/itzshukla/STRANGER-ROBOT2.0"),
],
[
              InlineKeyboardButton("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-SPAM-X"),
              InlineKeyboardButton("𝗕𝗔𝗡𝗔𝗟𝗟 10 𝗕𝗢𝗧︎", url=f"https://github.com/itzshukla/STRANGER-BANALL-BOTS"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://github.com/itzshukla/STRANGER-SESSION-HACK"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-IDCHATBOT"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-USERBOT3.0"),
InlineKeyboardButton("𝗜𝗗-𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://t.me/Shukla_op_clone1bot"),
],
[
InlineKeyboardButton("𝗦𝗨𝗣𝗘𝗥-𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/itzshukla/STRANGER-HELLBOT"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://telegra.ph/file/d9bddd89a8070632de73e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )