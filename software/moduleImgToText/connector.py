import matlab.engine
import os
currDir = "E:\MAJOR_PROJECT\software\moduleImgToText"

def getText():
    eng = matlab.engine.start_matlab()
    eng.cd(currDir, nargout=0)
    x=eng.getText(os.path.join(currDir,"images\img2.jpg"))
    return x


if __name__=="__main__":
    print(getText())