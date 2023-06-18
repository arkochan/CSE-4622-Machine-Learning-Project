from PIL import Image
import utils
import ML
import os
from pathlib import Path

# Usage example



def callback_function(filename, type, points):


    
    MEDIA_ROOT=Path(__file__).resolve().parent
    inputFilepath = os.path.join(MEDIA_ROOT, "media",'images'  ,filename)
    outputFilepath = os.path.join(MEDIA_ROOT,  "media",'images',type  ,filename)
   
    print("inputFilepathxxxxxxxxxxxx", inputFilepath)
    print("outputFilepathxxxxxxxxxxx" , outputFilepath)
    print("callback_function points")
    print(points)    
    proceesed_output_file_path = ML.model_chain_starter(inputFilepath, outputFilepath, type ,points = points)
    print("proceesed_output_file_path" , proceesed_output_file_path)
    return proceesed_output_file_path;