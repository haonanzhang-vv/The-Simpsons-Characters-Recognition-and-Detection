from keras import backend as K


class Config:

	def __init__(self):

		self.verbose = True

		# setting for data augmentation
		self.use_horizontal_flips = True
		self.use_vertical_flips = True
		self.rot_90 = True

		# Number of ROIs per iteration. Higher means more memory use.
		self.num_rois = 32

		# Output path for weights.
		self.model_path = './model_frcnn.hdf5'

		# Location to store all the metadata related to the training (to be used when testing).
		self.config_filename = "config.pickle"

		# anchor box scales
		self.anchor_box_scales = [64, 128, 256, 512]

		# anchor box ratios
		self.anchor_box_ratios = [[1, 1], [1, 2], [2, 1]]

		# size to resize the smallest side of the image
		self.im_size = 300

		# image channel-wise mean to subtract
		self.img_channel_mean = [103.939, 116.779, 123.68]
		self.img_scaling_factor = 1.0

		# number of ROIs at once
		self.num_rois = 4

		# stride at the RPN (this depends on the network configuration)
		self.rpn_stride = 16

		self.balanced_classes = False

		# scaling the stdev
		self.std_scaling = 4.0
		self.classifier_regr_std = [8.0, 8.0, 4.0, 4.0]

		# overlaps for RPN
		self.rpn_min_overlap = 0.3
		self.rpn_max_overlap = 0.7

		# overlaps for classifier ROIs
		self.classifier_min_overlap = 0.1
		self.classifier_max_overlap = 0.5

		# placeholder for the class mapping, automatically generated by the parser
		self.class_mapping = None

		#location of pretrained weights for the base network 
		# weight files can be found at:
		# https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_th_dim_ordering_th_kernels_notop.h5
		# https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
		#if K.image_dim_ordering() == 'th':
		if K.common.image_dim_ordering() == 'th':
			self.base_net_weights = 'resnet50_weights_th_dim_ordering_th_kernels_notop.h5'
		else:
			self.base_net_weights = 'resnet50_weights_tf_dim_ordering_tf_kernels.h5'
