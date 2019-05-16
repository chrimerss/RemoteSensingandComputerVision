'''
Docs:
    1. use Shi-Tomasi algorithm to track the corners at first image.
    2. LK algorithm to solve for (u,v) and predict for movement.
'''
import cv2
import numpy as np


# Shi-Tomasi coner detection
FEATURE_PARAMS = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

LK_PARAMS= dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                   10, 0.03))
COLOR = np.random.randint(0,255,(100,3))

def main():
    global FEATURE_PARAMS, COLOR
    cap= cv2.VideoCapture(0)
    first=True
    while True:
        ret, frame= cap.read()
        if not ret or 0xFF == ord('q'):
            break
        # add optical flow here
        if first:
            gray_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            p0 = cv2.goodFeaturesToTrack(gray_img, mask = None, **FEATURE_PARAMS)
            mask= np.zeros_like(gray_img) # to draw image
            first=False
            # print('p0: ',p0,'\nshape:',p0.shape)
        frame_gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(gray_img, frame_gray, p0, None, **LK_PARAMS)
        # print('p1:', p1.shape)
        #select good points
        good_new= p1[st==1]
        good_old= p0[st==1]
        # track changes:
        for i, (old, new) in enumerate(zip(good_old, good_new)):
            a,b= new.ravel()
            c,d= old.ravel()
            frame= cv2.line(frame, (a,b), (c,d),COLOR[i].tolist(), 2)
            frame = cv2.circle(frame,(a,b),5,(255,0,0),-1)
        # img= cv2.add(frame, mask)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

        # update good_old
        gray_img= frame_gray.copy()
        # good_new= good_new[:,np.newaxis,:]
        # print(good_new.shape)
        p0= good_new[:,np.newaxis,:].copy()

    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
