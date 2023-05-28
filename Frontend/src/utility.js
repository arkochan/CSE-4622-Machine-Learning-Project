import { BASE_IMAGE } from "./InputImageFrame";

export function appendBaseImageUrl(type, imageName) {
    console.log(BASE_IMAGE);
    // const dotIndex = BASE_IMAGE.lastIndexOf('.');
    // const baseName = BASE_IMAGE.slice(0, dotIndex);
    // const extension = BASE_IMAGE.slice(dotIndex);
    let imageUrl = 'http://localhost:8000/media/' + type + "/" + imageName;

    return imageUrl;
}
export default appendBaseImageUrl;
