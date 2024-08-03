from abc import ABC, abstractmethod
from typing import Tuple

import pandas as pd


class ITransformService(ABC):
    @abstractmethod
    def transform_data(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, str, bool]:
        pass
