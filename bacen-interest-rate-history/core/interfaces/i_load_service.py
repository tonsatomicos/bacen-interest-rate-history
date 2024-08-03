from abc import ABC, abstractmethod
from typing import Tuple

import pandas as pd


class ILoadService(ABC):
    @abstractmethod
    def load_data(self, data: pd.DataFrame) -> Tuple[str, bool]:
        pass
