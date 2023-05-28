import React, { useState } from 'react'
import OutputImageFrame from './OutputImageFrame'
import InputImageFrame from './InputImageFrame';
import './ImageSection.css'
import axios from 'axios';
const BASE_URL = 'http://127.0.0.1:8000';

import { uploadImage } from './api'



export default function ImageSection2() {


    const [selectedImageFileName, setSelectedImageFileName] = useState();
    const [selectedImageUrl, setSelectedImageUrl] = useState();
    const [uploadedKey, setuploadedKey] = useState(null);

    const handleImageSelect = (event) => {
        const imagefile = event.target.files[0];
        setSelectedImageFileName(event.target.files[0].name);
        console.log(selectedImageFileName);

        if (imagefile) {
            console.log("this runs");
            setSelectedImageUrl(URL.createObjectURL(imagefile)); //render
            console.log(selectedImageUrl);
            uploadImage(imagefile).then((uploadedImagePath) => {
                console.log(uploadedImagePath)
                BASE_IMAGE = uploadedImagePath;
                console.log("BASE IMAGE: ", BASE_IMAGE);
            }); //upload


        }
    }



    return (
        <div className='imagesection--container'>
            <div className="inputimage--container">
                <InputImageFrame imgSrc={selectedImageUrl} imgChange={handleImageSelect} text="Select image to process" />

            </div>
            <div className="outputimage--container">
                <OutputImageFrame imgName={selectedImageFileName} text="GAN1" />
                <OutputImageFrame imgName={selectedImageFileName} text="GAN2" />
                <OutputImageFrame imgName={selectedImageFileName} text="GAN3" />
                <OutputImageFrame imgName={selectedImageFileName} text="GAN4" />
            </div>


        </div>
    )
}
