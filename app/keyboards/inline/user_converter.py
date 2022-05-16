from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_selecting_menu() -> InlineKeyboardMarkup:
    """ The main keyboard for selecting the type of file conversion """
    items_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("⚪️ Word (.docx)", callback_data="from_word"),
             InlineKeyboardButton("▪️", callback_data="to_word")],
            [InlineKeyboardButton("⚪️ Exel (.xlsx)", callback_data="from_exel"),
             InlineKeyboardButton("▪️", callback_data="to_exel")],
            [InlineKeyboardButton("⚪️ PDF (.pdf)", callback_data="from_pdf"),
             InlineKeyboardButton("▪️", callback_data="to_pdf")],
            [InlineKeyboardButton("⚪️ Презентация (.pptx)", callback_data="from_pptx"),
             InlineKeyboardButton("▪️", callback_data="to_pptx")],
            [InlineKeyboardButton("⚪️ Фото (.jpg/.png)", callback_data="from_photo"),
             InlineKeyboardButton("▪️", callback_data="to_photo")],
            [InlineKeyboardButton("🔙", callback_data="main_menu")]
        ]
    )

    return items_kb


def choose_from_type(user_select: str) -> InlineKeyboardMarkup:
    """ Something like radio-buttons """
    chosen_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⚪️ Word (.docx)", callback_data="from_word"),
         InlineKeyboardButton("⚪️ Word (.docx)", callback_data="to_word")],
        [InlineKeyboardButton("⚪️ Exel (.xlsx)", callback_data="from_exel"),
         InlineKeyboardButton("⚪️ Exel (.xlsx)", callback_data="to_exel")],
        [InlineKeyboardButton("⚪️ PDF (.pdf)", callback_data="from_pdf"),
         InlineKeyboardButton("⚪️ PDF (.pdf)", callback_data="to_pdf")],
        [InlineKeyboardButton("⚪️ Презентация (.pptx)", callback_data="from_pptx"),
         InlineKeyboardButton("⚪️ Презентация (.pptx)", callback_data="to_pptx")],
        [InlineKeyboardButton("⚪️ Фото (.jpg/.png)", callback_data="from_photo"),
         InlineKeyboardButton("⚪️ Фото (.jpg/.png)", callback_data="to_photo")],
        [InlineKeyboardButton("🔙", callback_data="main_menu")]
    ])

    """ Here i try change keyboard like radio-buttons kb, i think it's look like sheet... """
    for buttons_row in chosen_kb.inline_keyboard[:-1]:  # because last button is 'back'
        from_button: InlineKeyboardButton = buttons_row[0]
        to_button: InlineKeyboardButton = buttons_row[1]

        if to_button.callback_data == user_select.replace("from", "to"):
            """ Need delete this button, it's like covert from .doc to .doc """
            to_button.text = "▪️"
            to_button.callback_data = "no_permission"

        if from_button.callback_data == user_select:
            """ If it's pressed button, set it like active """
            from_button.text = from_button.text.replace("⚪️", "🔘")

    return chosen_kb
