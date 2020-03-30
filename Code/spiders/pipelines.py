from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)
    
# Association Table for content to title, link, teaser and publiaction relationship between Quote and Tag
article_tag = Table('article_tag',Base.metadata,
                    Column('article_tag',Integer, ForeignKey('article.id')),
                    Column('tag_id',Integer,ForeignKey('tag.id'))
                   )

class title(Base):
    __tablename_ = "title"
    
    id = Column(Integer, primary_key=True)
    article_content = Column('article_content', Text())
    title_id = 
    tags = relationship('title',secondary='article_content')
    
class teaser(Base):
    __tablename__ = "teaser"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(30), unique=True)
    quotes = relationship('teaser', secondary='article_content',
        lazy='dynamic', backref="tag")  
    
class link(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    name = Column('link', String(30), unique=True)
    quotes = relationship('link', secondary='article_content',
        lazy='dynamic', backref="tag")  
    
    
# create the pipeline to save items to the database
class SaveArticlePipline(object):
    def __init__(self): 
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        article_content = article_content()
        title = title()
        teaser = teaser()
        publication = publication()
        
    try:
        session.add(article_content)
        session.commit()
        
    return item


