from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def user_links() -> InlineKeyboardMarkup:
    links = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Чат", url="t.me/chat")],
        [InlineKeyboardButton("Информационный канал", url="t.me/channel")],
        [InlineKeyboardButton("Разработчик", url="t.me/chat")],
        [InlineKeyboardButton("Исходники", url="t.me/chat")],
    ])  # TODO change urls (get them from cfg)

    return links
