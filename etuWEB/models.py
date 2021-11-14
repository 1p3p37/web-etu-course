from sqlalchemy import Column, String, Integer, DateTime
from core.db import Base
#https://youtu.be/eXj1gdDLKho?t=851


"""

Посмотри видос с 14:11 который Fastapi sqlalchemy alembic | FastAPI channel

"""



class Post(Base):
    __tablename__ = "microblog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())
    user = Column(String, ForeignKey('user.id'))
    user_id = relationship("User")
    parent_id = Column(Integer, ForeignKey('microblog_posts.id'), nullable=True)
    children = relationship("Post", backref=backref('parent', remote_side=[id]))


posts = Post.__table__