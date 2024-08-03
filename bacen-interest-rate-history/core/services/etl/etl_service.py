from typing import Tuple

import pandas as pd
from interfaces.i_etl_service import IETLService
from interfaces.i_extract_service import IExtractService
from interfaces.i_load_service import ILoadService
from interfaces.i_transform_service import ITransformService
from utils.log_decorator import log_decorator


class ETLService(IETLService):
    def __init__(
        self,
        extract_service: IExtractService,
        transform_service: ITransformService,
        load_service: ILoadService,
    ) -> None:
        self.data = pd.DataFrame
        self.message = ""
        self.success = False
        self.extract_service = extract_service
        self.transform_service = transform_service
        self.load_service = load_service

    @log_decorator
    def extract_data(self) -> Tuple[pd.DataFrame, str, bool]:
        return self.extract_service.extract_data()

    @log_decorator
    def transform_data(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, str, bool]:
        return self.transform_service.transform_data(data)

    @log_decorator
    def load_data(self, data: pd.DataFrame) -> Tuple[str, bool]:
        return self.load_service.load_data(data)

    @log_decorator
    def orchestrator(self) -> None:
        self.data, self.message, self.success = self.extract_data()
        if self.success:
            self.data, self.message, self.success = self.transform_data(self.data)
            if self.success:
                self.message, self.success = self.load_data(self.data)