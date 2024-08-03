import pandera as pa
from pandera.typing import Series


class DataSchemaRateHistory(pa.DataFrameModel):
    num_reuniao: Series[int] = pa.Field(ge=0)
    data_reuniao: Series[str] = pa.Field(regex=r"\d{8}")
    vies_reuniao: Series[str] = pa.Field()
    meta_selic: Series[float] = pa.Field()
    tban: Series[float] = pa.Field()
    taxa_selic_porcentagem: Series[float] = pa.Field()
    taxa_selic_a_a: Series[float] = pa.Field()
    inicio_vigencia: Series[str] = pa.Field(regex=r"\d{8}")
    fim_vigencia: Series[str] = pa.Field(regex=r"\d{8}")
