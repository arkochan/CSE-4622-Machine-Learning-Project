from PIL import Image,ImageEnhance
from utils import toOutput

type = [
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE']

def model_chain_starter(image_path,outputType):
    # Open the image
    output_path=toOutput(image_path , outputType)

    if outputType == type[0] :   
        return gan1(image_path,output_path)
    if outputType == type[1] :   
        return gan3(image_path,output_path)
    if outputType == type[2] :   
        return gan2(image_path,output_path)
    if outputType == type[3] :   
        return gan4(image_path,output_path)



   
    

def gan1(image_path,output_path ):
    
    image = Image.open(image_path)
    # Convert the image to grayscale
    gray_image = ImageEnhance.Color(image).enhance(2.0)
    # Save the grayscale image
    gray_image.save(output_path)
    
    error =0## ?

    if error:
            return "error" 
    else:
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