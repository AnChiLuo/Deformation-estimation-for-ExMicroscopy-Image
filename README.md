# Deformation-estimation-for-ExMicroscopy-Image
Following Abbe's diffraction limit, the resolution of optical microscopy is limited and insufficient for modern biologists to observe the intracellular phenomenon or subcellular structure. Expansion microscopy(ExM) solves this problem by expanding biological samples, which provides investigators with higher resolution without using specialized equipment. Its expansion procedure should be isotropic to avoid structure deformation. Therefore the extent of structure deformation represents the quality of ExM.To calculate it, a deformation vector field between two images(Pre and Post-ExM) is generated via a nonrigid registration process. Then, the root-mean-square (RMS) error of feature on Post_ExM images is computed to quantity the consistency in length change of specific structures before and after ExM. Here, we build a GUI tool based on Chozinski et al.'s method to run the above quantification. Our tool warps a Python module-PyElastix and the Elastix registration toolkit to register images, and the RMS calculation can also be done on our tool without changing tools.

# Installation
* For our tool:     
    Download "ExM deformation analysis.py" to your computer and put it in the Folder containing Elaxtix.    
* For the PyElastix:  
We modified PyElastix to fetch registration data and call the similarity registration function of Elastix. So, please update your installed PyElastix to our version.  
	1. Use the "pip install pyelastix" or "conda install pyelastix -c conda-forge" to install the library.          
	2. Replace the "pyelastix.py" in your Python "site-package" file with the new "pyelastix.py" provided in this repository.  
* For the Elastix:       
	1. Elastix needs to be installed on your device, which can be downloaded here https://elastix.dev/download.php        
	2. Add the ELASTIX_PATH to the environment variable helping PyElatix to detect the executable Elastix.      
* Module Dependencies:  
This tool also relies on the packages: 1.Scikit-image 0.19.2&nbsp;&nbsp;&nbsp;&nbsp;2.matplotlib 3.8.0&nbsp;&nbsp;&nbsp;&nbsp;3.OpenCV 4.8.1.78&nbsp;&nbsp;&nbsp;&nbsp;4.Pandas 2.0.3	
# Run ExM deformation analysis
### Start the GUI ###
1.  Open the anaconda prompt and change the working directory to the folder that includes ExM deformation analysis.py
2.  Start running GUI with:  

    	python ExM deformation analysis.py 

3.  Two separate windows, "Show Image"(for displaying results) and "RMS analysis"(for controlling our program), will pop up, chose the analysis model from "RMS analysis" window. 
### Step-by-step demo ###
* Start with Image model  
  This model requires images as input to run the quantification. If you are unfamiliar with Elastix or ImageJ, we highly recommend you choose this model.
1. Click the `Browse` button on the "Import Data region" to load images. Images must have the same size. Optionally check images on the "Show Image" window by clicking the `Preview` button.
2. Click the `GoNext` button. If two images are of different sizes, you will see the warning on the "Show Image" window.
3. Set the parameters on the "Similarity Registration region" of the "RMS analysis" window. Select $${\color{lightblue}Smooth\space checkbox}$$ to blur the images with the Gaussian filter when their resolutions are too different.  
   *Three parameters for registrater can be adjusted:
   	1.  Number Of Resolutions (int): Elastix adopts a multiresolution strategy to speed up the process. The higher value, the more smoothing and downsampling are imepled on images. (default 4)
   	2.  MaximumNumber Of Iterations (int): This value limits the iterations times in each resolution level. Increasing it can get a more robust registration, but the computation time will be longer. 200-2000 works usually fine for nonrigid registration. (default 800).
   	3.  Maximum Step Length (int):  This parameter refers to how many voxel/pixel displacements can be applied between two iterations. Increasing this parameter makes your program faster, but may cause Elastix crushing when it's too big. (default 5).
4.  Click the `GoNext` button and await the registration result. If it's not good enough, click `Go Back` button on the "beta-spline Registration region to reset the parameters and rerun the similarity registration.
5.  Set the parameters on the "beta-spline Registration region" and click the 'GoNext' button to run the nonrigid registration.
6.  Check the $${\color{lightblue}Reference\space checkbox}$$ and click the `Browse` button to import your skeleton image. Otherwise, this program will automatically extract features by skeletonizing your image. Optionally change the unit of the result by selecting the `Set scaling checkbox`.
7.  Click the `GoNext` button on the "Calculate Structure Deflection region" to calculate the length change of features. To speed up this process, you can down-sampling the feature size by increasing the "Sampling size of Skeleton" value.
8. Set the parameters and click the `GoNext` button on the "Calculate Root mean square(RMS) and plot region" to calculate the RMS values. You can adjust the resolution for RMS calculation using the "Length interval" parameter, which is inversely proportional to the resolution.
9.  Click the `GoNext` button on the "Plot the Deformation map region" to draw the deformation vector field on the image. The raw image is the default setting, even if you have applied the Gaussian filter in previous steps.
* Start with Transformix output model
  This model allows you to calculate the RMS values from the data obtained by using Chozinski's method.
1. Import the Transformix output data-"outputpoints.txt" by clicking the `Browse` button on the "Import the data of skeleton region".
2. Optionally check the $${\color{lightblue}Set\space scaling\space checkbox}$$ and set the scaling factors to change the unit of the RMS values.
3. Click the `GoNext` button on the "Import the data of skeleton region" to calculate the length change of features. You can also increase the "Sampling size of Skeleton" value to speed up the calculation.
4. Set the parameters and click the `GoNext` button on the "Calculate Root mean square(RMS) and plot region" to calculate the RMS values. Set the "Length interval" parameter to adjust the resolution for RMS calculation.The higher value, the lower resolution.
5. To draw the Deformation map, use the `Browse` buttons to import image and the outputpoints.txt file generated by deforming array of points with Transformix.
  
 <mark>螢光標記</mark>


    






