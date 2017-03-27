python $HOME/tensorflow/tensorflow/examples/image_retraining/retrain.py \
--image_dir=$HOME/data/food_101/images \
--output_graph=$HOME/data/models/food_101_v2/retrained_graph.pb \
--output_labels=$HOME/data/models/food_101_v2/retrained_labels.txt \
--summaries_dir=$HOME/data/models/food_101_v2/retrain_logs \
--how_many_training_steps=10000 \
--learning_rate=0.003 \
--model_dir=$HOME/data/models/food_101_v2/inception \
--bottleneck_dir=$HOME/data/models/food_101/bottlenecks \
