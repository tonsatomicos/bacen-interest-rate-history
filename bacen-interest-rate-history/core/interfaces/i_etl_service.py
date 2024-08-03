from abc import ABC, abstractmethod
from typing import Tuple

import pandas as pd


class IETLService(ABC):
    @abstractmethod
    def extract_data(self) -> Tuple[pd.DataFrame, str, bool]:
        pass

    @abstractmethod
    def transform_data(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, str, bool]:
        pass

    @abstractmethod
    def load_data(self, data: pd.DataFrame) -> Tuple[str, bool]:
        pass

    @abstractmethod
    def orchestrator(self) -> None:
        pass
