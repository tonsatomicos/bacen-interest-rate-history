from abc import ABC, abstractmethod
from typing import Tuple

import pandas as pd


class IExtractService(ABC):
    @abstractmethod
    def extract_data(self) -> Tuple[pd.DataFrame, str, bool]:
        pass
