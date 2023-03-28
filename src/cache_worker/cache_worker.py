
import redis
import json

# pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
# redis_client = redis.Redis(connection_pool=pool)
redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)


def make_general_key(key_name):
  return f'general_{key_name}'

class cache_worker:
  
  def set_new_game(new):
    key = make_general_key('new_games')
    redis_client.set(key, json.dumps(new))
    
  def get_new_game():
    key = make_general_key('new_games')
    data = redis_client.get(key)
    message = {}
    if data:
      message = json.loads(data)
    return message
  
  def set_new_game_time(new_time):
    key = make_general_key('new_games_time')
    redis_client.set(key, json.dumps(new_time))
    
    
  def get_new_game_time():
    key = make_general_key('new_games_time')
    data = redis_client.get(key)
    message = {}
    if data:
      message = json.loads(data)
    return message
  
  
  def delete_new_game():
    key = make_general_key("new_games")
    if redis_client.get(key):
      redis_client.delete(key)
      return True
    else:
      return False