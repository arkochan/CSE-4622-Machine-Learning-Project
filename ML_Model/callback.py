from PIL import Image
import utils
import ML



# Usage example



def callback_function(inputImageFilePath , outputType):
    
    
    output_file_path = ML.model_chain_starter(inputImageFilePath, outputType)
    
    return output_file_path;