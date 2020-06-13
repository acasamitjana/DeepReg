# CT Lung Registration
Lungs experince motion due to breathing and the motion can be a problem when registering two images of the lung taken at different times in teh breathing cycle. This demo uses the DeepReg toolbox to create a deep learning based image registration pipeline where the training data comes from an open source dataset.

# The Dataset
The dataset for this demo comes from [1] and can be downloaded from:
https://zenodo.org/record/3835682#.XsUWXsBpFhE

# Usage of the Python Scripts and Config File
The python scripts used along with their brief descriptions are as follows:
- data.py: used to download, unzip and restructure the dataset to suit the needs of the DeepReg toolbox (only the 'project_dir' variable needs to be changed)
- insp_to_exp_config.yaml: config file used to specify training options (only 'tfrecord_dir' and 'dir' need to be changed to indicate the locations tfrecord files and dataset respectively)
- train.py: used to generate tfrecord files and train the network using the DeepReg toolbox (the 'path_to_config_file' variable needs to be changed)
- predict.py: used to predict and visualise predictions from the trained network ('path_to_ckpt_file', 'path_to_image0_label0' and 'path_to_save_fig' need to be changed)

# References 
[1] Hering, Alessa, Murphy,Keelin, and van Ginneken, Bram. (2020). Lean2Reg Challenge: CT Lung Registration - Training Data [Data set]. Zenodo. http://doi.org/10.5281/zenodo.3835682

