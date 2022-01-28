from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(legend):
    LEGEND = legend.pattern_match.group(1)
    if not LEGEND:
        if legend.is_reply:
            (await legend.get_reply_message()).message
        else:
            await edit_or_reply(
                legend,
                "`Sir please give some query to search and download it for you..!`",
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(LEGEND))}")

    await troll[0].click(
        legend.chat_id,
        reply_to=legend.reply_to_msg_id,
        silent=True if legend.is_reply else False,
        hide_via=True,
    )
    await legend.delete()


CmdHelp("memevoice").add_command(
    "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
