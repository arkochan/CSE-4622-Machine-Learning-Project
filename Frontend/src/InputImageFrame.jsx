import React, { useState } from 'react'
import './ImageSection.css'
import image_transformer from './utility';
import axios from 'axios';
import { uploadImage } from './api';
import { appendBaseImageUrl } from './utility';

export var BASE_IMAGE;
export default function InputImageFrame(props) {

    const fileInputRef = React.useRef(null);


    const [imageUrl, setImageUrl] = useState(props.imgSrc);
    const [image, setImage] = useState(null);

    const handleImageSelect = (event) => {
        const imagefile = event.target.files[0];

        if (imagefile) {

            setImageUrl(URL.createObjectURL(imagefile)); //render
            uploadImage(imagefile).then((uploadedImagePath) => {
                BASE_IMAGE = uploadedImagePath;
                console.log("BASE IMAGE: ", BASE_IMAGE);
            }); //upload


        }
    }

    const handleClickImageSelect = (event) => {
        fileInputRef.current.click();


    }

    console.log(imageUrl);

    return (

        <div  >

            {imageUrl ?
                (<img className='image--frame' src={imageUrl} onClick={handleClickImageSelect} />) :

                (<p onClick={handleClickImageSelect} className='image--frame' >{props.text}</p>)}
            <input className='hiddeninput' type="file" ref={fileInputRef} onChange={handleImageSelect} />

        </div>

    )
}
