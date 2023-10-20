import telebot
import requests
import urllib


TOKEN = "6020686531:AAF-SiwmrR0Tu-JsWsk8c73BL2Ii6ez2fIU"


bot = telebot.TeleBot(TOKEN)

print("BOT AKTİF EDİLDİ AB")

def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(str(e))
        return False

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1001935298236
    group_id = -1001742580044

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @illegalchecker\nChat: @MajesteSohbet"
        bot.send_message(message.chat.id, response)
        return

    response = f"🍀 Merhaba {user_name}, ({user_id})!\n\n📚 Projessor Veri Ve Analiz Botuna Hoş Geldin. Bu bot, Sistemde bulunan verileri analiz etmene yardımcı olur ve tamamen ücretsizdir\n\n📮 Sorgular Ücretsiz Olduğu İçin: @illegalchecker Katılmak Zorunludur."

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("📢 İllegal Checker", url="https://t.me/illegalchecker"),
        telebot.types.InlineKeyboardButton("💭 Majeste Sohbet", url="https://t.me/MajesteSohbet"),
        telebot.types.InlineKeyboardButton("👨🏼‍💻 İletişim", url="https://t.me/Furkanisyanedior")
    )
    markup.add(
        telebot.types.InlineKeyboardButton("🔍 Komutlar", callback_data="commands")
    )

    bot.send_message(message.chat.id, response, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "commands")
def commands(call):
    response = "👨🏼‍💻 Komutlar Menüsü :"

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("Ad Soyad", callback_data="name"),
        telebot.types.InlineKeyboardButton("TC Sorgu", callback_data="tc")
    )
    markup.add(
        telebot.types.InlineKeyboardButton("Gsm TC", callback_data="gsm_tc"),
        telebot.types.InlineKeyboardButton("TC Gsm", callback_data="tc_gsm")
    )
    markup.add(
        telebot.types.InlineKeyboardButton("Aile", callback_data="aile"),
        telebot.types.InlineKeyboardButton("TC Plus", callback_data="tc_plus")
    )
    markup.add(
        telebot.types.InlineKeyboardButton("Ek Komutlar", callback_data="extra"),
        telebot.types.InlineKeyboardButton("⬅️ Geri", callback_data="back")
    )

    bot.edit_message_text(response, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    start(call.message)

@bot.callback_query_handler(func=lambda call: call.data in ["name", "tc", "gsm_tc", "tc_gsm", "aile", "tc_plus", "extra"])
def other_commands(call):
    if call.data == "name":
        response = "Ad Soyad Sorgu Yardım:\n\n/sorgu -isim <kurbanın adı> -soyisim <kurbanın soy adı> -il <kurbanın il>\n\nİki isimli Sorgulama için -isim2 kullanabilirsiniz örnek:\n/sorgu -isim betül -isim2 berra -soyisim kapancı -il istanbul"
    elif call.data == "tc":
        response = "TC Sorgu Yardım:\n\n/tc <kurbanın tc>\n\nYardım İçin Sohbet Grubumuza Gelebilirsin. @Majestesohbet"
    elif call.data == "gsm_tc":
        response = "Gsm TC Yardım:\n\n/gsmtc <kurbanın gsm>\n\nDestek Kanalımıza Göz Atmaya Ne Dersin? @illegalchecker."
    elif call.data == "tc_gsm":
        response = "TC Gsm Yardım:\n\n/tcgsm <kurbanın tc>\n\nÇekinmeden Sohbet Edebileceğin Sohbet Grubumuza Katıl @Majestesohbet."
    elif call.data == "aile":
        response = "Aile Sorgu Yardım:\n\n/aile <kurbanın tc>\n\nHer Gün Çok Güzel Paylaşımlar Olan Kanalımıza Katıl. @illegalchecker"
    elif call.data == "tc_plus":
        response = "TC Plus Sorgu Yardım:\n\n/tcplus <kurbanın tc>\n\nSohbet Grubumuza Katılmaya Ne Dersin?"
    elif call.data == "extra":
        response = "Ekstra Komutlar:\n\n/yaz - Verdiğiniz Metni Deftere Yazar.\n\n/tekrarla Verdiğiniz Metni Tekrarlar\n\n@illegalchecker ve @Majestesohbet Katılmayı Unutma"

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("⬅️ Geri", callback_data="commands")
    )

    bot.edit_message_text(response, call.message.chat.id, call.message.message_id, reply_markup=markup)

def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(str(e))
        return False


@bot.message_handler(commands=["tc"])
def tc_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    
    channel_id = -1001935298236  
    group_id = -1001742580044  
    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @illegalchecker\nChat: @Majestesohbet"
        bot.send_message(message.chat.id, response)
        return

    
    mesaj = message.text

    
    if mesaj.startswith("/tc"):
        
        tc = mesaj.replace("/tc", "").strip()

        
        if tc.isdigit() and len(tc) == 11:
            
            api_url = f"http://213.238.177.177/o7apiservis/tc.php?&tc={tc}"

            
            response = requests.get(api_url)

            
            if response.status_code == 200:
                json_data = response.json()

                
                if "ADI" in json_data:
                    
                    adi = json_data["ADI"]
                    soyadi = json_data["SOYADI"]
                    dogum_tarihi = json_data["DOĞUMTARIHI"]
                    yas = json_data["YAŞ"]
                    nufus_il = json_data["NUFUSIL"]
                    nufus_ilce = json_data["NUFUSILCE"]
                    anne_adi = json_data["ANNEADI"]
                    anne_tc = json_data["ANNETC"]
                    baba_adi = json_data["BABAADI"]
                    baba_tc = json_data["BABATC"]

                    
                    cevap = f"""
╭━━━━━━━━━━━━━╮
┃➥ @illegalchecker
╰━━━━━━━━━━━━━╯
╭━━━━━━━━━━━━━━
┃➥ 𝖳𝖢: {tc}
┃➥ 𝖠𝖣𝖨: {adi}
┃➥ 𝖲𝖮𝖸 𝖠𝖣𝖨: {soyadi}
┃➥ 𝖣𝖮𝖦̆𝖴𝖬 𝖳𝖠𝖱𝖨𝖧𝖨: {dogum_tarihi}
┃➥ 𝖸𝖠𝖲̧: {yas}
┃➥ 𝖭𝖴𝖥𝖴𝖲𝖨𝖫: {nufus_il}
┃➥ 𝖭𝖴𝖥𝖴𝖲𝖨𝖫𝖢𝖤: {nufus_ilce}
┃➥ 𝖠𝖭𝖭𝖤 𝖠𝖣: {anne_adi}
┃➥ 𝖠𝖭𝖭𝖤 𝖳𝖢: {anne_tc}
┃➥ 𝖡𝖠𝖡𝖠 𝖠𝖣: {baba_adi}
┃➥ 𝖡𝖠𝖡𝖠 𝖳𝖢: {baba_tc}
╰━━━━━━━━━━━━━━
"""
                else:
                    
                    cevap = "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯"
            else:
                
                cevap = f"Api Hata Kodu (mert babani sikim): {response.status_code}"
        else:
            
            cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tc <kurbanın tc>\n╰──────────────────────╯"
    else:
        
        cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tc <kurbanın tc>\n╰──────────────────────╯"

    bot.send_message(message.chat.id, cevap)

def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(str(e))
        return False

@bot.message_handler(commands=["tcplus"])
def tcplus_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1001935298236  
    group_id = -1001742580044  

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @illegalchecker\nChat: @Majestesohbet"
        bot.send_message(message.chat.id, response)
        return

    mesaj = message.text

    if mesaj.startswith("/tcplus"):
        tc = mesaj.replace("/tcplus", "").strip()

        if tc:
            api_url = f"http://213.238.177.177/o7apiservis/full.php?&tc={tc}"

            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if "ADI" in json_data:
                    adi = json_data["ADI"]
                    soyadi = json_data["SOYADI"]
                    dogum_tarihi = json_data.get("DOGUMTARIHI", "")
                    yas = json_data.get("YAS", "")
                    burc = json_data.get("BURC", "")
                    ayak_no = json_data.get("AYAKNO", "")
                    kizlik_soyadi = json_data.get("KIZLIKSOYADI", "")
                    nufus_il = json_data.get("NUFUSIL", "")
                    nufus_ilce = json_data.get("NUFUSILCE", "")
                    anne_adi = json_data.get("ANNEADI", "")
                    anne_tc = json_data.get("ANNETC", "")
                    baba_adi = json_data.get("BABAADI", "")
                    baba_tc = json_data.get("BABATC", "")

                    gsm_mesaj = ""
                    for gsm in json_data.get("BABA_GSM", []):
                        gsm_numarasi = gsm.get("GSM", "")
                        operatör = gsm.get("Operatör", "")
                        gsm_mesaj += f"┃➥ GSM: {gsm_numarasi}\n┃➥ OPERATÖR: {operatör}\n"

                    cevap = f"""
╭━━━━━━━━━━━━━╮
┃➥ @illegalchecker
╰━━━━━━━━━━━━━╯
╭━━━━━━━━━━━━━━
┃➥ TC: {tc}
┃➥ ADI: {adi}
┃➥ SOY ADI: {soyadi}
┃➥ DOĞUM TARİHİ: {dogum_tarihi}
┃➥ YAŞ: {yas}
┃➥ BURÇ: {burc}
┃➥ AYAK NO: {ayak_no}
┃➥ KIZLIK SOYADI: {kizlik_soyadi}
┃➥ NUFUSIL: {nufus_il}
┃➥ NUFUSILCE: {nufus_ilce}
┃➥ ANNE ADI: {anne_adi}
┃➥ ANNE TC: {anne_tc}
┃➥ BABA ADI: {baba_adi}
┃➥ BABA TC: {baba_tc}
{gsm_mesaj}╰━━━━━━━━━━━━━━
"""
                else:
                    cevap = "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯"
            else:
                cevap = f"api hata kod: ({response.status_code}): {response.text}"
        else:
            cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tcplus <kurbanın tc>\n╰──────────────────────╯"
    else:
        cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tcplus <kurbanın tc>\n╰──────────────────────╯"

    bot.send_message(message.chat.id, cevap)

@bot.message_handler(commands=["sorgu"])
def sorgu(message):
    text = message.text
    words = text.split()
    
    isim = None
    isim2 = None
    soyisim = None
    il = None
    
    for i in range(len(words)):
        if words[i] == "-isim" and i < len(words) - 1:
            isim = words[i + 1]
        elif words[i] == "-isim2" and i < len(words) - 1:
            isim2 = words[i + 1]
        elif words[i] == "-soyisim" and i < len(words) - 1:
            soyisim = words[i + 1]
        elif words[i] == "-il" and i < len(words) - 1:
            il = words[i + 1]
    
    if not isim or not soyisim:
        bot.reply_to(message, "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /sorgu -isim <kurbanın adı> -soyisim <kurbanın soy adı> -il <kurbanın il>\n╰──────────────────────╯")
        return
    
    if isim2:
        isim_encoded = urllib.parse.quote(f"{isim} {isim2}")
    else:
        isim_encoded = urllib.parse.quote(isim)
    
    api_url = f"http://213.238.177.177/o7apiservis/adsoyad.php?&ad={isim_encoded}&soyad={soyisim}"
    
    if il:
        api_url += f"&il={il}"
    
    response = requests.get(api_url)
    data = response.json()
    
    if data["success"] == "true":
        number = data["number"]
        
        if number > 0:
            people = data["data"]
            
            for person in people:
                tc = person["TC"]
                adi = person["ADI"]
                soyadi = person["SOYADI"]
                dogumtarihi = person["DOGUMTARIHI"]
                nufusil = person["NUFUSIL"]
                nufusilce = person["NUFUSILCE"]
                anneadi = person["ANNEADI"]
                annetc = person["ANNETC"]
                babaadi = person["BABAADI"]
                babatc = person["BABATC"]
                uyruk = person["UYRUK"]
                
                info = f"""
╭━━━━━━━━━━━━━╮
┃➥ @illegalchecker
╰━━━━━━━━━━━━━╯

╭━━━━━━━━━━━━━━
┃➥TC: {tc}
┃➥ ADI: {adi}
┃➥SOY ADI: {soyadi}
┃➥ DOĞUM TARİHİ: {dogumtarihi}
┃➥ İL: {nufusil}
┃➥ İLÇE: {nufusilce}
┃➥ ANNE ADI: {anneadi}
┃➥ ANNE TC: {annetc}
┃➥ BABA ADI: {babaadi}
┃➥ BABA TC: {babatc}
┃➥ UYRUK: {uyruk}
╰━━━━━━━━━━━━━━
"""
                bot.send_message(message.chat.id, info)
        else:
            bot.reply_to(message, "Veri Bulunmadı Ah Ah.")
    else:
        bot.reply_to(message, "Api Patladı Veya Mert Apiler İle Oynadı Mertin Vereceği Max Api.")

def is_user_member(user_id, chat_id):
    
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(str(e))
        return False

@bot.message_handler(commands=["aile"])
def aile_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1001935298236
    group_id = -1001742580044
    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @illegalchecker\nChat: @Majestesohbet"
        bot.send_message(message.chat.id, response)
        return

    mesaj = message.text

    if mesaj.startswith("/aile"):
        tc = mesaj.replace("/aile", "").strip()

        if tc.isdigit() and len(tc) == 11:
            api_url = f"http://213.238.177.177/o7apiservis/aile.php?&tc={tc}"
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if json_data["success"] == "true":
                    number = json_data["number"]

                    if number > 0:
                        people = json_data["data"]
                        cevap = "╭━━━━━━━━━━━━━╮\n┃➥ @illegalchecker\n╰━━━━━━━━━━━━━╯"
                        for person in people:
                            tc = person["TC"]
                            adi = person["ADI"]
                            soyadi = person["SOYADI"]
                            dogumtarihi = person["DOGUMTARIHI"]
                            nufusil = person["NUFUSIL"]
                            nufusilce = person["NUFUSILCE"]
                            anneadi = person["ANNEADI"]
                            annetc = person["ANNETC"]
                            babaadi = person["BABAADI"]
                            babatc = person["BABATC"]
                            uyruk = person["UYRUK"]
                            yakinlik = person.get("Yakinlik")

                            info = f"""

╭━━━━━━━━━━━━━━
┃➥ TC: {tc}
┃➥ ADI: {adi}
┃➥ SOY ADI: {soyadi}
┃➥ DOĞUM TARİHİ: {dogumtarihi}
┃➥ İL: {nufusil}
┃➥ İLÇE: {nufusilce}
┃➥ ANNE ADI: {anneadi}
┃➥ ANNE TC: {annetc}
┃➥ BABA ADI: {babaadi}
┃➥ BABA TC: {babatc}
┃➥ UYRUK: {uyruk}
┃➥ YAKINLIK: {yakinlik if yakinlik else "-"}
╰━━━━━━━━━━━━━━
"""
                            cevap += info

                        bot.send_message(message.chat.id, cevap)
                    else:
                        bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")
                else:
                    bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")
            else:
                bot.reply_to(message, f"hata ({response.status_code}).")
        else:
            bot.reply_to(message, "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /aile <kurbanın tc>\n╰──────────────────────╯")
    else:
        bot.reply_to(message, "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tc <kurbanın tc>\n╰──────────────────────╯")

@bot.message_handler(commands=["tcgsm"])
def tcgsm_sorgula(message):
    
    text = message.text

    
    _, tc = text.split(" ", 1)

    
    api_url = f"http://213.238.177.177/o7apiservis/tcgsm.php?&tc={tc}"

    
    response = requests.get(api_url)
    data = response.json()

    
    if data["success"] == "true":
        number = data["number"]
        if number > 0:
            people = data["data"]
            for person in people:
                tc = person["TC"]
                gsm = person["GSM"]
                engel = person["ENGEL"]

                
                info = f"""
╭━━━━━━━━━━━━━╮
┃➥ GSM: {gsm}
┃➥ TC: {tc}
╰━━━━━━━━━━━━━╯
"""
                
                bot.send_message(message.chat.id, info)
        else:
            bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")
    else:
        bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")


@bot.message_handler(commands=["gsmtc"])
def gsmtc_sorgula(message):
    
    text = message.text

    
    _, gsm = text.split(" ", 1)

    
    api_url = f"http://213.238.177.177/o7apiservis/gsmtc.php?&gsm={gsm}"

    
    response = requests.get(api_url)
    data = response.json()

    
    if data["success"] == "true":
        number = data["number"]
        if number > 0:
            people = data["data"]
            for person in people:
                tc = person["TC"]
                gsm = person["GSM"]
                engel = person["ENGEL"]

                # Bilgileri formatla
                info = f"""
╭━━━━━━━━━━━━━╮
┃➥ GSM: {gsm}
┃➥ TC: {tc}
╰━━━━━━━━━━━━━╯
"""
                
                bot.send_message(message.chat.id, info)
        else:
            bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")
    else:
        bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")

@bot.message_handler(commands=["tekrarla"])
def tekrarla(message):
    
    metin = message.text.split(' ', 1)[-1]

    
    if not metin:
        bot.reply_to(message, "neyi")
    else:
        
        bot.reply_to(message, metin)

@bot.message_handler(commands=['yaz'])
def yaz_command(message):
    try:
        
        text = message.text.replace('/yaz ', '')

        
        formatted_text = text.replace(' ', '%20')

        
        api_url = f'http://apis.xditya.me/write?text={formatted_text}'

        
        response = requests.get(api_url)

        if response.status_code == 200:
            
            bot.send_photo(message.chat.id, photo=("@illegalchecker.jpg", response.content))
        else:
            bot.reply_to(message, 'yarrami ye.')

    except Exception as e:
        bot.reply_to(message, 'sg')

@bot.message_handler(commands=["tekrarla"])
def tekrarla(message):
    
    metin = message.text.split(' ', 1)[-1]

    
    if not metin:
        bot.reply_to(message, "neyi")
    else:
        
        bot.reply_to(message, metin)

bot.polling()