import requests


def telegram_bot_sendtext(bot_message):

    bot_token = "965073923:AAFiaucweNmVcqIzZybls59IGZ4Nbc7Be1s"
    bot_chatID = "-263576935"
    # bot_chatID = "573696036"
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

    return response.json()