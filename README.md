# Reading List

## Contents
#### 1. [Atmosphric Sciences](#atmos)
#### 2. [Remote Sensing](#remotesensing)
#### 3. [Computer Vision](#computervision)
##### 3.1 [Machine Learning Basics](#mlbasics)
##### 3.2 [Object Detection](#objectdetect)
##### 3.3 [ML/DL for Weather Prediction](#mlweather)
##### 3.4 [ML/DL for Rainfall Estimation](#mlrain)
##### 3.5 [Generative Adversaril Network](#gan)
#### 4. [Numerical Models](#numeric)
##### 4.1 [Optical Flow](#opticalflow)
##### 4.2 [Semi-Lagrangian Scheme](#semilag)
#### 5. [Updates](#updates)

## Atmospheric Sciences<a name='atmos'></a>
1. [Atmospheric Science](http://cup.aos.wisc.edu/453/2016/readings/Atmospheric_Science-Wallace_Hobbs.pdf) by JONH M. WALLACE and PETER V. HOBBS


## Remote Sensing<a name='remotesensing'></a>
1. Hydrologic Remote Sensing: Capacity Building for Sustainability and Resilience


## Computer Vision<a name='computervision'></a>
### Machine Learning Basics<a name='mlbasics'></a>

1. [神经网络与深度学习](https://github.com/nndl/nndl.github.io)
2. [Standford CS231: Convolutional Neural Networks for Visual Recognition](http://vision.stanford.edu/teaching/cs231n/)
3. [Learning kernels for CV](https://cvml.ist.ac.at/papers/lampert-fnt2009.pdf)  
    3.1 Orientation Filter: Gabor Filter   [Interesting intro](https://medium.com/@anuj_shah/through-the-eyes-of-gabor-filter-17d1fdb3ac97); [opencv](https://docs.opencv.org/4.1.0/d4/d86/group__imgproc__filter.html#gae84c92d248183bd92fa713ce51cc3599)
4. [Collection of Pytorch Lists](https://bharathgs.github.io/Awesome-pytorch-list/#cv)

### Object Detection/Tracking Generalized<a name='objectdetect'></a>
1. [Gaussian Mixture Models (GMM)](https://github.com/llSourcell/Gaussian_Mixture_Models/blob/master/intro_to_gmm_%26_em.ipynb)

### ML/DL for weather prediction<a name='mlweather'></a> ([notes](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/RainRemoval/weather.pdf)) 
1. [Generating Videos with Scene Dynamics/GAN](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/Generating_Videos_with_Scene_Dynamics.pdf)
2. [A Predictive Neural Network for Learning Higher-Order Non-Stationarity from Spatiotemporal Dynamics](https://arxiv.org/pdf/1811.07490.pdf)
3. [Deep Learning for Precipitation Nowcasting: A benchmark and A new model](https://arxiv.org/pdf/1706.03458.pdf)

### ML/DL for rainfall estimation<a name='mlrain'></a> ([notes](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/RainRemoval/rain_removal_notes.pdf))
1. Video-based rainfall removal  
    
    1.1 [Video Rain Streak Removal By Multiscale ConvolutionalSparse Coding](https://github.com/MinghanLi/MS-CSC-Rain-Streak-Removal)

2. Image-based rainfall removal  

    2.1 [JORDEN: Deep Joint Rain Detection from a Single Image](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/RainRemoval/Deep_Joint_Rain_Detection_and_Removal_from_a_Single_Image.pdf.pdf)  

    2.2 [Rain Streaks Detection and Removal in Image based on
Entropy Maximization and Background Estimation](https://pdfs.semanticscholar.org/2975/6fb5238c69cea5d544df6227fa79ef6aa2cb.pdf)

    2.3 [Spatial Attentive Single-Image Deraining with a High Quality Real Rain dataset](https://github.com/stevewongv/SPANet)

    2.4 [Dynamic Routing Residue Recurrent Network for Video Removal](http://www.icst.pku.edu.cn/struct/Pub%20Files/2019/ywh_tip19.pdf)

    2.5 [Progressive Image Deraining Networks: A Better and Simpler Baseline](https://github.com/csdwren/PReNet)


### Generative Adversaril Network(GAN)<a name='gan'></a> ([notes](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/MachineLearning/texnote/GAN.pdf))
1. [Pytorch-GAN-zoo](https://github.com/facebookresearch/pytorch_GAN_zoo)
2. [InfoGAN](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/InfoGAN.pdf)
3. [tempoGAN](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/tempoGAN.pdf)
4. [WGAN](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/WGAN.pdf)
5. [WGAN-improved](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/ComputerVision/WGAN-improved.pdf) [github](https://github.com/jalola/improved-wgan-pytorch)
6. [DehazeGAN](https://arxiv.org/abs/1810.09479) [code](https://github.com/thatbrguy/Dehaze-GAN)

### Numerical Methods<a name='numeric'></a>
#### Optical Flow<a name='opticalflow'></a>
Methods:

>Lucas-Kanade method:  it tracks the corner with Shi-Tomasi algorithm and calculate (u,v) by solving 9 equations and then estimate the 3x3 patch movement;

~~~~
cv2.calcOpticalFlowPyrLK
~~~~

>Gunner Farneback's algorithm (Dense): It computes the optical flow for all the points in the frame;

~~~~
cv2.calcOpticalFlowFarneback
~~~~

1. [Optical flow models as an open benchmark for radar-based precipitation nowcasting](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/NumericalMethods/OpticalFlow/Optical_flow_mdoels_as_an_open_benchmark_for_radar-based_precipitation_nowcasting.pdf)
    >Codes available on github: [optical flow](https://github.com/hydrogo/rainymotion)
2. [Novel Video Prediction for Large-scale Scene using
Optical Flow](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/NumericalMethods/OpticalFlow/new_video_predction_for_large_scale_scene_using_optical_flow.pdf)
3. [Two Frame Motion Estimation Based on Polynomial Expansion](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/NumericalMethods/OpticalFlow/Two_Frame_Motion_Estimation_Based_on_Polynomial_Expansion.pdf)
4. [my radar project demo](https://github.com/chrimerss/RadarEnhancement)
5. [FlowNet: Learning Optical Flow with Convolutional Networks](https://github.com/chrimerss/RemoteSensingandComputerVision/blob/master/NumericalMethods/OpticalFlow/Learning_Optical_Flow_with_DL(FlowNet).pdf)

#### Semi-Lagrangian Scheme<a name='semilag'></a>

1. [My radar project demo](https://github.com/chrimerss/RadarEnhancement)

## Updates<a name='updates'></a>
- [x] Update GAN collections and rainfall removal category(2019.6.2)
- [x] FlowNet: Learning Optical Flow with Convolutional Networks(2019.5.23)
- [x] 神经网络与深度学习 (2019.5.22)
- [x] optical flow models as an open benchmark for radar-based precipitation nowcasting (2019.5.16)
- [x] Novel Video Prediction for Large-scale Scene using Optical Flow (2019.5.16)
- [x] Generating Videos with Scene Dynamics/GAN (2019.5.16)
- [ ] Two Frame Motion Estimation Based on Polynomial Expansion
