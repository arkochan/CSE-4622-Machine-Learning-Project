import os
import requests

def my_view(inputFilepath, outputFilepath, type ,points ,croppedImagePath):
    url = "http://cvlab.cse.msu.edu/cvl-demo/DR-GAN-DEMO/upload.php"  # Replace with the URL
    # url = "https://webhook.site/1b4d50a3-0332-48f4-85e2-d876a96dad1f"  # Replace with the URL
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1"
    }
    referrer = "http://cvlab.cse.msu.edu/cvl-demo/DR-GAN-DEMO/index.html"  # Replace with the referrer URL

    # Replace with the path to the image file on your system
    image_path = inputFilepath
    
    # Read the image file as binary data
    

    # Set up the form data
    form_data =points 
    print(form_data)

    print("points")
    print(points)
    files = {
        "fileToUpload": open(image_path, "rb")
    }

    response = requests.post(url, headers=headers, data=form_data,files=files)

    
    responseText = response.text
    print(response.text)
    string  = response.text.split("\n")[-3] 
    start_index = string.index("face/cropped_") + len("face/cropped_")
    end_index = string.find("\"",15)
    number = string[start_index:end_index]
    print(number)
    # number ="1687114685"

    image_url = "http://cvlab.cse.msu.edu/cvl-demo/DR-GAN-DEMO/rotated_face/rotated_"+number
    save_path = outputFilepath  # Provide the desired save path for the image

    print("ImageURL" , image_url)
    # Send a GET request to download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)

    image_url = "http://cvlab.cse.msu.edu/cvl-demo/DR-GAN-DEMO/cropped_face/cropped_"+number

    # Send a GET request to download the image
    response = requests.get(image_url)


    if response.status_code == 200:
        with open(croppedImagePath, "wb") as file:
            file.write(response.content)
            
        # Request was successful
        response_data = response.text  # Access the response data as text
        # Process the response data as needed
        # Request was not successful
        # Handle the error

    # Return the appropriate HTTP response
