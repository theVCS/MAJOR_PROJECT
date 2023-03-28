function name = recognise()
    load myNet;
    faceDetector=vision.CascadeObjectDetector;
    cao=webcam;
    name="";

    e=cao.snapshot;
    bboxes =step(faceDetector,e);
    fcnt = size(bboxes);
    fcnt = fcnt(1);
    
    if(sum(sum(bboxes))~=0)
        for i=1:fcnt
            es=imcrop(e,bboxes(i,:));
            es=imresize(es,[227 227]);
%             figure;
%             imshow(es);
            p=classify(myNet,es);
            name=append(name, ' ', char(p));
        end
    else
        name="no face detected";
    end
end