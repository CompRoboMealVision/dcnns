python $HOME/tensorflow/tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=$HOME/data/models/food_101/bottlenecks \
--how_many_training_steps 5000 \
--model_dir=$HOME/data/models/food_101/inception \
--output_graph=$HOME/data/models/food_101/retrained_graph.pb \
--output_labels=$HOME/data/models/food_101/retrained_labels.txt \
--image_dir $HOME/data/food_101/images
