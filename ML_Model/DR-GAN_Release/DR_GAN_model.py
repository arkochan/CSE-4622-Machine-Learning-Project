from __future__ import division
import os
import tensorflow as tf
import numpy as np
from tensorflow.compat.v1 import gfile

SUBJECT_NUM_CASIA = 10575


class DR_GAN(object):
    def __init__(self, gpu_options):
        self.gpu_options = gpu_options

        self.output_size = 96
        self.z_dim = 100
        self.c_dim = 3
        self.pose_dim = 1

        self.build_model()

    def build_model(self):
        self.graph = self.load_graph()
        self.sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(allow_soft_placement=True, log_device_placement=False, gpu_options=self.gpu_options), graph=self.graph)

        self.z = self.graph.get_tensor_by_name('dr_gan/z:0')
        self.pose = self.graph.get_tensor_by_name('dr_gan/pose:0')
        self.feature_in = self.graph.get_tensor_by_name('dr_gan/feature_in:0')

        self.input_image = self.graph.get_tensor_by_name('dr_gan/input_image:0')
        self.s_feature = self.graph.get_tensor_by_name('dr_gan/feature:0')
        self.s_coefficient = self.graph.get_tensor_by_name('dr_gan/coefficient:0')
        self.rotated_img = self.graph.get_tensor_by_name('dr_gan/rotated_image:0')

    def test(self, img, return_img=True):
        # img: RBG image in range [0, 255] with shape 96*96*3
        feature, coefficient = self.test_encoder(img)
        if return_img:
            rotated_image = self.test_decoder(feature)
        else:
            rotated_image = 0

        return rotated_image, feature, coefficient

    def test_encoder(self, img):
        # img: RBG image in range [0, 255] with shape 96*96*3
        batch_img = np.array(img / 127.5 - 1.).astype(np.float32).reshape((1, self.output_size, self.output_size, self.c_dim))
        feature, coefficient = self.sess.run([self.s_feature, self.s_coefficient], feed_dict={self.input_image: batch_img})

        return feature, coefficient

    def test_decoder(self, feature):
        target_pose = np.zeros([1, self.pose_dim], dtype=np.float32)
        sample_z = np.zeros(shape=(1, self.z_dim), dtype=np.float32)

        rotated_image = self.sess.run(self.rotated_img, feed_dict={self.z: sample_z, self.feature_in: feature, self.pose: target_pose})
        rotated_image = np.array((rotated_image + 1.0) / 2.0, dtype=np.float32).reshape(self.output_size, self.output_size, self.c_dim)

        return rotated_image

    def load_graph(self):
        # We load the protobuf file from the disk and parse it to retrieve the unserialized graph_def
        frozen_graph_filename = 'DR_GAN_model.pb'
        with gfile.FastGFile(frozen_graph_filename, "rb") as f:
            graph_def = tf.compat.v1.GraphDef()
            graph_def.ParseFromString(f.read())

        # Then, we can use again a convenient built-in function to import a graph_def into the current default Graph
        with tf.Graph().as_default() as graph:
            tf.compat.v1.import_graph_def(
                graph_def,
                input_map=None,
                return_elements=None,
                name="dr_gan",
                op_dict=None,
                producer_op_list=None
            )
        return graph
