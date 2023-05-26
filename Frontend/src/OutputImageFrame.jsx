import React, { useState } from 'react'
import './ImageSection.css'
import image_transformer from './utility';
import axios from 'axios';

import { appendBaseImageUrl } from './utility';
export default function OutputImageFrame(props) {


    const [imageUrl, setImageUrl] = useState();
    const [image, setImage] = useState(null);



    const handleImageRequest = (event) => {
        console.log('got ex');

        // setImageUrl('vite.svg');
        setImageUrl(appendBaseImageUrl(props.text));
        // setImageUrl(props.imgSrc);
    }

    console.log(imageUrl);

    return (

        <div  >

            {imageUrl ?
                (<img onClick={handleImageRequest} className='image--frame' src={imageUrl} />) :

                (<p onClick={handleImageRequest} className='image--frame' >{props.text}</p>)}

        </div>

    )
}
