import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    date_of_birth = Column(String(11), nullable=False)
    username = Column(String (20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String (100), nullable=False)
    #likes = Column()

class Comment(Base):
    __tablename__ = 'comment'

    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String(300), nullable=False)
    comment_likes = Column(Integer)
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.post_id"))

class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key=True)
    post_description = Column(String(300))
    post_likes = Column(Integer)
    author_id = Column(Integer, ForeignKey("user.id"))
    
class Media(Base):
    __tablename__ = "media"

    media_id = Column(Integer, primary_key=True)
    media_url = Column(String(250), nullable=False)
    media_type = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("post.post_id"))

class Follower(Base):
    __tablename__ = "follower"

    from_user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    to_user_id = Column(Integer, ForeignKey("user.id"))
 
#class Like(Base):
#   __tablename__ = "like"

#    like_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
