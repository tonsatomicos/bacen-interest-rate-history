from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class DBEngine:
    def __init__(self, db_type: str, db_local: str, db_user: str, db_pass: str, db_name: str) -> None:
        self.db_type = db_type
        self.db_local = db_local
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.engine = self.create_engine()
        self.session_factory = sessionmaker(self.engine)

    def create_engine(self):
        try:
            if self.db_type == "postgresql":
                db_url = f"postgresql+psycopg2://{self.db_user}:{self.db_pass}@{self.db_local}/{self.db_name}"
            elif self.db_type == "sqlserver":
                db_url = f"mssql+pyodbc://{self.db_user}:{self.db_pass}@{self.db_local}/{self.db_name}?driver=SQL Server"
            else:
                raise ValueError("Tipo de banco de dados não suportado")

            engine = create_engine(db_url)
            return engine
        
        except SQLAlchemyError as e:
            raise RuntimeError(f"Erro ao criar engine de banco de dados: {e}")

    def get_session(self):
        return self.session_factory()
