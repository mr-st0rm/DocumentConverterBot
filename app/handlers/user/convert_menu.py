from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from app.keyboards.inline import user_converter as user_convert_kb
from app.keyboards.reply import user_reply as user_r_kb
from app.states.user_states import ConverterMenu
from app.messages.user import converter_msgs, start_msgs


async def converter_menu(message: types.Message):
    """ Send user dialog inline keyboard with available document types """
    await message.answer(converter_msgs.choose_documents_types(),
                         reply_markup=user_convert_kb.main_selecting_menu())
    await ConverterMenu.choose_from_type.set()


async def back_to_main_menu(call: types.CallbackQuery, state: FSMContext):
    """ Delete message and send main menu keyboard """
    await state.finish()
    await call.message.delete()
    await call.message.answer(start_msgs.welcome_user(call.from_user.full_name),
                              reply_markup=user_r_kb.bot_main_keyboard())


async def choose_from_document_type(call: types.CallbackQuery, state: FSMContext):
    """ Choose from which document make converting """
    user_data = await state.get_data()
    user_choose_type = call.data

    if user_data.get('from_doc') == user_choose_type:
        await call.answer(converter_msgs.already_chosen_type(), show_alert=True)
        return

    await call.message.edit_reply_markup(reply_markup=user_convert_kb.choose_from_type(user_choose_type))
    await state.update_data(from_doc=user_choose_type)


async def user_no_permission(call: types.CallbackQuery):
    await call.answer(converter_msgs.same_types(), show_alert=True)


async def choose_to_document_type(call: types.CallbackQuery, state: FSMContext):
    """ Choose to which type make convert or return user back """
    user_state_data = await state.get_data()

    if not user_state_data.get("from_doc"):
        await call.answer(converter_msgs.choose_from_convert_type(), show_alert=True)
        return

    await state.update_data(to_doc=call.data)
    await call.message.edit_text(text=str(await state.get_data()))
    await state.finish()


def register_converter_handlers(dp: Dispatcher):
    dp.register_message_handler(converter_menu, Text("🔄 Конвертировать файл"), state="*")

    dp.register_callback_query_handler(back_to_main_menu, text="main_menu", state=ConverterMenu)
    dp.register_callback_query_handler(user_no_permission, text="no_permission", state=ConverterMenu)

    dp.register_callback_query_handler(choose_from_document_type, text_startswith="from_",
                                       state=ConverterMenu.choose_from_type)
    dp.register_callback_query_handler(choose_to_document_type, text_startswith="to_",
                                       state=ConverterMenu)
