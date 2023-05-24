import React, { useState } from 'react'
import './ImageSection.css'
const BASE_URL = 'http://127.0.0.1:8000';
import axios from 'axios';
export default function ImageSection() {

    var img;
    const [selectedImage, setSelectedImage] = useState(null);
    const [selectedImageFile, setSelectedImageFile] = useState(null);
    const [outputImageFile, setOutputImageFile] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        console.log(file);
        setSelectedImageFile(file);
        setSelectedImage(URL.createObjectURL(file));
    };
    const handleUpload = () => {
        if (selectedImage) {
            const formData = new FormData();
            console.log(selectedImageFile);
            formData.append('image', selectedImageFile);

            axios.post(BASE_URL + '/upload-image/', formData)
                .then(response => {
                    // Handle the response after successful image upload
                    setOutputImageFile(response.data.outputImagePath);
                })
                .catch(error => {
                    // Handle any errors that occurred during the image upload
                    console.error(error);
                });
        }
    };


    return (
        <div className='imagesection--container' >
            <h1 className='imagesection--header'>
                IMAGE SECTION
            </h1>
            <div className="imageframe--container">

                {!selectedImage && <div className="imagebox">
                    Select and Image
                </div>}
                {selectedImage && <img className="imagebox" src={selectedImage} alt="Selected" />}
                <button onClick={handleUpload} className='process--button'>Process</button>

                {!outputImageFile && <div className="imagebox">
                    Output Image
                </div>}
                {outputImageFile && <img className="imagebox" src={outputImageFile} alt="Selected" />}

            </div>
            <input type="file" accept="image/*" onChange={handleImageChange} />
        </div >
    )
}