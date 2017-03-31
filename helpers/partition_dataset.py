import argparse
import random
import os
import shutil

# Input arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '--data_dir',
    type=str
)
parser.add_argument(
    '--location_after',
    type=str
)
FLAGS, unparsed = parser.parse_known_args()

training_location = os.path.join(FLAGS.location_after, 'training')
validation_location = os.path.join(FLAGS.location_after, 'validation')

# Reset the validation file location.
if os.path.exists(FLAGS.location_after):
    shutil.rmtree(FLAGS.location_after)
    # os.makedirs(training_location)
    os.makedirs(validation_location)
    shutil.copytree(FLAGS.data_dir, training_location)

for label_name in os.listdir(training_location):
    training_label_path = os.path.join(training_location, label_name)
    validation_label_path = os.path.join(validation_location, label_name)
    os.makedirs(validation_label_path)

    if (os.path.isdir(training_label_path) == False):
        continue

    image_names_in_label = os.listdir(os.path.join(training_label_path))
    count = len(image_names_in_label)
    validation_image_names = random.sample(image_names_in_label, (int) (.2 * count))

    for image_name in validation_image_names:
        shutil.move(os.path.join(training_label_path, image_name), os.path.join(validation_label_path, image_name))

    print label_name
