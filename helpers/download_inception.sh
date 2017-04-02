# location of where to place the Inception v3 model
DATA_DIR=/data2/user_data/meal/inception-v3-model
mkdir -p ${DATA_DIR}
cd ${DATA_DIR}

# download the Inception v3 model
curl -O http://download.tensorflow.org/models/image/imagenet/inception-v3-2016-03-01.tar.gz
tar xzf inception-v3-2016-03-01.tar.gz
