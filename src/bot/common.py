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
                                f"‼️Link: {game.game_url}‼️\n" \
                                f"❗️Game name: {game.title}❗️\n" \
                                f"\n" \
                                f"🔥Giveaway end/start date: {time}🔥️ МСК\n" \
                                f"\n" \
                                f"🔥️Genres: {game_detail.genres}🔥️\n" \
                                f"\n" \
                                f"📖Features: {game_detail.features} 📖️\n" \
                                f"\n" \
                                f"📖Description: {game_detail.short_desc} 📖️\n" \
                                f"\n" \
                                f"💾Minimal system requirements: 💾\n" \
                                f"OS: {min_game_detail_specifications.os}\n" \
                                f"CPU: {min_game_detail_specifications.cpu}\n" \
                                f"RAM: {min_game_detail_specifications.memory}\n" \
                                f"GPU: {min_game_detail_specifications.gpu}\n" \
                                f"Space: {min_game_detail_specifications.space}\n" \
                                f"\n" \
                                f"Recommended system requirements: 🖥\n" \
                                f"OS: {rec_game_detail_specifications.os} \n" \
                                f"CPU: {rec_game_detail_specifications.cpu} \n" \
                                f"RAM: {rec_game_detail_specifications.memory} \n" \
                                f"GPU: {rec_game_detail_specifications.gpu}\n" \
                                f"Space: {rec_game_detail_specifications.space}\n"
                                
    return action