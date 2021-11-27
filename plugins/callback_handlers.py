from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from configs import config
from core.player import player
from functions.youtube_utils import (
    prev_search,
    next_search,
    extract_info,
    stream_result
)
from functions.markup_button import process_button, start_markup

from database.lang_utils import get_message as gm
from database.chat_database import ChatDB


@Client.on_callback_query(filters.regex(pattern=r"(back|next)(music|video)\|(\d+)"))
async def _button_cb(_, cb: CallbackQuery):
    match = cb.matches[0].group
    next_or_back = match(1)
    music_or_video = match(2)
    user_id = int(match(3))
    chat_id = cb.message.chat.id
    if cb.from_user.id != user_id:
        return await cb.answer(gm(chat_id, "not_for_you"), show_alert=True)
    yt_btn = process_button(user_id, music_or_video)
    if next_or_back == "next":
        next_search(chat_id)
        btn = [
            InlineKeyboardButton("⬅️", f"back{music_or_video}|{user_id}"),
            InlineKeyboardButton("🗑️", f"close|{user_id}"),
            InlineKeyboardButton("➡️", f"next{music_or_video}|{user_id}")
        ]
    else:
        prev_search(chat_id)
        btn = [
            InlineKeyboardButton("🗑️", f"close|{user_id}"),
            InlineKeyboardButton("➡️", f"next{music_or_video}|{user_id}")
        ]
    text = extract_info(chat_id, stream_result)
    await cb.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(
            [
                yt_btn[0],
                yt_btn[1],
                btn
            ]
        )
    )


@Client.on_callback_query(filters.regex(pattern=r"((video|music) ((\d)\|(\d+)))"))
async def _music_or_video(_, cb: CallbackQuery):
    chat_id = cb.message.chat.id
    match = cb.matches[0].group
    stream_type = match(2)
    index = int(match(4))
    user_id = match(5)
    result = stream_result[chat_id][0][index]
    res = {
        "user_id": user_id,
        "title": result["title"],
        "duration": result["duration"],
        "yt_url": result["yt_url"],
        "yt_id": result["yt_id"],
        "stream_type": stream_type
    }
    await player.music_or_video(cb, res)


@Client.on_callback_query(filters.regex(pattern=r"(close)(\|(\d+))?"))
async def _close_button(_, cb: CallbackQuery):
    match = cb.matches[0].group
    try:
        user_id = int(match(3))
    except TypeError:
        user_id = None
    if cb.message.chat.type == "private" and not user_id:
        return await cb.message.delete()
    member = await cb.message.chat.get_member(cb.from_user.id)
    if member.status in ["creator", "administrator"]:
        return await cb.message.delete()
    if cb.from_user.id != user_id:
        return await cb.answer(gm(cb.message.chat.id, "not_for_you"), show_alert=True)


@Client.on_callback_query(filters.regex(pattern=r"set_lang_(.*)"))
async def _change_lang(_, cb: CallbackQuery):
    lang = cb.matches[0].group(1)
    chat_id = cb.message.chat.id
    set_lang = ChatDB().set_lang(chat_id, lang)
    await cb.message.edit(
        gm(chat_id, set_lang),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(gm(chat_id, "channel"), url="https://t.me/xmarty_updates")
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("goback"))
async def goback(client: Client, hee: CallbackQuery):
    bot_username = (await client.get_me()).username
    chid = hee.message.chat.id
    await hee.edit_message_text(
        gm(chid, "pm_greet").format(hee.message.from_user.mention),
        reply_markup=start_markup(chid, bot_username),
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, lol: CallbackQuery):
    return await lol.edit_message_text(
        gm(lol.message.chat.id, "helpmusic"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        gm(lol.message.chat.id, "backtomenu"), callback_data="goback"
                    )
                ]
            ]
        ),
    )
