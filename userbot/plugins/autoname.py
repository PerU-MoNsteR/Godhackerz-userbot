# Copyright (C) 2020 by @Godhackerzuserbot, < https://github.com/rohithaditya/Godhackerz-userbot.git>.
#
# This file is part of < https://github.com/rohithaditya/Godhackerz-userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/rohithaditya/Godhackerz-userbot/blob/main/LICENSE >
# © @Godhackerzuserbot
# All rights reserved.


"""Auto Profile Updation Commands
.autoname"""
import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from uniborg.util import admin_cmd

from userbot.exclusive import ALIVE_NAME, AUTONAME

A_N = str(AUTONAME) if AUTONAME else f"{ALIVE_NAME}"

DEL_TIME_OUT = 60


@borg.on(admin_cmd(pattern="setname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"⌚{HM} ⚡{A_N}⚡ 📆{DM}"
        logger.info(name)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        #     "Successfully Changed Profile Name For Master"
        # )
        await asyncio.sleep(DEL_TIME_OUT)
    await event.edit(f"__Auto Name Started Master ! Check Your Name Master!!!_")
