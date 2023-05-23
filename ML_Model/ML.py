from PIL import Image


def model_chain_starter(image_path,output_path):
    # Open the image

    return demo_model(image_path,output_path )


   
    

def demo_model(image_path,output_path ):
    image = Image.open(image_path)
    # Convert the image to grayscale
    gray_image = image.convert('L')
    # Save the grayscale image
    gray_image.save(output_path)
    
    error =0## ?
    
    if error:
            return "error" 
    else:
        return output_path