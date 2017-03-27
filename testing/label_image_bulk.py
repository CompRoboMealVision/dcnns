# Inspired by https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#4

import argparse
import glob
import os
import sys

import numpy as np
import tensorflow as tf

FLAGS = None

# # Read in the image_data
# # TODO: Update.
# image_data = tf.gfile.FastGFile(image_path, 'rb').read()
#
# # Loads label file, strips off carriage return
# label_lines = [line.rstrip() for line in tf.gfile.GFile("/data2/user_data/meal/models/food_101/retrained_labels.txt")]
#
# # Unpersists graph from file
# with tf.gfile.FastGFile("/data2/user_data/meal/models/food_101/retrained_graph.pb", 'rb') as f:
#     graph_def = tf.GraphDef()
#     graph_def.ParseFromString(f.read())
#     _ = tf.import_graph_def(graph_def, name='')
#
# with tf.Session() as sess:
#     # Feed the image_data as input to the graph and get first prediction
#     softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
#
#     predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

    # TODO: Save to file.

    # Sort to show labels of first prediction in order of confidence
    # top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    # for node_id in top_k:
    #     human_string = label_lines[node_id]
    #     score = predictions[0][node_id]
    #     print('%s (score = %.5f)' % (human_string, score))

def main():
    image_paths = np.array([], dtype = np.str);
    image_labels = np.array([], dtype = np.str);
    directories = [directory for directory in os.listdir(FLAGS.image_dir) if os.path.isdir(os.path.join(FLAGS.image_dir, directory))]

    for directory in directories:
        directory_path = os.path.join(FLAGS.image_dir, directory)
        for _, image_name in zip(range(FLAGS.limit), os.listdir(directory_path)):
            image_labels = np.append(image_labels, directory)
            image_paths = np.append(image_paths, os.path.join(directory_path, image_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image_dir',
        type=str,
        default=''
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=50
    )
    FLAGS, unparsed = parser.parse_known_args()
    main()
