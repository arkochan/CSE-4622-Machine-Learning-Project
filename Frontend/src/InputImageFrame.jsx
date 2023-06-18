import React, { useState } from 'react'
import './ImageSection.css'
import image_transformer from './utility';
import axios from 'axios';
import { uploadImage } from './api';
import { appendBaseImageUrl } from './utility';

export var BASE_IMAGE;
export default function InputImageFrame(props) {
    const fileInputRef = React.useRef(null);
    const handleClickImageSelect = (event) => {
        fileInputRef.current.click();
    }
    return (
        <div className="inputimage--container " >
            {props.imgSrc ?
                (<img className='image--frame inputimage--container' src={props.imgSrc} onClick={props.recordClick} />) :
                (<p onClick={handleClickImageSelect} className='image--frame' >{props.text}</p>)}
            <input className='hiddeninput' type="file" ref={fileInputRef} onChange={props.imgChange} />
        </div >
    )
}
