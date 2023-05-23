from PIL import Image
import utils
import ML



# Usage example



def callback_function(inputImageFilePath):
    output_file_path = utils.toOutput(inputImageFilePath)

    ML.model_chain_starter(inputImageFilePath, output_file_path)
    
    return output_file_path;