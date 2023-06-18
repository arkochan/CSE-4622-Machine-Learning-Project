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
    croppedImagePath = os.path.join(MEDIA_ROOT,  "media",'images','cropped'  ,filename)   
    proceesed_output_file_path = ML.model_chain_starter(inputFilepath= inputFilepath, outputFilepath= outputFilepath, type=type ,points = points,croppedImagePath =croppedImagePath)
    print("proceesed_output_file_path" , proceesed_output_file_path)
    return proceesed_output_file_path;



def callback_function_cropped(filename):
 
    MEDIA_ROOT=Path(__file__).resolve().parent
    croppedImagePath = os.path.join(MEDIA_ROOT,  "media",'images','cropped'  ,filename)   
    print("croppedImagePath" , croppedImagePath)
    return croppedImagePath;