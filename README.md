# Deformation-estimation-for-ExMicroscopy-Image
Following Abbe's diffraction limit, the resolution of optical microscopy is limited and insufficient for modern biologists to observe the intracellular phenomenon or subcellular structure. Expansion microscopy(ExM) solves this problem by expanding biological samples, which provides investigators with higher resolution without using specialized equipment. Its expansion procedure should be isotropic to avoid structure deformation. Therefore the extent of structure deformation represents the quality of ExM.To calculate it, a deformation vector field between two images(Pre and Post-ExM) is generated via a nonrigid registration process. Then, the root-mean-square (RMS) error of feature on Post_ExM images is computed to quantity the consistency in length varying of specific structures before and after ExM. Here, we build a GUI tool based on Chozinski et al.'s method to run the above quantification. Our tool warps a Python module-PyElastix and the Elastix registration toolkit to register images, and the RMS calculation can also be done on our tool without changing tools.

# Installation
For the PyElastix:   
>1.Use the "pip install pyelastix" or "conda install pyelastix -c conda-forge" to install the library.  
>2.Replace the "pyelastix.py" in your Python "site-package" file with the new "pyelastix.py" provided in this repository.  
For the Elastix:  
>1.Elastix needs to be installed on your device,which can be downloaded here https://elastix.dev/download.php  
>2.Add the ELASTIX_PATH to the environment variable helping PyElatix to detect the executable Elastix.  
Module Dependencies:  
>1.Scikit-image 0.19.2 
   2.matplotlib 3.8.0 
   3.OpenCV 4.8.1.78
   4.Pandas 2.0.3


