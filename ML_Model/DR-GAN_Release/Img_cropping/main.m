close all
filename_in = 'img_in.png';
filename_out = 'img_cropped.png';
img = imread(filename);

figure, imshow(img);
hold on;
x = zeros(1,5);
y = zeros(1,5);
for i=1:5
[x(i), y(i)] = ginput(1);
plot(x,y, 'g*');
end

[img1, landmk1] = preprocessingAsDaYong(img, [x;y]);

imwrite(img1, filename_out);

