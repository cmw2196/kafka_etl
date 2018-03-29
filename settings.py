from grift import BaseConfig, ConfigProperty, DictLoader
from schematics.types import BooleanType, StringType, IntType

class KafkaConfig(BaseConfig):
	"""Configuration for a basic Kafka ETL app."""
    # attribute name does not need to match the property key
    #ELASTICSEARCH_HOST = ConfigProperty(property_key='ES_HOST', property_type=StringType())
    #ELASTICSEARCH_SHARDS = ConfigProperty(property_key='ES_SHARDS', property_type=IntType(), default=5)

    # properties can be excluded from varz
    #AWS_SECRET_KEY = ConfigProperty(property_type=StringType(), exclude_from_varz=True)
	

config_dict = {
}

loaders = [DictLoader(config_dict)]

# application config
app_config = AppConfig(loaders)
