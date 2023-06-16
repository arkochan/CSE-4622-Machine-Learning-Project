import os
import imageio
import numpy as np
import tensorflow as tf

from DR_GAN_model import DR_GAN

flags = tf.compat.v1.app.flags
flags.DEFINE_boolean("return_img", True, "True for return img, False for feature and coefficient only, img is set to 0")
flags.DEFINE_string("gpu", "0", "GPU to use [0]")
flags.DEFINE_string("input", "./img_in.png", "Path to input")
flags.DEFINE_string("output_prefix", "./out_", "Path to output")
FLAGS = flags.FLAGS


def main(_):
    os.environ["CUDA_VISIBLE_DEVICES"] = FLAGS.gpu
    gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.5)
    dr_gan = DR_GAN(gpu_options=gpu_options)

    path = FLAGS.input
    if os.path.isfile(path):
        # Read image
        img = imageio.imread(path).astype(np.float32)

        # Feed to DR-GAN
        rotated_image, feature, coefficient = dr_gan.test(img, return_img=FLAGS.return_img)

        # Save output
        imageio.imwrite(FLAGS.output_prefix + 'img.png', rotated_image)
        print('Frontalized image:', FLAGS.output_prefix + 'img.png')
        np.savetxt(FLAGS.output_prefix + 'feature.txt', feature)
        print('Feature:', FLAGS.output_prefix + 'feature.txt')
        np.savetxt(FLAGS.output_prefix + 'coefficient.txt', coefficient)
        print('Coefficient:', FLAGS.output_prefix + 'coefficient.txt')
    elif os.path.isdir(path):
        # TO DO: remove pass
        pass
        # Read all images in the folder

        # Feed each image to the network

        # Save output as you need


if __name__ == '__main__':
    tf.compat.v1.app.run()
