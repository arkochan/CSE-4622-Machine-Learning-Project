import React, { useState } from 'react'
import './ImageSection.css'

export default function ImageSection() {

    const [selectedImage, setSelectedImage] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        setSelectedImage(URL.createObjectURL(file));
    };

    return (
        <div className='imagesection--container' >
            <h1>
                IMAGE SECTION
            </h1>
            <div className="imageframe--container">

                {!selectedImage && <div className="imagebox">
                    left
                </div>}
                {selectedImage && <img className="imagebox" src={selectedImage} alt="Selected" />}
                <button className='process--button'>Process</button>
                <div className="imagebox">
                    Right
                </div>
            </div>
            <input type="file" accept="image/*" onChange={handleImageChange} />
        </div >
    )
}
