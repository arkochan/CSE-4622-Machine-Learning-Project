from PIL import Image,ImageEnhance
from utils import toOutput
from posty import my_view
typeArr = [
    'GAN1',
    'GAN2',
    'GAN3',
    'GAN4']

def model_chain_starter(inputFilepath, outputFilepath, type):
    # Open the image
    print("inputFilepath",inputFilepath)
    print("outputFilepath",outputFilepath)
    print("type",type)

    if type == typeArr[0] :   
        return gan1(inputFilepath,outputFilepath)
    if type == typeArr[1] :   
        return gan3(inputFilepath,outputFilepath)
    if type == typeArr[2] :   
        return gan2(inputFilepath,outputFilepath)
    if type == typeArr[3] :   
        return gan4(inputFilepath,outputFilepath)
    else: 
         print("type was" ,type)


def gan1(image_path,output_path ):
    print("gan1 called")
    # image = Image.open(image_path)
    # # Convert the image to grayscale
    # gray_image = ImageEnhance.Color(image).enhance(2.0)
    # # Save the grayscale image
    # gray_image.save(output_path)
    
    error =0## ?
    my_view(output_path)
    return output_path
    
def gan2(image_path,output_path ):
    image = Image.open(image_path)
    # Convert the image to grayscale
    gray_image = ImageEnhance.Color(image).enhance(1.5)
    # Save the grayscale image
    gray_image.save(output_path)
    
    error =0## ?

    if error:
            return "error" 
    else:
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