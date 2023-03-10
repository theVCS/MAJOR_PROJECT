import matlab.engine
import os
currDir = "E:\MAJOR_PROJECT\software\moduleFaceRecon"

def recognise():
    eng = matlab.engine.start_matlab()
    eng.cd(currDir, nargout=0)
    x=eng.recognise(os.path.join(currDir,"images/Prince Mishra/0.bmp"))
    return x


if __name__=="__main__":
    print(recognise())