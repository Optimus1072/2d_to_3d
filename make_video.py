from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import sys, os

def make_video(images, outvid=None, fps=20, size=None, is_color=True, format="XVID"):
    fourcc = VideoWriter_fourcc(*format)
    vid = None
    for image in images:
        if not os.path.exists(image):
            print("File not found. Path:", image)
        img = imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vid.write(img)
    vid.release()
    return vid

if __name__ == '__main__':
    if len(sys.argv) == 3:

        inputImageDir = sys.argv[1]
        fps = sys.argv[2]

        # Where we are, the root folder
        rootPath = os.path.dirname(os.path.abspath(__file__))

        # Where the images are found
        datasetPath = os.path.join(rootPath, inputImageDir)
        # Put the video there once it's done
        outputVideoDir = datasetPath
        print(datasetPath)

        make_video(inputImageDir, outputVideoDir, fps)
    else:
        print('Usage:')
        print('python make_video.py inputImageDir fps')

