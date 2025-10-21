


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import json
import os
import datetime
from datetime import datetime, timedelta


def load_dictionary():
    if os.path.exists('dictionary.json'):
        with open('dictionary.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            'мыхе': 'родной',
            'хед': 'вода',
            'тыла': 'собака',
            'мащин': 'машина',
            'хыды': 'друг',
            'хал': 'дом',
            'улесды': 'еда',
            'михIман': 'гость',
            'келле': 'голова',
            'гардан': 'шея',
            'дуст': 'друг',
            'бахд': 'счастье',
            'гаьдаь': 'мальчик',
            'хейир': 'добро',
            'къаргъыш': 'заклинание',
            'совда': 'торг',
            'бухов': 'кандалы',
            'карван': 'караван',
            'маIрдды': 'щедрый',
            'пеше': 'профессия, род занятий',
            'аIмаIлдаIр': 'хитрец',
            'гьаIлаIф': 'корм',
            'зулумкар': 'деспот, угнетатель',
            'пачахI': 'царь',
            'устар': 'мастер',
            'зилдан': 'темница, наковальня',
            'чидар': 'путы',
            'джейран': 'газель',
            'балий': 'вишня',
            'диб': 'корень',
            'даьрваьзаь': 'ворота',
            'джам': 'блюдо',
            'легаIн': 'таз',
            'йургъан': 'одеяло',
            'чатIур': 'женские штаны',
            'аяз': 'безоблачное ночное небо',
            'баIнд': 'плотина, поэтическая строфа',
            'майдан': 'площадь',
            'къарпы́з': 'арбуз',
            'машма́ш': 'абрикос',
            'маши́н': 'автомобиль',
            'афто́бус': 'автобус',
            'чарх': 'арка',
            'ил': 'аромат',
            'къарг': 'баран',
            'кьа́1сды нин': 'бабушка',
            'яс': 'бык',
            'чавра́': 'бык',
            'дери́башды': 'быстрый',
            'йа́хас': 'бегать',
            'джва́гварды': 'белый',
            'дэ1бэ́1бэ1ль': 'бабочка',
            'ийва́н': 'балкон',
            'шу': 'брат',
            'Гьа́Iммиш': 'всегда',
            'Жу': 'вы',
            'Ушды́': 'ваш',
            'Мы́йед': 'восемь',
            'ЦIымы́йед': 'восемнадцать',
            'чIар': 'волос',
            'гьа́рхыд': 'высокий',
            'хьэ1д': 'весна',
            'Гьи́ле': 'где',
            'хъыц': 'грязь',
            'хыIр': 'груша',
            'бан': 'гора',
            'пIыз': 'губа',
            'гэ́IйгъaIс': 'гулять',
            'гьа́лгас': 'говорить',
            'ул': 'глаз',
            'Эй': 'да',
            'Кьвад': 'два',
            'Гьу́чIуд': 'девять',
            'Гьи́цIыд': 'десять',
            'ЦIыкьва́д': 'двенадцать',
            'ЦIыгьу́чIуд': 'девятнадцать',
            'Къа́ад': 'двадцать',
            'гьиги́т': 'джигит',
            'гьа́ас': 'делать',
            'фи́кыр ва́ас': 'думать',
            'хук': 'дерево',
            'рак': 'дверь',
            'гал': 'дверь',
            'выс': 'дать',
            'эгер': 'если',
            'ге́не': 'еще',
            'Гьа́нады': 'его, её',
            'ы́лес': 'есть',
            'къари́': 'жена',
            'гьу́Iмур': 'жизнь',
            'гьэше́миш гьи́кис': 'жить',
            'мал': 'животное',
            'ку́кды': 'жирный',
            'ухьу́н': 'живот',
            'си́гIыд': 'жаркий',
            'гIар': 'змея',
            'ши́лды': 'зеленый',
            'гъыIр': 'заяц',
            'гъи́гъи гьа́ас': 'закрывать',
            'кьы1д': 'зима',
            'Гьа́бишды': 'их',
            'гьу́лхъас': 'играть',
            'дур': 'имя',
            'на': 'и',
            'йы́мэIль': 'ищак',
            'ру́ус': 'идти',
            'руб': 'игла',
            'Гьуш': 'кто',
            'Мыс': 'когда',
            'Гьи́лаъ': 'куда',
            'э́Iбыр': 'кровь',
            'джул': 'ковер',
            'кьыры́б': 'кость',
            'кIаз': 'кувшин',
            'зер': 'корова',
            'и́рды': 'красный',
            'бытIра́д': 'красивый',
            'гьа́рай': 'крик',
            'гьарай ва́ас': 'кричать',
            'къав': 'крыша',
            'кIэIтI': 'курица',
            'ваз': 'луна',
            'хье́сым': 'лицо',
            'гыгла́д': 'левый',
            'на́выр': 'лужа',
            'сикIь': 'лиса',
            'си́пыл': 'лук',
            'ле́йчес': 'летать',
            'гъы́1льд': 'лето',
            'Жи': 'мы',
            'Изды́': 'мой',
            'дзыр': 'медь',
            'ВыгIы́л': 'муж',
            'хуIр': 'мука',
            'дерья́': 'море',
            'се́хьыд': 'мокрый',
            'Ваъ': 'нет',
            'Гьэлли́': 'никогда',
            'Ишды́': 'наш',
            'гъил': 'нога',
            'джи́кды': 'низкий',
            'хаIл': 'небо',
            'кантI': 'нож',
            'хьэхьь': 'нос',
            'Гьад': 'он, она',
            'Са': 'один',
            'ЦIыса́': 'одиннадцать',
            'цIай': 'огонь',
            'Гьа́быр': 'они',
            'гъул': 'окно',
            'ачи́х гьа́ас': 'открывать',
            'хуму́хун': 'осень',
            'Хьуд': 'пять',
            'ЦIыхьу́д': 'пятнадцать',
            'маIни́': 'песня',
            'тIили́': 'палец',
            'джил': 'пол',
            'да́дал': 'петух',
            'шуру́к': 'птица',
            'нэц1': 'река',
            'хыл': 'рука',
            'кьат1 гьа́ас': 'резать',
            'г1ал': 'рот',
            'Гъу': 'ты',
            'Выды́': 'твой',
            'Хьи́быд': 'три',
            'ЦIыхьи́быд': 'тринадцать',
            'укь': 'трава',
            'Йы́выд': 'семь',
            'ЦIыйы́выд': 'семнадцать',
            'устIу́л': 'стол',
            'выры́гъ': 'солнце',
            'шига́р': 'сахар',
            'гьикIь': 'сердце',
            'риши́': 'сестра',
            'гя́хъас': 'смотреть',
            'а́ сукьас': 'сидеть',
            'хьус': 'сказать',
            'Шив': 'что',
            'Йу́кьуд': 'четыре',
            'ЦIыйу́кьуд': 'четырнадцать',
            'лы́Iхды': 'черный',
            'кьыле́ гьаа́с': 'читать',
            'теми́з гьаа́с': 'чистить',
            'Ры́хьыд': 'шесть',
            'ЦIыры́хьыд': 'шестнадцать',
            'а́Iкьурды': 'широкий',
            'хьыв': 'хлеб',
            'зурба́д': 'храбрый',
            'гъеми́д': 'храбрый',
            'мы́кьды': 'холодный',
            'гьаIджи́зды': 'худой',
            'гьи́рхьас': 'ходить',
            'егьы́хды': 'хороший',
            'Зы': 'я',
            'къуй': 'яма',
            'миз': 'язык (анатом.)',
            'чаIл': 'язык (линг.)',
            'лугъát': 'язык (линг.)',
            'гъылы́гъ': 'яйцо',
            'э1ч': 'яблоко',
            'мизид кIеъ': 'кончик языка',
            'улид къав': 'веко',
            'гьымхь': '(в составе: гьымхь выъын косо) — взглянуть на кого-л.',
            'гьуцIа': '(в составе: гьуцIа гьыъын) — изнашивать',
            'гIарад-тIымыл': 'паслён',
            'кIвачIахъ-тIили': 'безымянный палец',
            'пIаIraIкь-чIаIraIкь': 'звукоподражание: треск, шум',
            'кIваIчIе': 'брезговать, быть противным, ненавидеть',
            'лаазим': 'использовать, пользоваться; пригодиться',
            'кIар1': 'палка',
            'кIар2': 'кадык',
            'kIар3': 'катушка',
            'ачар': 'ключ',
            'кьурукь': 'лист',
            'хьылынвалды': 'синева, синяк',
            'чIукунвалды': 'изгиб, кривизна',
            'чыхапI': 'худой человек; маленький нож',
            'аьраьдхьаьй': 'палка для чистки жерновов',
            'жваьл': 'толстая шерстяная нитка',
            'ширипIей': 'шпингалет',
            'хъыIр': 'тряпка, пелёнка',
            'хаIр': 'учить, приучать, дрессировать',
            'гьалгад': 'говорливый',
            'цIухьуд': 'пятнадцать',
            'йицIыдхьусды': 'десятый',
            'цIийывыдхьусды': 'семнадцатый',
            'хьуд': 'пять',
            'йукьа-йукьа': 'по четыре',
            'йицIа-йицIа': 'по десять',
            'гьулхъун': 'играть',
            'гьулхъас': 'инфинитив от гьулхъун',
            'хъыъыn1': 'повторительный способ: делать повторно, чинить, лечить',
            'хъулхъас': 'повторительная форма инфинитива',
            'хъулхъун': 'повторительная форма масдара',
            'мукI выъын': 'танцевать',
            'джываб вын': 'отвечать',
            'чIири гьыъын / йишин': 'портить / портиться',
            'гъигъе йишин': 'затвердевать',
            'хъуъ гьыъын / йишин': 'отодвигать / отходить',
            'лаъ лийин': 'поднимать, злить',
            'хур-хур выъын': 'храпеть',
            'рап-рап выъын': 'порхать',
            'гьаIв-гьаIв выъын': 'лаять',
            'хIаIл': 'размягчать, приводить в готовность',
            'гьудкьа': 'разрушать, обваливать',
            'хыл гъыIвхыIн / йыIвхыIн / лихьин / ливхьин': 'гладить, пожать руку, прикрывать, присваивать',
            'лийчин': 'прыгать (в сочетаниях: гъаъ лийчин, лаъ лийчин, саъ лийчин, хьуъ лийчин)',
            'гьа': 'тот',
            'ми': 'этот',
            'выдж': 'себя',
            'гьади': 'там',
            'гьадиъ': 'туда',
            'гьадаа': 'оттуда',
            'кьыIчиne': 'устало',
            'йаькваьс': 'утром',
            'анатом.': 'анатомический термин',
            'борч.-хнов.': 'борчинско-хновский диалект рутульского языка',
            'бот.': 'ботанический термин',
            'бран.': 'бранное слово',
            'букв.': 'буквально',
            'вводное сл.': 'вводное слово',
            'возвр.': 'возвратное местоимение',
            'геомет.': 'геометрический термин',
            'грам.': 'грамматика',
            'груб.': 'грубое слово',
            'детск.': 'детская речь',
            'запрет. форма': 'запретительная форма',
            'звукоизоб.': 'звукоподобразительное слово',
            'звукопод.': 'звукоподражательное слово',
            'зоол.': 'зоологический термин',
            'ирон.': 'ироничное слово',
            'ихрек.': 'ихрекский диалект рутульского языка',
            'ласкат.': 'ласкательная форма',
            'кулин.': 'кулинарный термин',
            'мед.': 'медицинский термин',
            'межд.': 'междометие',
            'мест.': 'местоимение',
            'мест. вопр.': 'местоимение вопросительное',
            'мест. притяж.': 'местоимение притяжательное',
            'миф.': 'мифологический термин',
            'мн. ч.': 'множественное число',
            'мюхрек.': 'мюхрекский диалект рутульского языка',
            'нареч.': 'наречие',
            'неодобр.': 'неодобрительное слово',
            'неопред. мест.': 'неопределённое местоимение',
            'образопод.': 'образодражательное слово',
            'орнит.': 'орнитологический термин',
            'перен.': 'переносное значение',
            'повел. накл.': 'повелительное наклонение',
            'поэт.': 'поэтическое слово',
            'редко': 'редко употребляемое слово',
            'рел.': 'религиозный термин',
            'ругат.': 'ругательное слово',
            'см.': 'смотри',
            'собств.': 'собственное имя',
            'союз соед.': 'соединительный союз',
            'союз сравнит.': 'союз сравнительный',
            'тж.': 'также',
            'указ.': 'указательное местоимение',
            'усл.': 'условный',
            'устар.': 'устаревшее',
            'шиназ.': 'шиназский диалект',
            'частиц.': 'частица',
            'числ.': 'числительное',
            "эрг.": "эргативный падеж"

        }


def save_dictionary(dictionary):
    with open('dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)


def load_user_data():
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}


def save_user_data(user_data):
    with open('user_data.json', 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=2)


def load_feedbacks():
    if os.path.exists('feedbacks.json'):
        with open('feedbacks.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []


def save_feedbacks(feedbacks):
    with open('feedbacks.json', 'w', encoding='utf-8') as f:
        json.dump(feedbacks, f, ensure_ascii=False, indent=2)


def is_admin(username):
    return username == "m001rutul"


def check_user_limit(user_id, username=None):
    user_data = load_user_data()
    user_id_str = str(user_id)

    if is_admin(username):
        return True

    if user_id_str not in user_data:
        user_data[user_id_str] = {
            'words_used': 0,
            'last_reset': datetime.now().isoformat(),
            'paid_until': None
        }
        save_user_data(user_data)
        return True

    user = user_data[user_id_str]

    if user.get('paid_until'):
        paid_until = datetime.fromisoformat(user['paid_until'])
        if paid_until < datetime.now():
            user['paid_until'] = None
            user['words_used'] = 0
            save_user_data(user_data)

    last_reset = datetime.fromisoformat(user['last_reset'])
    if last_reset.date() < datetime.now().date():
        user['words_used'] = 0
        user['last_reset'] = datetime.now().isoformat()
        save_user_data(user_data)

    if user.get('paid_until'):
        return True

    return user['words_used'] < 10


def increment_word_count(user_id, username=None):
    if is_admin(username):
        return

    user_data = load_user_data()
    user_id_str = str(user_id)

    if user_id_str in user_data:
        if not user_data[user_id_str].get('paid_until'):
            user_data[user_id_str]['words_used'] += 1
        save_user_data(user_data)


def get_remaining_words(user_id, username=None):
    if is_admin(username):
        return "∞"

    user_data = load_user_data()
    user_id_str = str(user_id)

    if user_id_str not in user_data or user_data[user_id_str].get('paid_until'):
        return "∞"

    return 10 - user_data[user_id_str]['words_used']


def activate_user_access(user_id):
    user_data = load_user_data()
    user_id_str = str(user_id)

    if user_id_str not in user_data:
        user_data[user_id_str] = {
            'words_used': 0,
            'last_reset': datetime.now().isoformat(),
            'paid_until': None
        }

    paid_until = datetime.now() + timedelta(days=30)
    user_data[user_id_str]['paid_until'] = paid_until.isoformat()
    user_data[user_id_str]['words_used'] = 0

    save_user_data(user_data)
    return paid_until


def get_user_status(user_id):
    user_data = load_user_data()
    user_id_str = str(user_id)

    if user_id_str not in user_data:
        return "❌ Не зарегистрирован"

    user = user_data[user_id_str]

    if user.get('paid_until'):
        paid_until = datetime.fromisoformat(user['paid_until'])
        if paid_until > datetime.now():
            days_left = (paid_until - datetime.now()).days
            return f"✅ Активен ({days_left} дней осталось)"
        else:
            return "❌ Подписка истекла"
    else:
        return f"🆓 Бесплатный ({user.get('words_used', 0)}/10 слов использовано)"


dictionary = load_dictionary()
user_data_dict = {}

BOT_TOKEN = "8477369141:AAH2xUwRi74CeCZRfcNrYDRC-DDjmt_KpFM"

PAYMENT_DETAILS = {
    "tinkoff": {
        "name": "Тинькофф",
        "number": "79884490537",
        "url": "https://www.tinkoff.ru/rm/yakubov.ruslan98/RSqSy49856/"
    },
}


def find_rutul_key_by_text(text):
    text_l = text.lower()
    for k in dictionary.keys():
        if k.lower() == text_l:
            return k
    return None


def build_reverse_dict():
    rev = {}
    for rutul, rus in dictionary.items():
        key = rus.lower()
        rev.setdefault(key, []).append(rutul)
    return rev


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username

    if not is_admin(username):
        await update.message.reply_text("❌ У вас нет прав администратора")
        return

    keyboard = [
        [InlineKeyboardButton("👥 Список пользователей", callback_data="admin_list_users")],
        [InlineKeyboardButton("➕ Активировать доступ", callback_data="admin_activate_user")],
        [InlineKeyboardButton("📊 Статистика", callback_data="admin_stats")],
        [InlineKeyboardButton("📝 Отзывы", callback_data="admin_feedbacks")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🛠 *Панель администратора*\n\nВыберите действие:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def handle_admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    username = query.from_user.username

    if not is_admin(username):
        await query.edit_message_text("❌ У вас нет прав администратора")
        return

    action = query.data

    if action == "admin_list_users":
        await show_users_list(query, context)
    elif action == "admin_activate_user":
        await activate_user_prompt(query, context)
    elif action == "admin_stats":
        await show_admin_stats(query, context)
    elif action == "admin_feedbacks":
        await show_feedbacks(query, context)
    elif action == "admin_back":
        await admin_command(update, context)


async def show_users_list(query, context):
    user_data = load_user_data()

    if not user_data:
        await query.edit_message_text("📝 Пользователей пока нет")
        return

    users_text = "👥 *Список пользователей:*\n\n"

    for user_id_str, user_info in list(user_data.items())[:50]:
        status = get_user_status(int(user_id_str))
        users_text += f"🆔 `{user_id_str}` - {status}\n"

    if len(user_data) > 50:
        users_text += f"\n... и еще {len(user_data) - 50} пользователей"

    keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data="admin_back")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(users_text, reply_markup=reply_markup, parse_mode='Markdown')


async def activate_user_prompt(query, context):
    context.user_data['admin_waiting_for_user_id'] = True

    await query.edit_message_text(
        "➕ *Активация доступа пользователю*\n\nВведите ID пользователя для активации доступа на 30 дней:",
        parse_mode='Markdown'
    )


async def handle_admin_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username

    if not is_admin(username):
        return

    if context.user_data.get('admin_waiting_for_user_id'):
        try:
            target_user_id = int(update.message.text.strip())
            paid_until = activate_user_access(target_user_id)

            await update.message.reply_text(
                f"✅ *Доступ активирован!*\n\n"
                f"👤 Пользователь: `{target_user_id}`\n"
                f"📅 Доступ до: {paid_until.strftime('%d.%m.%Y %H:%M')}\n"
                f"⏰ На 30 дней",
                parse_mode='Markdown'
            )

            try:
                await context.bot.send_message(
                    chat_id=target_user_id,
                    text=f"🎉 *Ваш доступ активирован!*\n\n"
                         f"✅ Теперь у вас неограниченный доступ к боту на 30 дней!\n"
                         f"📅 Доступ активен до: {paid_until.strftime('%d.%m.%Y')}\n\n"
                         f"💬 *Хотите оставить отзыв?* Используйте команду /feedback\n\n"
                         f"📢 *Наш канал:* https://t.me/Rutultranslate\n\n"
                         f"Спасибо за оплату! 🎊",
                    parse_mode='Markdown'
                )
            except:
                await update.message.reply_text("⚠ Не удалось уведомить пользователя")

            context.user_data['admin_waiting_for_user_id'] = False

        except ValueError:
            await update.message.reply_text("❌ Неверный формат ID. Введите числовой ID пользователя:")
        except Exception as e:
            await update.message.reply_text(f"❌ Ошибка: {str(e)}")


async def show_admin_stats(query, context):
    user_data = load_user_data()

    total_users = len(user_data)
    paid_users = 0
    active_paid_users = 0

    for user_info in user_data.values():
        if user_info.get('paid_until'):
            paid_users += 1
            paid_until = datetime.fromisoformat(user_info['paid_until'])
            if paid_until > datetime.now():
                active_paid_users += 1

    stats_text = (
        f"📊 *Статистика системы:*\n\n"
        f"• Всего пользователей: {total_users}\n"
        f"• С оплаченным доступом: {paid_users}\n"
        f"• Активных подписок: {active_paid_users}\n"
        f"• Бесплатных пользователей: {total_users - paid_users}\n\n"
        f"💎 Доход: {paid_users * 80} руб."
    )

    keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data="admin_back")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(stats_text, reply_markup=reply_markup, parse_mode='Markdown')


async def show_feedbacks(query, context):
    feedbacks = load_feedbacks()

    if not feedbacks:
        await query.edit_message_text("📝 Отзывов пока нет")
        return

    feedbacks_text = "📝 *Последние отзывы:*\n\n"

    for i, feedback in enumerate(feedbacks[-10:], 1):
        user_id = feedback.get('user_id', 'Неизвестно')
        text = feedback.get('text', '')
        date = feedback.get('date', '')
        feedbacks_text += f"{i}. 👤 `{user_id}`\n   📅 {date}\n   💬 {text}\n\n"

    keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data="admin_back")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(feedbacks_text, reply_markup=reply_markup, parse_mode='Markdown')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    remaining = get_remaining_words(user_id, username)

    welcome_text = f"""🤖 Привет! Я бот-переводчик с рутульского на русский и с русского на рутульский!

📝 Просто напиши слово на любом языке - я переведу его.
Напишите отзыв пожалуйста! канал(https://t.me/Rutultranslate)

🔢 Лимит использования: {remaining}/10 слов в день
💎 После исчерпания лимита доступна оплата 80 руб. за неограниченный доступ

🔤 Доступные команды:
/start - начать работу
/addword - добавить новое слово
/stats - статистика словаря
/pay - оплатить доступ
/myid - узнать свой ID
/feedback - оставить отзыв
/help - помощь
/cancel - отменить добавление"""
    await update.message.reply_text(welcome_text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    remaining = get_remaining_words(user_id, username)

    help_text = f"""📖 Как пользоваться ботом:

• Напишите слово на рутульском → получите перевод на русский
• Напишите слово на русском → получите перевод на рутульский

🔢 Осталось бесплатных слов сегодня: {remaining}
💎 Полный доступ: /pay

➕ Добавить новое слово: /addword
📊 Статистика словаря: /stats
🆔 Узнать свой ID: /myid
💬 Оставить отзыв: /feedback
❌ Отменить добавление: /cancel

📢 *Наш канал:* https://t.me/Rutultranslate"""
    await update.message.reply_text(help_text)


async def my_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "не установлен"

    await update.message.reply_text(
        f"🆔 Ваш ID: `{user_id}`\n"
        f"👤 Ваш username: @{username}\n\n"
        f"💡 *Для активации доступа:*\n"
        f"1. Оплатите 80 руб. через /pay\n"
        f"2. Отправьте чек и этот ID @m001rutul\n"
        f"3. Доступ будет активирован после проверки оплаты",
        parse_mode='Markdown'
    )


async def feedback_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username

    user_data = load_user_data()
    user_id_str = str(user_id)

    # Проверяем, есть ли у пользователя активная подписка
    has_paid_access = False
    if user_id_str in user_data and user_data[user_id_str].get('paid_until'):
        paid_until = datetime.fromisoformat(user_data[user_id_str]['paid_until'])
        if paid_until > datetime.now():
            has_paid_access = True

    if not has_paid_access:
        await update.message.reply_text(
            "💬 *Оставить отзыв могут только пользователи с оплаченным доступом*\n\n"
            "💎 Оплатите доступ через /pay чтобы оставить отзыв о работе бота!\n\n"
            "📢 *Наш канал:* https://t.me/Rutultranslate",
            parse_mode='Markdown'
        )
        return

    context.user_data['waiting_for_feedback'] = True
    await update.message.reply_text(
        "💬 *Напишите ваш отзыв о работе бота:*\n\n"
        "Расскажите, что вам нравится, что можно улучшить, или просто поделитесь впечатлениями!",
        parse_mode='Markdown'
    )


async def handle_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username

    if not context.user_data.get('waiting_for_feedback'):
        return

    feedback_text = update.message.text.strip()

    if len(feedback_text) < 5:
        await update.message.reply_text("❌ Отзыв слишком короткий. Напишите хотя бы 5 символов.")
        return

    # Сохраняем отзыв
    feedbacks = load_feedbacks()
    feedbacks.append({
        'user_id': user_id,
        'username': username,
        'text': feedback_text,
        'date': datetime.now().strftime('%d.%m.%Y %H:%M')
    })
    save_feedbacks(feedbacks)

    context.user_data['waiting_for_feedback'] = False

    await update.message.reply_text(
        "✅ *Спасибо за ваш отзыв!*\n\n"
        "Ваше мнение очень важно для нас и поможет улучшить бота!\n\n"
        "📢 *Подписывайтесь на наш канал:* https://t.me/Rutultranslate",
        parse_mode='Markdown'
    )

    # Уведомляем администратора
    try:
        admin_id = 79884490537  # Замените на ваш ID
        await context.bot.send_message(
            chat_id=admin_id,
            text=f"📝 *Новый отзыв!*\n\n"
                 f"👤 Пользователь: `{user_id}`\n"
                 f"👤 Username: @{username}\n"
                 f"💬 Отзыв: {feedback_text}",
            parse_mode='Markdown'
        )
    except:
        pass


async def pay_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data = load_user_data()
    user_id_str = str(user_id)

    if user_id_str in user_data and user_data[user_id_str].get('paid_until'):
        paid_until = datetime.fromisoformat(user_data[user_id_str]['paid_until'])
        if paid_until > datetime.now():
            await update.message.reply_text(
                f"✅ У вас уже есть активная подписка до {paid_until.strftime('%d.%m.%Y')}"
            )
            return

    keyboard = [
        [InlineKeyboardButton("💳 Тинькофф", callback_data="pay_tinkoff")],
        [InlineKeyboardButton("💳 ОзонБанк", callback_data="pay_Ozon")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    payment_text = f"""💎 *ОПЛАТА ДОСТУПА*

Стоимость: *80 руб.*
Срок доступа: *30 дней*

*Ваш ID для активации:* `{user_id}`

*После оплаты:*
1. Сохраните чек/скриншот
2. Отправьте чек и этот ID @m001rutul
3. Доступ будет активирован после проверки оплаты

*Выберите банк для оплаты:*"""

    await update.message.reply_text(payment_text, reply_markup=reply_markup, parse_mode='Markdown')


async def handle_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    bank_type = query.data.replace('pay_', '')
    bank_info = PAYMENT_DETAILS.get(bank_type)

    if bank_info:
        user_id = query.from_user.id

        payment_instructions = f"""💳 *{bank_info['name']}*

*Реквизиты для перевода:*
Номер телефона/карты: `{bank_info['number']}`
Сумма: *80 руб.*

*Ваш ID для активации:* `{user_id}`

*Или перейдите по ссылке для быстрой оплаты:*
[{bank_info['name']}]({bank_info['url']})

⚠ *Внимание:* После оплаты отправьте скриншот чека @m001rutul для проверки и активации доступа.

💬 *После активации доступа вы сможете оставить отзыв командой /feedback*"""

        keyboard = [
            [InlineKeyboardButton("🔙 К выбору банков", callback_data="back_to_banks")],
            [InlineKeyboardButton("🆔 Мой ID", callback_data="show_my_id")],
            [InlineKeyboardButton("📢 Наш канал", url="https://t.me/Rutultranslate")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            payment_instructions,
            parse_mode='Markdown',
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )


async def handle_back_to_banks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await pay_command(update, context)


async def handle_show_my_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    await query.edit_message_text(
        f"🆔 Ваш ID: `{user_id}`\n\n💡 Сообщите этот ID @m001rutul после оплаты для активации доступа.",
        parse_mode='Markdown'
    )


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username

    if update.message.document:
        await update.message.reply_text(
            f"📨 *Чек получен!*\n\n"
            f"✅ Ваш чек передан администратору\n"
            f"👤 Ваш ID: `{user_id}`\n"
            f"👤 Ваш username: @{username}\n"
            f"⏳ Доступ будет активирован после проверки оплаты\n\n"
            f"Обычно это занимает до 1 часа\n\n"
            f"💬 *После активации не забудьте оставить отзыв командой /feedback*",
            parse_mode='Markdown'
        )


async def add_word_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username

    if not check_user_limit(user_id, username):
        await update.message.reply_text("❌ Лимит слов исчерпан. Используйте /pay для получения полного доступа.")
        return

    user_data_dict[user_id] = {'step': 'waiting_rutul'}
    await update.message.reply_text("📝 Введите слово на рутульском языке:")


async def handle_add_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    text = update.message.text.strip()

    if user_id not in user_data_dict:
        await update.message.reply_text("Начните процесс добавления слова командой /addword")
        return

    step = user_data_dict[user_id].get('step')

    if step == 'waiting_rutul':
        existing = find_rutul_key_by_text(text)
        if existing:
            await update.message.reply_text(
                f"⚠ Рутульское слово '{existing}' уже есть в словаре (перевод: {dictionary[existing]}).")
            del user_data_dict[user_id]
            return

        user_data_dict[user_id] = {'step': 'waiting_russian', 'rutul_word': text}
        await update.message.reply_text(f"✅ Рутульское слово: '{text}'\nТеперь введите перевод на русский:")

    elif step == 'waiting_russian':
        rutul_word = user_data_dict[user_id]['rutul_word']
        russian_translation = text
        existing = find_rutul_key_by_text(rutul_word)
        if existing:
            await update.message.reply_text(f"⚠ Ошибка: рутульское слово '{rutul_word}' уже существует. Отмена.")
            del user_data_dict[user_id]
            return

        rev = build_reverse_dict()
        rus_l = russian_translation.lower()
        if rus_l in rev and rutul_word in rev[rus_l]:
            await update.message.reply_text("⚠ Такое сочетание уже есть в словаре.")
            del user_data_dict[user_id]
            return

        dictionary[rutul_word] = russian_translation
        save_dictionary(dictionary)
        del user_data_dict[user_id]
        increment_word_count(user_id, username)
        await update.message.reply_text(f"🎉 Слово успешно добавлено!\n📖 {rutul_word} → {russian_translation}")


async def translate_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username

    if not check_user_limit(user_id, username):
        remaining = get_remaining_words(user_id, username)
        await update.message.reply_text(
            f"❌ Лимит бесплатных слов исчерпан!\n\n"
            f"💎 Для продолжения использования оплатите доступ:\n"
            f"• 80 руб. за 30 дней неограниченного доступа\n"
            f"• Используйте команду /pay\n\n"
            f"🆔 Ваш ID для активации: `{user_id}`\n\n"
            f"После оплаты отправьте чек и ID @m001rutul для активации\n\n"
            f"📢 *Наш канал:* https://t.me/Rutultranslate",
            parse_mode='Markdown'
        )
        return

    text = update.message.text.strip()
    if not text:
        return

    if user_id in user_data_dict:
        await handle_add_word(update, context)
        return

    text_l = text.lower()
    rutul_key = find_rutul_key_by_text(text)
    if rutul_key:
        rus = dictionary[rutul_key]
        rev = build_reverse_dict()
        rus_l = rus.lower()
        rutul_variants = rev.get(rus_l, [])
        response = f"🔤 Рутульский → Русский:\n📖 {rutul_key} → {rus}\n\n"
        if rutul_variants:
            if len(rutul_variants) == 1:
                response += f"🔁 Русский → Рутульский:\n📖 {rus} → {rutul_variants[0]}"
            else:
                response += f"🔁 Русский → Рутульский:\n📖 {rus} →\n"
                for r in rutul_variants:
                    response += f"• {r}\n"

        increment_word_count(user_id, username)
        remaining = get_remaining_words(user_id, username)
        response += f"\n📊 Осталось слов: {remaining}/10"

        await update.message.reply_text(response)
        return

    rev = build_reverse_dict()
    if text_l in rev:
        rutul_variants = rev[text_l]
        response = ""
        if len(rutul_variants) == 1:
            rkey = rutul_variants[0]
            rus = dictionary[rkey]
            response += f"🔤 Русский → Рутульский:\n📖 {text} → {rkey}\n\n"
            response += f"🔁 Рутульский → Русский:\n📖 {rkey} → {rus}"
        else:
            response += f"🔁 Русский → Рутульский:\n📖 {text} →\n"
            for r in rutul_variants:
                response += f"• {r}\n"
            response += "\n🔁 Обратные пары:\n"
            for r in rutul_variants:
                response += f"• {r} → {dictionary[r]}\n"

        increment_word_count(user_id, username)
        remaining = get_remaining_words(user_id, username)
        response += f"\n📊 Осталось слов: {remaining}/10"

        await update.message.reply_text(response)
        return

    increment_word_count(user_id, username)
    remaining = get_remaining_words(user_id, username)

    await update.message.reply_text(
        f"❌ Слово '{text}' не найдено в словаре.\n"
        f"💡 Используйте команду /addword\n\n"
        f"📊 Осталось слов: {remaining}/10"
    )


async def show_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    remaining = get_remaining_words(user_id, username)

    total_words = len(dictionary)
    unique_russian = len(build_reverse_dict())
    stats_text = (
        f"📊 Статистика словаря:\n\n"
        f"• Всего рутульских слов (ключей): {total_words}\n"
        f"• Уникальных русских переводов: {unique_russian}\n"
        f"• Ваш остаток слов: {remaining}/10\n\n"
        f"📢 *Наш канал:* https://t.me/Rutultranslate"
    )
    await update.message.reply_text(stats_text)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in user_data_dict:
        del user_data_dict[user_id]
        await update.message.reply_text("❌ Процесс добавления слова отменен")
    elif context.user_data.get('waiting_for_feedback'):
        context.user_data['waiting_for_feedback'] = False
        await update.message.reply_text("❌ Отправка отзыва отменена")
    else:
        await update.message.reply_text("Нечего отменять")


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("addword", add_word_start))
app.add_handler(CommandHandler("stats", show_stats))
app.add_handler(CommandHandler("pay", pay_command))
app.add_handler(CommandHandler("myid", my_id))
app.add_handler(CommandHandler("feedback", feedback_command))
app.add_handler(CommandHandler("cancel", cancel))
app.add_handler(CommandHandler("admin", admin_command))

app.add_handler(CallbackQueryHandler(handle_payment_callback, pattern="^pay_"))
app.add_handler(CallbackQueryHandler(handle_back_to_banks, pattern="^back_to_banks$"))
app.add_handler(CallbackQueryHandler(handle_show_my_id, pattern="^show_my_id$"))
app.add_handler(CallbackQueryHandler(handle_admin_callback, pattern="^admin_"))

app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_admin_message), group=1)
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_feedback), group=2)
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_word))

print("🤖 Бот запущен!")
print("🛠 Админ-панель: /admin (для @m001rutul)")
print("📢 Канал: https://t.me/Rutultranslate")

app.run_polling()

