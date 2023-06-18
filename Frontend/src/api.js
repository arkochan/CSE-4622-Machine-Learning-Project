import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000';

export const uploadImage = async (imageFile, points) => {
    if (imageFile) {
        const formData = new FormData();
        formData.append('image', imageFile);
        points.map((val, index) => {
            formData.append(`ptx${index+1}`, val[0]);
            formData.append(`pty${index+1}`, val[1]);
            return null; 
          });

        try {
            const response = await axios.post(`${BASE_URL}/upload-image/`, formData);


            const uploadedImagePath = response.data.BaseImagePath;
            console.log("uploadedImagePath" , uploadedImagePath);
            return uploadedImagePath;

        } catch (error) {
            console.error(error);
            return null;
        }
    }
};
