python $HOME/tensorflow/tensorflow/examples/image_retraining/retrain.py \
--image_dir=$HOME/data/food_101/images \
--output_graph=$HOME/dcnns/models/food_101_v3/retrained_graph.pb \
--output_labels=$HOME/dcnns/models/food_101_v3/retrained_labels.txt \
--summaries_dir=$HOME/dcnns/models/food_101_v3/retrain_logs \
--how_many_training_steps=20000 \
--learning_rate=0.005 \
--model_dir=$HOME/data/models/food_101_v3/inception \
--bottleneck_dir=$HOME/data/models/food_101/bottlenecks \
