% 
img=imread("snut.jpg");
imshow(img);
r=img(:,:,1);
g=img(:,:,2);
b=img(:,:,3);
figure;imshow(r);
figure;imshow(g);
figure;imshow(b);
% % figure;imshow(r+b);
% A=100;
% gg=[255*ones(A,A), 0*ones(A,A), 255*ones(A,A);
%     0*ones(A,A), 255*ones(A,A), 0*ones(A,A);
%     255*ones(A,A), 0*ones(A,A), 255*ones(A,A)];
% % figure;imshow(gg,[0 255]);
% 
clear all
for i=1:16
    for j=1:16
        A1(i,j)=max(i*16,j*16)-16;
    end
end
figure;imshow(A1,[0 255]);
imwrite(A1,'A0.jpg')


for i=1:32
    for j=1:32
        A2(i,j)=max(i*8,j*8)-8;
    end
end
figure;imshow(A2,[0 255]);
imwrite(A2,'A1.jpg')

% AA=imread("AA.jpg");
% A=0*ones(380,380,3);
% 
% AA(:,:,1);
% AA(:,:,1);
% figure;imshow(AA(:,:,3));