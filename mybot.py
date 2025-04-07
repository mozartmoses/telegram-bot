from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, CallbackContext

# === Your Telegram Bot Token ===
BOT_TOKEN = '7732649694:AAGA-GT7zZmvGeLnoVxZM3eltRjL4P9N-I4'

# === Google Drive Direct Download PDF Links ===
pdf_data = {
    "grade6": {
        "semester1": {
            "Chapter 1 - Knowing Our Numbers": "https://drive.google.com/uc?export=download&id=13isZhwdrq2fxaDbwQ0yRgbaurx98tgdc",
            "Chapter 2 - Whole Numbers": "https://drive.google.com/uc?export=download&id=1T7Lq7nmbnu_WSIKBkFbSQ881FUYZnWiH",
            "Chapter 3 - Playing with Numbers": "https://drive.google.com/uc?export=download&id=1WqohZLKj8NnCN2Me2GvvQ6NSnI9WTdpf",
            "Chapter 4 - Basic Geometric Ideas": "https://drive.google.com/uc?export=download&id=1OZv6gZXfMqwTL6nIlc-dngFzvb3rz1tP",
            "Chapter 5 - Understanding Shapes": "https://drive.google.com/uc?export=download&id=11gfK7GT-4UJW6Td_GF0A_qDZYvOTYz7Cu",
            "Chapter 6 - Integers": "https://drive.google.com/uc?export=download&id=1XxQFTSO3DGbV8fKnxVDTtTAg3zADhwuA",
            "Chapter 7 - Fractions": "https://drive.google.com/uc?export=download&id=1umh0RlbAxeh_lptSz1F1i8cxc6-RLoRb"
        },
        "semester2": {
            "Chapter 8 - Decimals": "https://drive.google.com/uc?export=download&id=1hgJXQ3kcByY3d_iJwyfdz_udZLPNpsac",
            "Chapter 9 - Ratio and Proportion": "https://drive.google.com/uc?export=download&id=1YMBWOcXF9rg0od6Ot1qLJwZ1sczYDfEX",
            "Chapter 10 - Mensuration": "https://drive.google.com/uc?export=download&id=1KudbAVJhzUEztcWDqNOOyXrbhwpARu3b",
            "Chapter 11 - Practical Geometry": "https://drive.google.com/uc?export=download&id=1u7hi4wauGQvWKfgB8cHjKx8zJRdmfwsE",
            "Chapter 12 - Data Handling": "https://drive.google.com/uc?export=download&id=1YRTOhuQSrxdcc8nVexwxrx4xVvsrC0dj",
            "Chapter 13 - Algebra": "https://drive.google.com/uc?export=download&id=1sOeq-hBodM7BIXJigXXx9Lv_FVcsXmwS",
            "Chapter 14 - Symmetry": "https://drive.google.com/uc?export=download&id=1KU4IRnRJQnTe0bp4n6D9K1IwbfJANvdV"
        }
    },
    "grade7": {
         "semester1": {
            "Chapter 1 - Integers": "https://drive.google.com/uc?export=download&id=114BIrDO0Gwt8lomixksU2gSR_7cxYsdC",
            "Chapter 2 - Fractions": "https://drive.google.com/uc?export=download&id=182sCcvU8ono1NIQS6WOapUHYUy_N7M3C",
            "Chapter 3 - Decimals": "https://drive.google.com/uc?export=download&id=19ET1V0_l4XDbrcIr9IGoszXEFAoH1YaT",
            "Chapter 4 - Data Handling": "https://drive.google.com/uc?export=download&id=1oTcTBgRU8PlZBNPFX9GrPPWIQXT4ecuR",
            "Chapter 5 - Simple Equations": "https://drive.google.com/uc?export=download&id=1nWoCVJJfe_V8YvUnjgxlsOPtjED4cW3P",
            "Chapter 6 - Lines and Angles": "https://drive.google.com/uc?export=download&id=1GZxyo3Tes9s6xkbkpDmOPLY1G27Oj-Kg",
            "Chapter 7 - Triangle and its Properties": "https://drive.google.com/uc?export=download&id=1fC19OnIkNULQarE1P2sooTP0oXKqwVdB",
            "Chapter 8 - Congruence of Triangles": "https://drive.google.com/uc?export=download&id=1_B83ibjqUwjA4_Lt_1_lQCQIZ9tRvuqk",
            "Chapter 9 - Constructions": "https://drive.google.com/uc?export=download&id=1-R5bksrSRM-PYQb9iaA92DAT-1DOzixU"
        },
        "semester2": {
            "Chapter 10 - Comparing Quantities": "https://drive.google.com/uc?export=download&id=1GfflAJUG8W1FbI6K1xga8R2IaJt6kWCc",
            "Chapter 11 - Rational Numbers": "https://drive.google.com/uc?export=download&id=1lXpSfMuVjSqGcviBYs4UmPD4pfyYKg0q",
            "Chapter 12 - Area and Perimeter": "https://drive.google.com/uc?export=download&id=1unaeYQtmivXx-6XF0yDxXsuTSAsofaml",
            "Chapter 13 - Algebraic Expressions": "https://drive.google.com/uc?export=download&id=1Lf8XZeSc4kh_nqqfAYr-0nCJGXYHIro3",
            "Chapter 14 - Exponents and Powers": "https://drive.google.com/uc?export=download&id=15IlGcO4T1lbhRpa2EG-0_49Qxb9azB4j",
            "Chapter 15 - Symmetry": "https://drive.google.com/uc?export=download&id=1tw_syysSe0InY_FkSgfWrY2hZ1D6K54m",
            "Chapter 16 - Visualising Solid Shapes": "https://drive.google.com/uc?export=download&id=1ji3yGATgXH3gFt9NkZSKTumF8E4aM0V6"
        }
    },
    "grade8": {
         "semester1": {
            "Chapter 1 - Rational Numbers": "https://drive.google.com/uc?export=download&id=1RZ1Ewx8ZTfXx9qOfZLFiKzc3_wqCiKMV",
            "Chapter 2 - Linear Equations in One Variable": "https://drive.google.com/uc?export=download&id=1nam6dWJlM4HbrjBoSSYNeRIjWrD2_GWE",
            "Chapter 3 - Data Handling": "https://drive.google.com/uc?export=download&id=1WUWc_Dad63iqrGv01FcGRHF1o6V4P06q",
            "Chapter 4 - Squares and Square Roots": "https://drive.google.com/uc?export=download&id=1IS8FQOKBn5_UutbPWVdkdJts6ZHjXxkv",
            "Chapter 5 - Cubes and Cube Roots": "https://drive.google.com/uc?export=download&id=1n7QMjeK32FuwXGyIhGwXheMfe8V0DhYZ",
            "Chapter 6 - Introduction to Graphs": "https://drive.google.com/uc?export=download&id=1I4Y8OqlMDTcGgerPwhOXwlO-malaUko6",
            "Chapter 7 - Exponents": "https://drive.google.com/uc?export=download&id=13RLmW_y9v8861KSbhx0DBSswbxBwA_Wf",
            "Chapter 8 - Dir and Inv Proportions": "https://drive.google.com/uc?export=download&id=1hVUIQTwOPAStQApbQaYIloSRsv-JNgxm"
        },
        "semester2": {
            "Chapter 9 - Exp and Identities": "https://drive.google.com/uc?export=download&id=1KW9wDHP2Zk_PjxFeALijcRFkcyZtNwjH",
            "Chapter 10 - Comparing Quantities": "https://drive.google.com/uc?export=download&id=13WTDIiWLj4-UJw9Z35UCPAqwrcOTOBK-",
            "Chapter 11 - Mensuration": "https://drive.google.com/uc?export=download&id=19YeAcPc_DJFg4QnS2u1hUdNFtW-28YO-",
            "Chapter 12 - Factorisation": "https://drive.google.com/uc?export=download&id=1epdvLejdm1iQRe8WJATMzRgNiypTP6nx",
            "Chapter 13 - Understanding Quadrilaterals": "https://drive.google.com/uc?export=download&id=1x1ii28Uy827mMmejGK-OZZlBxcJg2T4F",
            "Chapter 14 - Practical Geometry": "https://drive.google.com/uc?export=download&id=1iz6JmvvgO_scMNr5-fYScvV9_ILu8qWn",
            "Chapter 15 - Playing with Numbers": "https://drive.google.com/uc?export=download&id=1iuuRYh6VVwNPPXgBd0WjBo0mXSO4eFKx",
            "Chapter 16 - Visualising Solid Shapes": "https://drive.google.com/uc?export=download&id=1UYWb3kW3AgtoVa_0bUuKiROrlGG-I1eL"
        }
    }
}

# === Start Command ===
def start(update, context):
    keyboard = [
        [InlineKeyboardButton(grade.title(), callback_data=f'grade|{grade}')]
        for grade in pdf_data.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        update.message.reply_text("Select your grade", reply_markup=reply_markup)
    elif update.callback_query:
        update.callback_query.edit_message_text("Select your grade", reply_markup=reply_markup)

# === Button Navigation Handler ===
def button(update, context):
    query = update.callback_query
    query.answer()
    data = query.data

    if data.startswith("grade|"):
        grade = data.split("|")[1]
        context.user_data["grade"] = grade
        keyboard = [
            [InlineKeyboardButton("Semester 1", callback_data=f"semester|semester1")],
            [InlineKeyboardButton("Semester 2", callback_data=f"semester|semester2")],
            [InlineKeyboardButton("🔙 Back", callback_data="back|start")]
        ]
        query.edit_message_text(f"Selected Grade: {grade.title()}\nChoose your semester:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("semester|"):
        semester = data.split("|")[1]
        grade = context.user_data.get("grade")
        if not grade or semester not in pdf_data[grade]:
            query.edit_message_text("Invalid selection. Please start again with /start.")
            return

        context.user_data["semester"] = semester
        chapter_buttons = [
            [InlineKeyboardButton(chap, callback_data=f"chapter|{chap}")]
            for chap in pdf_data[grade][semester]
        ]
        chapter_buttons.append([InlineKeyboardButton("🔙 Back", callback_data="back|grade")])
        query.edit_message_text(f"Grade: {grade.title()}, Semester: {semester.title()}\nSelect a chapter:",
                                reply_markup=InlineKeyboardMarkup(chapter_buttons))

    elif data.startswith("chapter|"):
        chapter = data.split("|", 1)[1]
        grade = context.user_data.get("grade")
        semester = context.user_data.get("semester")

        if grade and semester and chapter in pdf_data[grade][semester]:
            link = pdf_data[grade][semester][chapter]
            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="back|semester")]]
            query.edit_message_text(f"{chapter}\n[Download PDF]({link})", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        else:
            query.edit_message_text("Invalid chapter selection. Please start again with /start.")

    elif data.startswith("back|"):
        where = data.split("|")[1]
        if where == "start":
            start(update, context)
        elif where == "grade":
            grade = context.user_data.get("grade")
            if grade:
                start(update, context)
        elif where == "semester":
            grade = context.user_data.get("grade")
            if grade:
                query.data = f"grade|{grade}"
                button(update, context)

# === Main Bot Logic ===
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
