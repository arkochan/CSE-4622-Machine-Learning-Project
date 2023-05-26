import React, { useState } from 'react'
import OutputImageFrame from './OutputImageFrame'
import InputImageFrame from './InputImageFrame';
import './ImageSection.css'
import axios from 'axios';
const BASE_URL = 'http://127.0.0.1:8000';

import { uploadImage } from './api'



export default function ImageSection2() {

    const [selectedImageFile, setSelectedImageFile] = useState();
    const [selectedImageUrl, setSelectedImageUrl] = useState();
    const [uploadedKey, setuploadedKey] = useState(null);




    return (
        <div className='imagesection--container'>
            <div className="inputimage--container">
                <InputImageFrame imgSrc={selectedImageUrl} text="Select image to process" />

            </div>
            <div className="outputimage--container">
                <OutputImageFrame text="GAN1" />
                <OutputImageFrame text="GAN2" />
                <OutputImageFrame text="GAN3" />
                <OutputImageFrame text="GAN4" />
            </div>


        </div>
    )
}
