
from datetime import datetime, timedelta
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select, update
from sqlalchemy import desc
from sqlalchemy.sql.expression import bindparam

from .models import User, Game, GameDetail, GameDetailSpecifications
from .engine import engine


class db_queries:
    
    def create_user(telegram_user_id, telegram_chat_id, telegram_username):
        try:
            with Session(engine) as session:
                user = User(
                    telegram_user_id = telegram_user_id,
                    telegram_chat_id = telegram_chat_id,
                    telegram_username = telegram_username,
                )
                session.add(user)
                session.commit()
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')


    def create_game(title, image_url, status, game_url, time_end):
        try:
            with Session(engine) as session:
                if not session.query(Game).filter(Game.title == title).filter(Game.time_end == time_end).first():
                    game = Game(
                        title = title,
                        image_url = image_url,
                        status = status,
                        game_url = game_url,
                        time_end = time_end,
                    )
                    session.add(game)
                    session.commit()
                    session.close()
                    return True
                else:
                    session.close()
                    return False
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')
            
            
    def create_game_detail(title, short_desc, genres, features, game_id):
        try:
            with Session(engine) as session:
                try:
                    game = session.query(Game).filter(Game.title == title).first()
                    if session.query(GameDetail).filter(GameDetail.game_fk == game.id).first():
                        session.refresh(session.query(GameDetail).filter(GameDetail.game_fk == game.id).first())
                except:
                    pass
                
                if not session.query(GameDetail).filter(GameDetail.short_desc == short_desc).first():
                        game = session.query(Game).filter(Game.title == title).first()
                        game_detail = GameDetail(
                            game_fk = game.id,
                            short_desc = short_desc,
                            genres = genres,
                            features = features,
                        )
                        
                        session.add(game_detail)
                        session.commit()
                        session.close()
                        return game_detail
                else:
                    if not session.query(GameDetail).filter(GameDetail.game_fk == game_id).first():
                        game = session.query(Game).filter(Game.title == title).first()
                        game_detail = GameDetail(
                            game_fk = game_id,
                            short_desc = short_desc,
                            genres = genres,
                            features = "Redistribution " + features,
                            )
                        session.add(game_detail)
                        session.commit()
                        session.close()
                        return game_detail
                    # else:
                    #     game_detail = session.query(GameDetail).filter(GameDetail.short_desc == short_desc).first()
                    #     session.close()
                    
                        
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')
            
    
    def create_game_detail_specifications(game_detail_id, type, os, cpu, gpu, memory, space):
        try:
            with Session(engine) as session:
                if not session.query(GameDetailSpecifications).filter(GameDetailSpecifications.game_detail == game_detail_id).filter(GameDetailSpecifications.type == type).first():
                    game_detail_specifications = GameDetailSpecifications(
                        game_detail = game_detail_id,
                        type = type,
                        os = os,
                        cpu = cpu,
                        gpu = gpu,
                        memory = memory,
                        space = space,
                    )
                    
                    session.add(game_detail_specifications)
                    session.commit()
                    session.close()
                    return game_detail_specifications
                else:
                    session.close()
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')
            
            
    def get_game(status=None, time=None):
        try:
            with Session(engine) as session:
                if session.query(Game).first() == None:
                    return None 
                if status == None:
                    if time != None:
                        return session.query(Game).filter(Game.time_end == time)
                    else:    
                        return session.query(Game)
                else:
                    if time != None:
                        return session.query(Game).filter(Game.status == status).filter(Game.time_end == time)
                    else:
                        return session.query(Game).filter(Game.status == status)
                
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')
    
    
    def get_game_detail(game_id):
        try:
            with Session(engine) as session:
                return session.query(GameDetail).filter(GameDetail.game_fk == game_id).first()
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')
            
            
    def get_game_by_title(title):
        try:
            with Session(engine) as session:
                return session.query(Game).filter(Game.title == title).order_by(desc(Game.timestamp)).first()
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')
    
    
    def get_game_detail_specifications(game_detail_id, type):
        try:
            with Session(engine) as session:
                return session.query(GameDetailSpecifications).filter(GameDetailSpecifications.game_detail == game_detail_id).filter(GameDetailSpecifications.type == type).first()
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')


    def get_users():
        try:
            with Session(engine) as session:
                user = session.query(User)
                session.close()
                return user
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')

    def get_user_by_id(user_id):
        try:
            with Session(engine) as session:
                return session.query(User).filter(User.id == user_id).first()
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')



    def get_user_by_telegram_user_id(telegram_user_id):
        try:
            with Session(engine) as session:
                return session.query(User).filter(User.telegram_user_id == telegram_user_id).first()
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')

    
    def get_last_game():
        try:
            with Session(engine) as session:
                return session.query(Game).order_by(desc(Game.timestamp)).limit(4)
        except Exception as e:
            print(f'Запрос не выполнени по причине: TypeError: {type(e).__name__}: {e}.')
