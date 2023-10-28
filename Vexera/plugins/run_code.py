import io
import sys
import traceback
from subprocess import getoutput as run
from pyrogram import filters
from Hydra import prefix
from Hydra import OWNER_ID
from Hydra import pub as bot


@bot.on_message(filters.user(OWNER_ID) & filters.command("logs", prefixes=prefix))
async def logs(_, m):
    run_logs = run("tail log.txt")
    msg = m.reply_text("sending logs...")
    with io.BytesIO(str.encode(run_logs)) as logs:
        logs.name = "log.txt"
        await m.reply_document(
            document=logs,
        )
    await msg.delete()


@bot.on_message(filters.user(OWNER_ID) & filters.command("sh", prefixes=prefix))
async def sh(_, message):
    mmm = await bot.send_message(message.chat.id, "processing..")
    code = message.text.replace(message.text.split(" ")[0], "")
    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message
    x1 = run(code)
    x2 = f"""
𝗜𝗡𝗣𝗨𝗧:
{code}

𝗢𝗨𝗧𝗣𝗨𝗧:
{x1}
"""
    if len(x2) > 4096:
        with io.BytesIO(str.encode(x2)) as out_file:
            out_file.name = "output.txt"
            await reply_to_.reply_document(
                document=out_file, caption=code, disable_notification=True
            )
    else:
        await reply_to_.reply_text(x2)
    await mmm.delete()


@bot.on_message(filters.user(OWNER_ID) & filters.command("eval", prefixes=prefix))
async def eval(client, message):
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.txt"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await reply_to_.reply_text(final_output)
    await status_message.delete()


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)
#under @Hyper_speed0
