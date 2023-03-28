from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_user_id = Column(BigInteger, nullable=False, unique=True)
    telegram_chat_id = Column(BigInteger, nullable=False, unique=True)
    telegram_username = Column(String(255))    
    subscriptions_id = Column(Integer, ForeignKey('subscriptions.id'), nullable=True)
    
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    subscriptions = relationship("Subscription", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")
       
    sub_start_date = Column(DateTime(timezone=True))
    sub_end_date = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.telegram_username!r})"


class Subscription(Base):
    __tablename__ = "subscriptions"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, default=0)

    user = relationship('User', back_populates='subscriptions')
    transactions = relationship('Transaction', back_populates='subscriptions')

    def __repr__(self):
        return f"Subscription(id={self.id!r}, title={self.title!r}, price={self.price!r}, user_id={self.user_id!r})"
    
    
class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    total = Column(Integer, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'), nullable=False)

    user = relationship('User', back_populates='transactions')
    subscriptions = relationship('Subscription', back_populates='transactions')

    def __repr__(self):
        return f"Transaction(id={self.id!r}, title={self.title!r}, total={self.total!r}, user_id={self.user_id!r}, subscription_id={self.subscription_id!r})"
    


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    image_url = Column(String)
    status = Column(String)
    game_url = Column(String)
    
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    time_end = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"Game(id={self.id!r}, title={self.title!r}, image_url={self.image_url!r}, status={self.status!r}, game_url={self.game_url!r}, timestamp={self.timestamp!r}, time_end={self.time_end!r})"
    
    
class GameDetail(Base):
    __tablename__ = "game_details"

    id = Column(Integer, primary_key=True)
    game_fk = Column(Integer, ForeignKey('games.id'), nullable=False)
    short_desc = Column(String)
    genres = Column(String)
    features = Column(String)
    specifications = relationship("GameDetailSpecifications", backref="game_details")

    def __repr__(self):
        return f"GameDetail(id={self.id!r}, title={self.title!r})"
    
    
class GameDetailSpecifications(Base):
    __tablename__ = "game_detail_specifications"

    id = Column(Integer, primary_key=True)
    game_detail = Column(Integer, ForeignKey('game_details.id'), nullable=False)
    type = Column(String)
    os = Column(String)
    cpu = Column(String)
    gpu = Column(String)
    memory = Column(String)
    space = Column(String)

    def __repr__(self):
        return f"GameDetailSpecifications(id={self.id!r}, game_detail={self.game_detail!r})"
    
  
# TODO: Future   
# class GameGenres(Base):
#     __tablename__ = "game_genres"

#     id = Column(Integer, primary_key=True)
#     game_detail = Column(Integer, ForeignKey('game_details.id'), nullable=False)
#     os = Column(String)
#     cpu = Column(String)
#     gpu = Column(String)
#     memory = Column(String)
#     space = Column(String)
    
#     time_end = Column(DateTime(timezone=True))

#     def __repr__(self):
#         return f"GameDetailSpecifications(id={self.id!r}, game_detail={self.game_detail!r})"
    

# class GameFeatures(Base):
#     __tablename__ = "game_features"

#     id = Column(Integer, primary_key=True)
#     game_detail = Column(Integer, ForeignKey('game_details.id'), nullable=False)
#     os = Column(String)
#     cpu = Column(String)
#     gpu = Column(String)
#     memory = Column(String)
#     space = Column(String)
    
#     time_end = Column(DateTime(timezone=True))

#     def __repr__(self):
#         return f"GameDetailSpecifications(id={self.id!r}, game_detail={self.game_detail!r})"