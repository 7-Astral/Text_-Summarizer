from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import Data_Transformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=Data_Transformation(config=data_transformation_config)
        data_transformation.convert()