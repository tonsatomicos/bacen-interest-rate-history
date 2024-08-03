from typing import Tuple

import pandas as pd
from domain.models.rate_history import RateHistory
from interfaces.i_load_service import ILoadService
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from utils.db_engine import DBEngine


class LoadService(ILoadService):
    def __init__(self, db_engine: DBEngine) -> None:
        self.db_engine = db_engine
        self.model = RateHistory

    def load_data(self, data: pd.DataFrame) -> Tuple[str, bool]:
        try:
            with self.db_engine.get_session() as s:
                for _, row in data.iterrows():
                    result = s.scalar(
                        select(self.model).where(
                            self.model.num_reuniao == row["num_reuniao"],
                            self.model.data_reuniao == row["data_reuniao"],
                            self.model.inicio_vigencia == row["inicio_vigencia"],
                        )
                    )

                    if result:

                        if (
                            result.fim_vigencia == "19000101"
                            and result.fim_vigencia != row["fim_vigencia"]
                        ):
                            result.vies_reuniao = row["vies_reuniao"]
                            result.meta_selic = row["meta_selic"]
                            result.tban = row["tban"]
                            result.taxa_selic_porcentagem = row[
                                "taxa_selic_porcentagem"
                            ]
                            result.taxa_selic_a_a = row["taxa_selic_a_a"]
                            result.fim_vigencia = row["fim_vigencia"]
                    else:
                        rate_history_entry = self.model(
                            num_reuniao=row["num_reuniao"],
                            data_reuniao=row["data_reuniao"],
                            vies_reuniao=row["vies_reuniao"],
                            meta_selic=row["meta_selic"],
                            tban=row["tban"],
                            taxa_selic_porcentagem=row["taxa_selic_porcentagem"],
                            taxa_selic_a_a=row["taxa_selic_a_a"],
                            inicio_vigencia=row["inicio_vigencia"],
                            fim_vigencia=row["fim_vigencia"],
                        )
                        s.add(rate_history_entry)
                s.commit()
                return 'Carregamento realizado com sucesso.', True

        except ValueError as e:
            message = f'Erro de configuração: {str(e)}'
            return message, False

        except IntegrityError as e:
            s.rollback()
            message = f'Erro de integridade: {e}.'
            return message, False

        except SQLAlchemyError as e:
            message = f'Erro ao interagir com o banco de dados: {str(e)}'
            return message, False

        except Exception as e:
            message = f"Erro inesperado: {str(e)}"
            return message, False
