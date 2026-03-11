from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎬 Kino olish")],
            [KeyboardButton(text="🪙 Tanga yig'ish"), KeyboardButton(text="🎁 Kunlik bonus")],
            [KeyboardButton(text="👥 Referal"), KeyboardButton(text="💰 Tangalarim")],
            [KeyboardButton(text="🛒 Coin sotib olish"), KeyboardButton(text="ℹ️ Yordam")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_back_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔙 Orqaga")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_referral_keyboard(link: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Do'stlarga yuborish", url=f"https://t.me/share/url?url={link}&text=Ajoyib kinolar uchun ushbu botga kiring!")]
        ]
    )

def get_tasks_keyboard(tasks):
    buttons = []
    for task in tasks:
        buttons.append([InlineKeyboardButton(text=task.name, url=task.url)])
    buttons.append([InlineKeyboardButton(text="✅ Bajarildi (Tekshirish)", callback_data="check_tasks")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
