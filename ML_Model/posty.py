import os
import requests

def my_view(inputPath, outputPath, points):
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
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = inputPath
    
    # Read the image file as binary data
    

    # Set up the form data
    form_data = {
        # "fileToUpload": ("poggchamp.png", image_data, "image/png"),
        "ptx1": "80",
        "pty1": "62.1761474609375",
        "ptx2": "99",
        "pty2": "62.1761474609375",
        "ptx3": "88",
        "pty3": "96.1761474609375",
        "ptx4": "41",
        "pty4": "69.1761474609375",
        "ptx5": "104",
        "pty5": "67.1761474609375",
    }
    print(form_data)
    print(points)
    files = {
        "fileToUpload": open(image_path, "rb")
    }

    response = requests.post(url, headers=headers, data=form_data,files=files)

    
    responseText = response.text
    string  = response.text.split("\n")[-3]
    start_index = string.index("face/cropped_") + len("face/cropped_")
    end_index = string.index(".png")
    number = string[start_index:end_index]
    # print(number)
    

    image_url = "http://cvlab.cse.msu.edu/cvl-demo/DR-GAN-DEMO/rotated_face/rotated_"+number+".png"
    save_path = outputPath  # Provide the desired save path for the image

    # Send a GET request to download the image
    response = requests.get(image_url)


    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
            

        # Request was successful
        response_data = response.text  # Access the response data as text
        # Process the response data as needed
        # Request was not successful
        # Handle the error

    # Return the appropriate HTTP response
