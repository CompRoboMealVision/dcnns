python $HOME/tensorflow/tensorflow/examples/image_retraining/retrain.py \
--image_dir=$HOME/data/uec \
--output_graph=$HOME/data/models/uec_v02/retrained_graph.pb \
--output_labels=$HOME/data/models/uec_v02/retrained_labels.txt \
--summaries_dir=$HOME/data/models/uec_v02/retrain_logs \
--how_many_training_steps=7000 \
--model_dir=$HOME/data/models/uec_v02/inception \
--bottleneck_dir=$HOME/data/models/uec/bottlenecks \
