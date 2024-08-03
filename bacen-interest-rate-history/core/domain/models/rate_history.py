from sqlalchemy import Column, Integer, String, DECIMAL, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RateHistory(Base):
    __tablename__ = 'historico_taxas_juros'

    id_controle = Column(Integer, primary_key=True, autoincrement=True)
    num_reuniao = Column(Integer)
    data_reuniao = Column(String(8), nullable=True)
    vies_reuniao = Column(String(50), nullable=True)
    meta_selic = Column(DECIMAL(10, 2), nullable=True)
    tban = Column(DECIMAL(10, 2), nullable=True)
    taxa_selic_porcentagem = Column(DECIMAL(10, 2), nullable=True)
    taxa_selic_a_a = Column(DECIMAL(10, 2), nullable=True)
    inicio_vigencia = Column(String(8), nullable=True)
    fim_vigencia = Column(String(8), nullable=True)
