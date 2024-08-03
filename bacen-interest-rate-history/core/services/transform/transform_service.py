from typing import Tuple

import pandas as pd
import pandera as pa
from interfaces.i_transform_service import ITransformService
from schema.rate_history_schema import DataSchemaRateHistory


class TransformService(ITransformService):
    def __init__(self) -> None:
        self.schema = DataSchemaRateHistory

    def transform_data(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, str, bool]:
        try:
            data.columns = data.columns.get_level_values(1)
            rename_columns = [
                "num_reuniao",
                "data_reuniao",
                "vies_reuniao",
                "periodo",
                "meta_selic",
                "tban",
                "taxa_selic_porcentagem",
                "taxa_selic_a_a",
            ]
            data.columns = rename_columns
            data["num_reuniao"] = data["num_reuniao"].str.extract("(\d+)").astype(int)
            data["data_reuniao"] = (
                pd.to_datetime(data["data_reuniao"], format="%d/%m/%Y")
                .dt.strftime("%Y%m%d")
                .fillna("19000101")
            )
            data["vies_reuniao"] = data["vies_reuniao"].fillna("N/I")
            data[["inicio_vigencia", "fim_vigencia"]] = data["periodo"].str.extract(
                r"([\d/]+)\s*-\s*(\s*[\d/]*)"
            )
            data["inicio_vigencia"] = (
                pd.to_datetime(data["inicio_vigencia"], format="%d/%m/%Y")
                .dt.strftime("%Y%m%d")
                .fillna("19000101")
            )
            data["fim_vigencia"] = (
                pd.to_datetime(data["fim_vigencia"], format="%d/%m/%Y")
                .dt.strftime("%Y%m%d")
                .fillna("19000101")
            )
            data["meta_selic"] = (data["meta_selic"].astype(float) / 100).fillna(0.0)
            data["tban"] = (data["tban"].astype(float) / 100).fillna(0.0)
            data["taxa_selic_porcentagem"] = (
                data["taxa_selic_porcentagem"].astype(float) / 100
            ).fillna(0.0)
            data["taxa_selic_a_a"] = (
                data["taxa_selic_a_a"].astype(float) / 100
            ).fillna(0.0)
            data.drop("periodo", axis=1, inplace=True)
            data.sort_values(by='num_reuniao', ascending=True, inplace=True)
            
            self.schema.validate(data)
            return data, '', True

        except pa.errors.SchemaError as e:
            message = f"Erro de validação de schema: {str(e)}"
            return pd.DataFrame(), message, False

        except Exception as e:
            message = f"Ocorreu um erro: {str(e)}"
            return pd.DataFrame(), message, False
