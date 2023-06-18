import React, { useState, useEffect, useRef } from 'react'
import './ImageSection.css'
import image_transformer from './utility';
import axios from 'axios';
import { appendBaseImageUrl } from './utility';

export default function OutputImageFrame2(props) {
    const [imageUrl, setImageUrl] = useState();
    const [image, setImage] = useState(null);


    const handleImageRequest = (event) => {
        console.log(imageUrl);
        // setImageUrl('vite.svg');
        setImageUrl(appendBaseImageUrl(props.text, props.imgName));
        // setImageUrl(props.imgSrc);

    }




    return (
        <div className='inputimage--container' >
            {imageUrl ?
                (<img onClick={handleImageRequest} className='image--frame' src={imageUrl} />) :
                (<p onClick={handleImageRequest} className='image--frame' >{props.text}</p>)}
        </div>
    )
}
