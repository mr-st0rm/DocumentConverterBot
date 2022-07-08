from typing import Callable
from app.messages.user.converter_msgs import send_pdf_doc, send_exel_doc, send_pptx_doc, send_word_doc, send_photo_pack


def switch_convert_msg(from_format: str) -> Callable:
    """
    Get message for user, depends on from_format
    @param from_format: string like from_{doc_type}
    @return: Callable function that return a str
    """
    from_formats: dict = {
        "from_word": send_word_doc,
        "from_exel": send_exel_doc,
        "from_pdf": send_pdf_doc,
        "from_pptx": send_pptx_doc,
        "from_photo": send_photo_pack,
    }

    return from_formats.get(from_format)


def switch_converting_func(from_format: str, to_format: str) -> Callable:
    """  Parse function for converting and return message
    @param from_format: format from converting
    @param to_format: format to converting
    @rtype: function for converting objects
    """
    if from_format == "from_word":
        if to_format == "to_exel":
            ...
        elif to_format == "to_pdf":
            ...
        elif to_format == "to_pptx":
            ...
        else:
            # to_photo
            ...

    elif from_format == "from_exel":
        if to_format == "to_word":
            ...
        elif to_format == "to_pdf":
            ...
        elif to_format == "to_pptx":
            ...
        else:
            # to photo
            ...

    elif from_format == "from_pdf":
        if to_format == "to_word":
            ...
        elif to_format == "to_exel":
            ...
        elif to_format == "to_pptx":
            ...
        else:
            # to photo
            ...

    elif from_format == "from_pptx":
        if to_format == "to_word":
            ...
        elif to_format == "to_exel":
            ...
        elif to_format == "to_pdf":
            ...
        else:
            # to photo
            ...

    else:
        # from_photo
        if to_format == "to_word":
            ...
        elif to_format == "to_exel":
            ...
        elif to_format == "to_pdf":
            ...
        else:
            # to_pptx
            ...
