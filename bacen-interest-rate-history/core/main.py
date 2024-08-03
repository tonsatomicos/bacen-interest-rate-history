from services.etl.etl_service import ETLService
from services.extract.extract_service import ExtractService
from services.transform.transform_service import TransformService
from services.load.load_service import LoadService
from utils.db_engine import DBEngine
from config.logging_config import configure_logging


configure_logging()
db_engine = DBEngine('sqlserver','localhost:5434','sa','Teste!1234','BACEN')
#db_engine = DBEngine('postgresql','localhost:5437','admin','admin','BACEN')

extract_service = ExtractService()
transform_service = TransformService()
load_service = LoadService(db_engine)

etl_batch = ETLService(
    extract_service,
    transform_service,
    load_service
)

data = etl_batch.orchestrator()