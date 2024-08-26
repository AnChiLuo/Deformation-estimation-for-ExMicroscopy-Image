# Deformation-estimation-for-ExMicroscopy-Image ![image](https://github.com/user-attachments/assets/daad6715-f503-4361-b5fc-0cb44ad5e96f)
Following Abbe's diffraction limit, the resolution of optical microscopy is limited and insufficient for modern biologists to observe small structures. Expansion microscopy(ExM) solves this problem by expanding biological samples. The quality of ExM can be evaluated with the extent of structure deformation because the expansion should be isotropic to keep the information. To quantify deformations, a deformation vector field between two images(Pre and Post-ExM) is generated via a nonrigid registration process. Subsequently, the length change of structures on images was obtained from the vector field, and then the root-mean-square (RMS) error was calculated to quantify the consistency in length change,i.e. the isotropy of ExM. Here, we build a GUI tool based on Chozinski et al.'s method to run the above procedure. Unlike their method, our tool executes all procedures with Python by warping a Python module-PyElastix and the Elastix registration toolkit. You can register images and perform calculations without changing tools.  



# Installation
* Module Dependencies:  
This tool also relies on the other packages: 1.Scikit-image 0.19.2&nbsp;&nbsp;&nbsp;&nbsp;2.matplotlib 3.8.0&nbsp;&nbsp;&nbsp;&nbsp;3.OpenCV 4.8.1.78&nbsp;&nbsp;&nbsp;&nbsp;4.Pandas 2.0.3&nbsp;&nbsp;&nbsp;&nbsp;5.PyElastix 1.2	  
* For the PyElastix:  
We modified PyElastix to fetch registration data and call the similarity registration function of Elastix. So, please update your installed PyElastix to our version.  
	1. Use the "pip install pyelastix" or "conda install pyelastix -c conda-forge" to install the library.          
	2. Replace the "pyelastix.py" in your Python "site-package" file with the new "pyelastix.py" provided in this repository.  
* For the Elastix:       
	1. Elastix needs to be installed on your device, which can be downloaded here https://elastix.dev/download.php        
	2. Add the ELASTIX_PATH to the environment variable helping PyElatix to detect the executable Elastix.
* For our tool:     
    Download "ExM deformation analysis.py" to your computer and place it together with Elaxtix.       

# Run ExM deformation analysis
### Start the GUI ###
1.  Open the anaconda prompt and change the working directory to the folder that includes ExM deformation analysis.py
2.  Start running GUI with:  

    	python ExM deformation analysis.py 

3.  Two separate windows, "Show Image"(for displaying results) and "RMS analysis"(the control panel), will pop up.Then chose the entrance from the "RMS analysis" window. 
### Step-by-step demo ###
The image deformation can be stepwisely quantified within the same platform with our tool. You can use `GoBack` to redo the previous step if you are not satisfied with the current result and a `Save result`  button is available to save the confirmed results.

* **Start with Image model**    
  This entrance requires images as input to run the quantification. If you are unfamiliar with Elastix or ImageJ, we highly recommend you to choose it.
1. Click the `Browse` button on the "Import Data region" to load images. Images must have the same size. Optionally check images on the "Show Image" window by clicking the `Preview` button.
2. Click the `GoNext` button. If the images are in different size, you will see a warning.
3. Set the parameters on the "Similarity Registration region" of the "RMS analysis" window. Select $${\color{blue}Smooth\space checkbox}$$ to blur the PostExM images with the Gaussian filter when the pre-ExM image is too vague comparing to the post-ExM image..  
   *Three parameters for registration can be adjusted:
   	1.  Number Of Resolutions (int): Elastix adopts a multiresolution strategy to speed up the process. The higher the value you set, the smoother and downsampler tools are applied. (default 4). 
   	2.  MaximumNumber Of Iterations (int): This value limits the iterations in each resolution level.  You will get a robust registration, but longer computation time will be the trade-off. The value 200-2000 works usually fine for nonrigid registration. (default 800).
   	3.  Maximum Step Length (int):  This parameter refers to the freedom of deforming the Post-expansion image to fit the Pre-expansion image between iterations. Increasing this parameter makes it faster, but may cause Elastix to crush. (default 5).
4.  Click the `GoNext` button and await the registration result. If your result is not good enough, click `Go Back` button on the "beta-spline Registration region to run the similarity registration again with newly refined parameters.
5.  Set the parameters on the "beta-spline Registration region" and click the 'GoNext' button to run the nonrigid registration.
6.  Check the $${\color{blue}Reference\space checkbox}$$ and click the `Browse` button to import your skeleton image. If you don't have your own skeleton image, this program will automatically extract features to generate one for you skeletonizing your image. Optionally change the unit of the result by selecting the $${\color{blue}Set\space scaling\space checkbox}$$.
7.  Click the `GoNext` button on the "Calculate Structure Deflection region" to calculate the length change of features. To speed up this process, you can down-sampling the feature size by increasing the "Sampling size of Skeleton" value.
8. Set the parameters and click the `GoNext` button on the "Calculate Root mean square(RMS) and plot region" to calculate the RMS values. You can adjust the resolution for RMS calculation using the "Length interval" parameter, which is inversely proportional to the resolution.
9.  Click the `GoNext` button on the "Plot the Deformation map region" to draw the deformation vector field on the image. The raw image will be adopted here, even if you have applied the Gaussian filter in previous steps.
* **Start with Transformix output model**  
  This entrance allows you to calculate the RMS values using the data obtained by Chozinski's method without installing the commercial software.  
1. Import the Transformix output data-"outputpoints.txt" by clicking the `Browse` button on the "Import the data of skeleton region".
2. Optionally check the $${\color{blue}Set\space scaling\space checkbox}$$ and set the scaling factors to change the unit of the RMS values.
3. Click the `GoNext` button on the "Import the data of skeleton region" to calculate the length change of features. You can also increase the "Sampling size of Skeleton" value to speed up the calculation.
4. Set the parameters and click the `GoNext` button on the "Calculate Root mean square(RMS) and plot region" to calculate the RMS values. Set the "Length interval" parameter to adjust the resolution for RMS calculation. The higher the value you choose, the lower the resolution you get.
5. To draw the Deformation map, use the `Browse` buttons to import images and the outputpoints.txt file generated by deforming an array of points with Transformix.
# Figures
<img src="https://github.com/user-attachments/assets/b1ec0e62-46df-440b-a90a-e7f375cd1778" width="600" />


# Reference   
1. S. Klein, M. Staring, K. Murphy, M.A. Viergever, J.P.W. Pluim, "elastix: a toolbox for intensity based medical image registration," IEEE Transactions on Medical Imaging, vol. 29, no. 1, pp. 196 - 205, January 2010.
2. D.P. Shamonin, E.E. Bron, B.P.F. Lelieveldt, M. Smits, S. Klein and M. Staring, "Fast Parallel Image Registration on CPU and GPU for Diagnostic Classification of Alzheimer’s Disease", Frontiers in Neuroinformatics, vol. 7, no. 50, pp. 1-15, January 2014.
3. Chozinski TJ, Halpern AR, Okawa H, et al. Expansion microscopy with conventional antibodies and fluorescent proteins. Nat Methods. 2016;13(6):485-488. doi:10.1038/nmeth.3833
4. Klein, A. (2019). PyElastix – Python wrapper for the Elastix nonrigid registration toolkit, https://github.com/almarklein/pyelastix.
  


    






