import os
import matplotlib.pyplot as plt

# this is the path to the checkpoint you want to use for prediciton
path_to_ckpt_file = r'/home/ssd/Desktop/DeepReg_Project/insp_to_exp_train_logs/logs/insp_to_exp_log_train/save/weights-epoch2.ckpt'

# refer to the DeepReg github page to see when to use which options to use
os.system('deepreg_predict' + ' -g \"\" ' + '--ckpt_path '  + path_to_ckpt_file + ' --mode test' + ' --log insp_to_exp_test_pred')

print('Predictions generated!')

# Now lets load in a few samples from the predicitons and plot them
path_to_image0_label0 = r'/home/ssd/Desktop/DeepReg_Project/predictions_and_labels'

os.chdir(path_to_image0_label0)

plt.subplot(3,2,1)
label144 = plt.imread('depth144_fixed_label.png')
plt.imshow(label144)
plt.title('Label')
plt.axis('off')

plt.subplot(3,2,2)
pred144 = plt.imread('depth144_fixed_pred.png')
plt.imshow(pred144)
plt.title('Prediction')
plt.axis('off')



plt.subplot(3,2,3)
label145 = plt.imread('depth145_fixed_label.png')
plt.imshow(label145)
plt.axis('off')

plt.subplot(3,2,4)
pred145 = plt.imread('depth145_fixed_pred.png')
plt.imshow(pred145)
plt.axis('off')



plt.subplot(3,2,5)
label184 = plt.imread('depth184_fixed_label.png')
plt.imshow(label184)
plt.axis('off')

plt.subplot(3,2,6)
pred184 = plt.imread('depth184_fixed_pred.png')
plt.imshow(pred184)
plt.axis('off')

# this is the path where you want to save the visualisation as a png
path_to_save_fig = r'/home/ssd/Desktop'
plt.savefig(os.path.join(path_to_save_fig, 'labels_and_preds.png'))

print('Visual representation of predictions saved to path specified')