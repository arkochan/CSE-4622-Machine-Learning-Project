import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000';

export const uploadImage = async (imageFile) => {
    if (imageFile) {
        const formData = new FormData();
        formData.append('image', imageFile);

        try {
            const response = await axios.post(`${BASE_URL}/upload-image/`, formData);
            const uploadedImagePath = response.data.outputImagePath;
            console.log("response", uploadedImagePath);
            return uploadedImagePath;
        } catch (error) {
            console.error(error);
            return null;
        }
    }
};
