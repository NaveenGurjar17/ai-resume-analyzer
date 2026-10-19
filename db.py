import ssl
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from urllib.parse import quote_plus

password = quote_plus(os.environ["DB_PASSWORD"])
DATABASE_URL = f"mysql+pymysql://2FPLWQZhSzWFDjs.root:{password}@gateway01.ap-northeast-1.prod.aws.tidbcloud.com:4000/test"


ssl_context = ssl.create_default_context()

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"ssl":{
                    "ssl":True
    }
})

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

