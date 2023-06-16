fetch("http://cvlab.cse.msu.edu/cvl-demo/DR-GAN-DEMO/upload.php", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryFSz01mRYvgYjgWj6",
    "upgrade-insecure-requests": "1"
  },
  "referrer": "http://cvlab.cse.msu.edu/cvl-demo/DR-GAN-DEMO/index.html",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"face.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"ptx1\"\r\n\r\n124\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"pty1\"\r\n\r\n72.125\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"ptx2\"\r\n\r\n138\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"pty2\"\r\n\r\n84.125\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"ptx3\"\r\n\r\n124\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"pty3\"\r\n\r\n112.125\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"ptx4\"\r\n\r\n100\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"pty4\"\r\n\r\n102.125\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"ptx5\"\r\n\r\n93\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6\r\nContent-Disposition: form-data; name=\"pty5\"\r\n\r\n80.125\r\n------WebKitFormBoundaryFSz01mRYvgYjgWj6--\r\n",
  "method": "POST",
  "mode": "cors",
  "credentials": "omit"
});