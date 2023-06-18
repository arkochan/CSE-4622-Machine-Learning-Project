from PIL import Image,ImageEnhance
from utils import toOutput
from posty import my_view
typeArr = [
    'GAN1',
    'cropped',
    'GAN3',
    'GAN4']

def model_chain_starter(inputFilepath,croppedImagePath, outputFilepath, type ,points):
    # Open the image
    print("inputFilepath",inputFilepath)
    print("outputFilepath",outputFilepath)
    print("type",type)

    print("model_chain_starter points")
    print(points)

    if type == typeArr[0] :   
        return gan1(inputFilepath= inputFilepath, outputFilepath= outputFilepath, type=type ,points = points,croppedImagePath =croppedImagePath)
    if type == typeArr[1] :   
        return cropppedImage(inputFilepath,outputFilepath)
    if type == typeArr[2] :   
        return gan2(inputFilepath,outputFilepath)
    if type == typeArr[3] :   
        return gan4(inputFilepath,outputFilepath)
    else: 
        print("type was" ,type)


def gan1(inputFilepath, outputFilepath, type ,points ,croppedImagePath  ):
    print("model_chain_starter points")
    print(points)
    print("gan1 called")
    # image = Image.open(image_path)
    # # Convert the image to grayscale
    # gray_image = ImageEnhance.Color(image).enhance(2.0)
    # # Save the grayscale image
    # gray_image.save(output_path)
    
    error =0## ?
    my_view(inputFilepath= inputFilepath, outputFilepath= outputFilepath, type=type ,points = points,croppedImagePath =croppedImagePath)
    return outputFilepath
import time
import os
def cropppedImage(image_path,output_path ):
    count =70
    while os.path.exists(output_path)==False:
        time.sleep(.3)
        count = count-1
        if count <0:
            break       
    return output_path
def gan3(image_path,output_path ):
    image = Image.open(image_path)
    # Convert the image to grayscale
    gray_image = ImageEnhance.Color(image).enhance(.5)
    # Save the grayscale image
    gray_image.save(output_path)
    
    error =0## ?

    if error:
            return "error" 
    else:
        return output_path
    
def gan4(image_path,output_path ):
    image = Image.open(image_path)
    # Convert the image to grayscale
    gray_image = ImageEnhance.Color(image).enhance(0)
    # Save the grayscale image
    gray_image.save(output_path)
    
    error =0## ?

    if error:
            return "error" 
    else:
        return output_path