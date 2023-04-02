import sys
sys.path.append('src')
import logging

from cache_worker.cache_worker import cache_worker

import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from db.queries import db_queries
from common import base_keyboard, create_message

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    db_queries.create_user(telegram_user_id=message.from_user.id, telegram_chat_id=message.chat.id, telegram_username=message.from_user.username)
    await message.answer(f"Hi! {message.from_user.username}\nI'm EpicGamesInfoBot!\nPowered by Suslicke", reply_markup=base_keyboard())


@dp.message_handler(regexp="Now free")
async def now_free(message: types.Message):
    active_time = cache_worker.get_new_game_time()
    games = db_queries.get_game(status="Free Now", time=active_time)
    
    if games == None:
        await message.answer("No information in base")

    for game in games:
        game_detail = db_queries.get_game_detail(game_id=game.id)
        rec_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Recommended")
        min_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Minimum")
        
        action = create_message(game, game_detail, min_game_detail_specifications, rec_game_detail_specifications)
                                
        await message.answer(action)
    

@dp.message_handler(regexp="Soon free")
async def soon_free(message: types.Message):
    active_time = cache_worker.get_new_game_time()
    games = db_queries.get_game(status="Coming Soon", time=active_time)
    
    if games == None:
        await message.answer("No information in base")
    
    for game in games:
        game_detail = db_queries.get_game_detail(game_id=game.id)
        rec_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Recommended")
        min_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Minimum")
        
        action = create_message(game, game_detail, min_game_detail_specifications, rec_game_detail_specifications)
                                
        await message.answer(action)
    

@dp.message_handler(regexp="All")
async def all_free(message: types.Message):
    try:
        games = db_queries.get_game()
    except:
        pass
    
    if games == None:
        await message.answer("No information in base")
    
    for game in games:
        try:
            game_detail = db_queries.get_game_detail(game_id=game.id)
            rec_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Recommended")
            min_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Minimum")
        
            action = create_message(game, game_detail, min_game_detail_specifications, rec_game_detail_specifications)
            await message.answer(action)
        except:
            continue


async def broadcaster():
    while True:
        new_game = cache_worker.get_new_game()
        if new_game:
            users = db_queries.get_users()
            for user in users:
                active_time = cache_worker.get_new_game_time()
                games = db_queries.get_game(time=active_time)
                for game in games:
                    game_detail = db_queries.get_game_detail(game_id=game.id)
                    rec_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Recommended")
                    min_game_detail_specifications = db_queries.get_game_detail_specifications(game_detail_id=game_detail.id, type="Minimum")
                    
                    action = create_message(game, game_detail, min_game_detail_specifications, rec_game_detail_specifications)
                    await bot.send_message(user.telegram_chat_id, action)
                await asyncio.sleep(5)
                new = False
                cache_worker.set_new_game(new)
        await asyncio.sleep(86400)


if __name__ == '__main__':
    print("Start")
    loop_task = asyncio.ensure_future(broadcaster())
    executor.start_polling(dp)
