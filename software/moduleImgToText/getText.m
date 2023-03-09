%% extracts text from the given image
function text = getText(location)
orgImage = imread(location);
grayImage = imadjust(rgb2gray(orgImage));

rotImage = houghTransformation(grayImage);
% thinImage=bwmorph(rotImage,'thin',1);
% closedImage = closeImage(rotImage);

t = ocr(rotImage);
% t = ocr(thinImage);
% t = ocr(closedImage);
text = t.Text;
end

%% close image
function closedImage = closeImage(img)
g=strel('disk',10);
closedImage=imclose(img,g);
end

%% hough transform
function rotImage=houghTransformation(grayImage)
[r c]=size(grayImage);

%% edge detection
BW = edge(grayImage,'canny');

%% hough transform
[H,T,R] = hough(BW);

%% finding rho and theta which has maximum line passing through
P  = houghpeaks(H,1,'threshold',ceil(0.9*max(H(:))));
lines = houghlines(BW,T,R,P,'FillGap',0.8*c,'MinLength',40);

%% rotating the image according to theta
if(lines.theta<0)
    rotImage=imrotate_white(grayImage,(90-abs(lines.theta)));
else
    rotImage=(imrotate_white(grayImage,lines.theta-90));
end
end

%% function to rotate the image without making image black
function rotated_image = imrotate_white(image, rot_angle_degree)
RA = imref2d(size(image));
tform = affine2d([cosd(rot_angle_degree)    -sind(rot_angle_degree)     0; ...
    sind(rot_angle_degree)     cosd(rot_angle_degree)     0; ...
    0                          0                          1]);
Rout = images.spatialref.internal.applyGeometricTransformToSpatialRef(RA,tform);
Rout.ImageSize = RA.ImageSize;
xTrans = mean(Rout.XWorldLimits) - mean(RA.XWorldLimits);
yTrans = mean(Rout.YWorldLimits) - mean(RA.YWorldLimits);
Rout.XWorldLimits = RA.XWorldLimits+xTrans;
Rout.YWorldLimits = RA.YWorldLimits+yTrans;
rotated_image = imwarp(image, tform, 'OutputView', Rout, 'interp', 'cubic', 'fillvalues', 255);
end
