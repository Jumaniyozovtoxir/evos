from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackQueryHandler
from telegram import  KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
###  @dars_jadvali_bot        DARS JADVALINI TAXLASH BO'YICHA BOT

def battn(type=None):
    btn = []
    if type=="yillar":
        btn = [
            [KeyboardButton("2021-yil")],
            [KeyboardButton("2020-yil"),KeyboardButton("2019-yil")],
            [KeyboardButton("2018-yil"), KeyboardButton("2017-yil")]
        ]
    return ReplyKeyboardMarkup(btn,resize_keyboard=True)


def inline_battn(type=None):
    btn = []
    if type == "oylarjamlanmasi":
        btn = [
            [InlineKeyboardButton("Yanvar",callback_data="yanvar_oyi"),
             InlineKeyboardButton("Fevral",callback_data="fevral_oyi"),
             InlineKeyboardButton("Mart",callback_data="mart_oyi")],
            [InlineKeyboardButton("Aprel", callback_data="aprel_oyi"),
             InlineKeyboardButton("May", callback_data="may_oyi"),
             InlineKeyboardButton("Iyun", callback_data="iyun_oyi")],
            [InlineKeyboardButton("Iyul", callback_data="iyul_oyi"),
             InlineKeyboardButton("Avgust", callback_data="avgust_oyi"),
             InlineKeyboardButton("Sentabr", callback_data="sentabr_oyi")],
            [InlineKeyboardButton("Oktyabr", callback_data="oktyabr_oyi"),
             InlineKeyboardButton("Noyabr", callback_data="noyabr_oyi"),
             InlineKeyboardButton("Dekabr", callback_data="dekabr_oyi")]
        ]
    return InlineKeyboardMarkup(btn)
def start(updete,context):
    updete.message.reply_text("Assalomu aleykum botimizga xush kelibsizππππ",reply_markup=battn("yillar"))

def message_handler(update,context):
    msg = update.message.text
    if msg == "2021-yil":
        update.message.reply_text("Quyidagi oylardan birini tanlangππ»ππ»ππ»ππ»",reply_markup=inline_battn("oylarjamlanmasi"))

def inline_handler(update,context):
    query= update.callback_query
    data_sp = query.data.split('_')
    if data_sp[0] == "yanvar":
        if data_sp[1]== "oyi":
            context.bot.send_document(document=open("5. Π΄Π»Ρ ΠΏΠ΅ΡΠ°Ρ ΡΠ½Π²Π°ΡΡ 2021.xls","rb"),
                                      chat_id=query.message.chat_id,
                                      caption="""Yanvar oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                      reply_markup=inline_battn()

                                      )

    elif data_sp[0] == "fevral":
        if data_sp[1]== "oyi":
            context.bot.send_document(document=open("6. Π΄Π»Ρ ΠΏΠ΅ΡΠ°Ρ Π€ΠΠΠ ΠΠΠ¬ 2021 ΠΉΠΈΠ».xls","rb"),
                                      chat_id=query.message.chat_id,
                                      caption="""Fevral oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                      reply_markup=inline_battn()
                                      )

    elif data_sp[0] == "mart":
        if data_sp[1] == "oyi":
            context.bot.send_document(document=open("7. Π΄Π»Ρ ΠΏΠ΅ΡΠ°Ρ ΠΌΠ°ΡΡ 2021.xls", "rb"),
                                      chat_id=query.message.chat_id,
                                      caption="""Mart oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                      reply_markup=inline_battn()
                                      )
    elif data_sp[0] == "aprel":
        if data_sp[1] == "oyi":
            context.bot.send_document(document=open("8. Π΄Π»Ρ ΠΏΠ΅ΡΠ°Ρ ΠΠΠ ΠΠΠ¬ 2021 ΠΉΠΈΠ».xls", "rb"),
                                      chat_id=query.message.chat_id,
                                      caption="""Aprel oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                      reply_markup=inline_battn()
                                      )
    elif data_sp[0] == "may":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("9. Π΄Π»Ρ ΠΏΠ΅ΡΠ°Ρ ΠΠΠ 2021 ΠΉΠΈΠ».xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""May oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
    elif data_sp[0] == "iyun":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("11. Π΄Π»Ρ ΠΏΠ΅ΡΠ°Ρ ΠΠ?ΠΠ¬ 2021 ΠΉΠΈΠ».xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""Iyun oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
    elif data_sp[0] == "iyul":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("10. Π΄Π»Ρ ΠΏΠ΅ΡΠ°Ρ ΠΠ?ΠΠ¬ 2021 ΠΉΠΈΠ».xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""Iyul oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
    elif data_sp[0] == "avgust":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("1. pechat Avgust rasp.  3 vzvod 2021 yil.xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""Avgust oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
    elif data_sp[0] == "sentabr":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("2. Dars jadvali SENTABR 2021 yil.xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""Sentabr oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
    elif data_sp[0] == "oktabr":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("3.dars jadvali 1-kurslar oktabr uchun 2021 yil.xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""Oktabr oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
    elif data_sp[0] == "noyabr":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("4. Dars jadvali Noyabr oyi uchun  2021-yil.xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""Noyabr oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
    elif data_sp[0] == "dekabr":
        if data_sp[1] == "oyi":
                context.bot.send_document(document=open("pechat  Dekabr oyiga 2021 yil.xls", "rb"),
                                          chat_id=query.message.chat_id,
                                          caption="""Dekabr oyiga tasdiqlangan dars jadvaliπ€π€π€π€""",
                                          reply_markup=inline_battn()
                                          )
        else:
            query.message.edit_text("Umumiy dars jadvali",reply_markup=data_sp[0])

def main():
    TOKEN = "5012164802:AAGjVV6h6e6BSooECLJoq_ow2pUO41nW7ew"
    updater= Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text,message_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()