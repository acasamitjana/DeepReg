import numpy as np
import wget
import zipfile
import os
import shutil
import random


################# DOWNLOADING AND UNZIPPING ALL FILES INTO CORRECT PATH ########################

project_dir = r'/home/ssd/Desktop/DeepReg_Project'
os.chdir(project_dir)

url = 'https://zenodo.org/record/3835682/files/training.zip'
fname = wget.download(url)
print('The file ', fname,' has successfully been downloaded!')

#fname = 'training.zip'

data_folder_name = 'insp_to_exp'

if os.path.exists(os.path.join(project_dir, data_folder_name))!=True:
    os.mkdir(data_folder_name)

with zipfile.ZipFile(fname, 'r') as zip_ref:
    zip_ref.extractall(data_folder_name)
    

print('Files unzipped!')

################# MOVING ALL FILES INTO CORRECT PATH ########################

path_to_data_folder = os.path.join(project_dir,data_folder_name)
path_to_images_and_labels = os.path.join(os.path.join(project_dir,data_folder_name), 'training')
path_to_train = os.path.join(path_to_data_folder, 'train')

labels_fnames = os.listdir(os.path.join(path_to_images_and_labels,'lungMasks'))
images_fnames = os.listdir(os.path.join(path_to_images_and_labels,'scans'))


if os.path.exists(path_to_train)!=True:
    os.mkdir(path_to_train)
    os.mkdir(os.path.join(path_to_train, 'fixed_images'))
    os.mkdir(os.path.join(path_to_train, 'fixed_labels'))
    os.mkdir(os.path.join(path_to_train, 'moving_images'))
    os.mkdir(os.path.join(path_to_train, 'moving_labels'))

def moveFilesIntoCorrectPath(fnames, path_to_images_and_labels, new_path, suffix, sub_folder_name):
        
    os.chdir(os.path.join(path_to_images_and_labels, sub_folder_name))

    for file in fnames:
        if 'insp' in file:
            source = file
            destination = os.path.join(path_to_train, 'fixed_'+suffix)
            shutil.move(source, destination)
        if 'exp' in file:
            source = file
            destination = os.path.join(path_to_train, 'moving_'+suffix)
            shutil.move(source, destination)
    
if os.path.exists(path_to_images_and_labels):
    
    moveFilesIntoCorrectPath(images_fnames, path_to_images_and_labels, path_to_train, 'images', 'scans')
    moveFilesIntoCorrectPath(labels_fnames, path_to_images_and_labels, path_to_train, 'labels', 'lungMasks')
    
os.chdir(project_dir)    
    
if os.path.exists(path_to_images_and_labels)==True:
    os.rmdir(os.path.join(path_to_images_and_labels, 'scans'))
    os.rmdir(os.path.join(path_to_images_and_labels, 'lungMasks'))
    os.rmdir(path_to_images_and_labels)

################# MOVING TEST AND VALID FILES INTO CORRECT PATH ########################

path_to_test = os.path.join(path_to_data_folder, 'test')
path_to_valid = os.path.join(path_to_data_folder, 'valid')

if os.path.exists(path_to_test)!=True:
    
    os.mkdir(path_to_test)
    os.mkdir(os.path.join(path_to_test, 'fixed_images'))
    os.mkdir(os.path.join(path_to_test, 'fixed_labels'))
    os.mkdir(os.path.join(path_to_test, 'moving_images'))
    os.mkdir(os.path.join(path_to_test, 'moving_labels'))
    
    ratio_of_test_and_valid_samples = 0.2
    
    unique_case_names = []
    for file in images_fnames:
        case_name_as_list = file.split('_')[0:2]
        case_name = case_name_as_list[0]+'_'+case_name_as_list[1]
        unique_case_names.append(case_name)
    unique_case_names = np.unique(unique_case_names)
    
    test_and_valid_cases = random.sample(list(unique_case_names), int(ratio_of_test_and_valid_samples*len(unique_case_names)))
    test_cases = test_and_valid_cases[0:int(int(ratio_of_test_and_valid_samples*len(unique_case_names)/2))]
    valid_cases = test_and_valid_cases[int(int(ratio_of_test_and_valid_samples*len(unique_case_names)/2))+1:]
    
    
    def moveTestCasesIntoCorrectPath(test_cases, path_to_train, path_to_test):
        
        folder_names = os.listdir(path_to_train)
        os.chdir(path_to_train)
        for case in test_cases:
            for folder in folder_names:
                file_names = os.listdir(os.path.join(path_to_train, folder))
                for file in file_names:    
                    if case in file:
                        os.chdir(os.path.join(path_to_train, folder))
                        source = file
                        destination = os.path.join(path_to_test, folder)
                        shutil.move(source, destination)


    
    moveTestCasesIntoCorrectPath(test_cases, path_to_train, path_to_test)

    os.mkdir(path_to_valid)
    os.mkdir(os.path.join(path_to_valid, 'fixed_images'))
    os.mkdir(os.path.join(path_to_valid, 'fixed_labels'))
    os.mkdir(os.path.join(path_to_valid, 'moving_images'))
    os.mkdir(os.path.join(path_to_valid, 'moving_labels'))
    
    moveTestCasesIntoCorrectPath(valid_cases, path_to_train, path_to_valid)



################# NAMING FILES CORRECTLY ########################

# name all files such that names match exactly for training

for folder in os.listdir(path_to_train):
    path_to_folder = os.path.join(path_to_train, folder)
    os.chdir(path_to_folder)
    
    for file in os.listdir(path_to_folder):
        if '_insp' in file:
            new_name = file.replace('_insp', '')
        elif '_exp' in file:
            new_name = file.replace('_exp', '')
        
        source = file
        destination = new_name
        os.rename(source, destination)

# name all files such that names match exactly for testing

for folder in os.listdir(path_to_test):
    path_to_folder = os.path.join(path_to_test, folder)
    os.chdir(path_to_folder)
    
    for file in os.listdir(path_to_folder):
        if '_insp' in file:
            new_name = file.replace('_insp', '')
        elif '_exp' in file:
            new_name = file.replace('_exp', '')
        
        source = file
        destination = new_name
        os.rename(source, destination)


for folder in os.listdir(path_to_valid):
    path_to_folder = os.path.join(path_to_valid, folder)
    os.chdir(path_to_folder)
    
    for file in os.listdir(path_to_folder):
        if '_insp' in file:
            new_name = file.replace('_insp', '')
        elif '_exp' in file:
            new_name = file.replace('_exp', '')
        
        source = file
        destination = new_name
        os.rename(source, destination)

print('All files moved and restructured')