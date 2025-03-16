from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./database.db"  # Change to PostgreSQL/MySQL if needed
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """Initialize the database and create tables"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency to get a database session"""
    with Session(engine) as session:
        yield session
