from aiogram import types


def base_keyboard():
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

    now_free = types.KeyboardButton(text="Now free")
    soon_free = types.KeyboardButton(text="Soon free")
    all_free = types.KeyboardButton(text="All")

    keyboard_markup.add(now_free, soon_free, all_free)
    
    return keyboard_markup


def create_message(game, game_detail, min_game_detail_specifications, rec_game_detail_specifications):
    # f"💳Бывшая цена: {value[num]['Цена']}💳\n" \
    time = game.time_end.strftime("%d.%m.%Y, %H:%M:%S")
    action = f"❗ Статус: {game.status}❗️\n" \
                                f"‼️Ссылка: {game.game_url}‼️\n" \
                                f"❗️Название игры: {game.title}❗️\n" \
                                f"\n" \
                                f"🔥Дата окончания раздачи: {time}🔥️ МСК\n" \
                                f"\n" \
                                f"🔥️Жанр: {game_detail.genres}🔥️\n" \
                                f"\n" \
                                f"📖Описание: {game_detail.short_desc} 📖️\n" \
                                f"\n" \
                                f"💾Минимальные системные требования: 💾\n" \
                                f"Опреционная система: {min_game_detail_specifications.os}\n" \
                                f"Процессор: {min_game_detail_specifications.cpu}\n" \
                                f"Оперативная память: {min_game_detail_specifications.memory}\n" \
                                f"Видеокарта: {min_game_detail_specifications.gpu}\n" \
                                f"Место на диске: {min_game_detail_specifications.space}\n" \
                                f"\n" \
                                f"🖥Рекомендованные системные требования: 🖥\n" \
                                f"Опреционная система: {rec_game_detail_specifications.os} \n" \
                                f"Процессор: {rec_game_detail_specifications.cpu} \n" \
                                f"Оперативная память: {rec_game_detail_specifications.memory} \n" \
                                f"Видеокарта: {rec_game_detail_specifications.gpu}\n" \
                                f"Место на диске: {rec_game_detail_specifications.space}\n"
                                
    return action