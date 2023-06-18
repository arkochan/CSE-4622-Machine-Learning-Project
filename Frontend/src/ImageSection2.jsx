import React, { useState, useEffect } from 'react'
import OutputImageFrame from './OutputImageFrame'
import OutputImageFrame2 from './OutputImageFrame2'
import InputImageFrame from './InputImageFrame';
import './ImageSection.css'
import axios from 'axios';
const BASE_URL = 'http://127.0.0.1:8000';
import { useWindowSize } from '@react-hook/window-size'

import { useImageSize } from 'react-image-size';
import { uploadImage } from './api';


const pointNames = ["Eye 1", "Eye 2", "Lips", "Ear 1", "Ear 2"]
export default function ImageSection2() {

    const [imageFileState, setImageFileState] = useState()
    const [selectedImageFileName, setSelectedImageFileName] = useState();
    const [selectedImageUrl, setSelectedImageUrl] = useState();
    const [uploadedKey, setuploadedKey] = useState(null);
    const [width, height] = useWindowSize()
    const [imageX, SetImageX] = useState()
    const [imageY, SetImageY] = useState()
    const [points, setPoints] = useState([])
    const [dimensions] = useImageSize(selectedImageUrl)
    const [cursorX, setCursorX] = useState()
    const [cursorY, setCursorY] = useState()

    const handleImageSelect = (event) => {
        const imagefile = event.target.files[0];
        setImageFileState(imagefile)
        setSelectedImageFileName(event.target.files[0].name);
        console.log(selectedImageFileName);

        const image = new Image();
        image.src = URL.createObjectURL(imagefile);
        image.onload = () => {
            console.log('Image Dimensions: YEAH');
            SetImageX(image.width);
            SetImageY(image.height);

            console.log("🚀 ~ file: ImageSection2.jsx:43 ~ handleImageSelect ~ image.width:", image.width)
            const height = image.height;

        };

        if (imagefile) {
            console.log("Image Selected");
            setSelectedImageUrl(image.src); //render

        }
    }
    useEffect(() => {
        const handleMouseMove = (event) => {
            const { clientX, clientY } = event;
            // let [widthX, frameWidth, spaceWidth] = [width, 200, 0]
            // spaceWidth = widthX / 3 - frameWidth * 2 / 3
            // let crusor_on_image = clientX - spaceWidth

            // const X = imageX / 200 * crusor_on_image
            // console.log(" crusor_on_image:", crusor_on_image)
            // console.log(" imageX:", imageX)
            // console.log(" cursorX:", cursorX)
            const Y = clientY - 105
            setCursorX(clientX);
            setCursorY(Y);
            //200   thranslates to full
            //1     thranslates to full/200 
            //X     thranslates to full/200 * x 
        };

        window.addEventListener('mousemove', handleMouseMove);

        // Clean up the event listener on component unmount
        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

    function recordClick() {

        if (points.length === 5)
            (setPoints(prev => [[cursorX, cursorY]]))
        else
            setPoints(prev => [...prev, [cursorX, cursorY]])
        console.log(points)


    }
    function uploadImageHandler() {
        uploadImage(imageFileState, points)
    }
    return (
        <div >
            <div className='imagesection--container'>
                <div className="inputimage--container">

                    <InputImageFrame recordClick={recordClick} imgSrc={selectedImageUrl} imgChange={handleImageSelect} text="Select image to process" />

                </div>

            </div>
            <div> {imageX}x{imageY}</div>
            
            <div> Current cursor X = {Math.round((imageX / 202) * (cursorX - (width / 2 - 101)))}  Y ={cursorY} </div>
            <div> </div>

            <div > {points.map((array, index) => <p>{pointNames[index]} : {array[0]},{array[1]}</p>)}</div>
            <div className="">
                {points.length === 5 && <button onClick={uploadImageHandler} >Upload Image</button>
                }</div>
            <div className='imagesection--container'>

                <div className="inputimage--container">
                    <OutputImageFrame2 imgName={selectedImageFileName} text="GAN1" />
                </div>
                <div className="inputimage--container">
                    <OutputImageFrame2 imgName={selectedImageFileName} text="GAN1" />
                </div>
            </div>
        </div >

    )
}
