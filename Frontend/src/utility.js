import { BASE_IMAGE } from "./InputImageFrame";

export function appendBaseImageUrl(appendText) {
    console.log(BASE_IMAGE);
    const dotIndex = BASE_IMAGE.lastIndexOf('.');
    const baseName = BASE_IMAGE.slice(0, dotIndex);
    const extension = BASE_IMAGE.slice(dotIndex);

    return `${baseName}(${appendText})${extension}`;
}
export default appendBaseImageUrl;
