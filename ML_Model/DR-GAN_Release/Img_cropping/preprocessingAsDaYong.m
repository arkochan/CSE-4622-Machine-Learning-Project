function [img1] = preprocessingAsDaYong(img0, landmk0)

% face crop same as Dayong's method, 
% Using 5 landmark left_eye, right_eye, mouth_center, most_left_landmark, most_right_landmark

nLand = 5;
left_eye_indexs = [1];
right_eye_indexs = [2];
mouth_indexs = [3];
imsize = 110;
eye_to_mouth = 0.3*imsize;

    if size(landmk0, 2) == 2
        landmk0 = landmk0';
    end

    % (1) rotate the face in the image plane to make it upright based
    % on the eye positions. 
    % Xi: make two eye centers to be horizontal 
    left_eye_center = mean(landmk0(:, left_eye_indexs), 2);
    right_eye_center = mean(landmk0(:, right_eye_indexs), 2);
    theta0 = atan((right_eye_center(2)-left_eye_center(2))/(right_eye_center(1)-left_eye_center(1)));        
    theta = theta0/pi*180;
    im1 = imrotate(img0, theta, 'bicubic');
    
    [h0, w0, ~] = size(img0);
    landmk0 = landmk0 - repmat([w0/2; h0/2], 1, nLand);
    land1 = [cos(-theta0), -sin(-theta0); sin(-theta0), cos(-theta0)]*landmk0;
    [h1, w1, ~] = size(im1);
    land1 = land1 + repmat([w1/2; h1/2], 1, nLand);

    % (2) find a central point on the face by taking the mid-point
    % betweeen the leftmost and rightmost landmarks.
    [~, left] = min(land1(1,:));
    [~, right] = max(land1(1,:));
    left_most = land1(:, left);
    right_most = land1(:, right);
    central_point = (left_most + right_most) / 2;

    % (3) find the center points of the eyes and mouth by averaging all
    % landmarks in the eye and mouth regions. 
    eye_center = mean(land1(:, [left_eye_indexs right_eye_indexs]), 2);
    mouth_center = mean(land1(:, mouth_indexs), 2);

    % (4) center the face along the x-axis based on the central point
    dist1 = mouth_center(2) - eye_center(2) + 1;
    s = eye_to_mouth / dist1; % scale ratio
    x1 = round(central_point(1)- imsize/2/s);
    x2 = round(x1+imsize/s-1);

    % (5) keep the aspect ratio and fix the position along the y-axis
    % by placing the eye center point at 45% from the top of the image
    % and mouth center point at 25% from the bottom of the image
    y1 = round(eye_center(2) - imsize*0.45/s);
    y2 = round(y1+imsize/s-1);
    
%     % pad the images just in case the bbox will be out of range
    [t, l, b, r] = findPaddingPara(im1, y1, x1, y2, x2);
    im2 = facePadding(im1, t, l, b, r);
    land2 = land1 + repmat([l; t], 1, nLand); 
    
    x1 = x1 + l;
    x2 = x2 + l;
    y1 = y1 + t;
    y2 = y2 + t;
    im3 = im2(y1:y2, x1:x2, :);
    land3 = land2 - repmat([x1-1; y1-1], 1, nLand); 

    % (6) resize the width and height of the image to 110*110 
    img1 = imresize(im3, [imsize, imsize], 'bicubic');
    landmk1 = land3*s;
    
    img1 = img1(8:103,8:103,:);
    
    function [t, l, b, r] = findPaddingPara(im1, y1, x1, y2, x2)
       [height, width, ~] = size(im1);
       t = 0; l = 0; b = 0; r = 0;
       if y1 < 1
           t = -y1 + 1;
       end
       if x1 < 1
           l = -x1 + 1;
       end
       if y2 > height
           b = y2 - height + 1;
       end
       if x2 > width
           r = x2 - width + 1;
       end
    end  
    
end


