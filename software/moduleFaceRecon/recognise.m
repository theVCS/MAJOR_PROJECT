function name = recognise(loc)
    load myNet;
    faceDetector=vision.CascadeObjectDetector;

    e=imread(loc);
    bboxes =step(faceDetector,e);
    
    if(sum(sum(bboxes))~=0)
        es=imcrop(e,bboxes(1,:));
        es=imresize(es,[227 227]);
        name=classify(myNet,es);
        name=char(name);
    else
        name="no face detected";
    end
end