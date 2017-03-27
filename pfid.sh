python $HOME/tensorflow/tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=$HOME/data/models/pfid/bottlenecks \
--how_many_training_steps 500 \
--model_dir=$HOME/data/models/pfid/inception \
--output_graph=$HOME/data/models/pfid/retrained_graph.pb \
--output_labels=$HOME/data/models/pfid/retrained_labels.txt \
--image_dir $HOME/data/pfid_correct_format
