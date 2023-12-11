# SpeedNN

The aim of SpeedNN is to aggregate common neural network architectures in an easy-to-use API.

SpeedNN will provide **easy-to-use TensorFlow wrappers** for the following tasks:

- Regression
- Text Classification
- Text Generation
- Image Classification
- Image Segmentation
- Siamese Networks
- and many more...

Example usage:
```py
import speednn
from speednn import ImgClassifier

# load data from TensorFlow Datasets
ds_train, ds_test = speednn.get_tfds("mnist")

# build an image classification model with 5 convolution layers and 3 feed forward layers
# data normalization, batching, shuffling, and prefetching is automatically handled
c = ImgClassifier(ds_train, ds_test, conv=5, ffn=3)

# train image classifier
c.fit(epochs=100, reduce_lr=True, stop_early=True, patience=10)

# plot loss and accuracy
speednn.plot_metrics(c)
```

In just 4 lines you can create an image classifier model.

SpeedNN will abstract away the boring boilerplate code so you can focus on solving problems with neural nets.

SpeedNN  will automatically take care of the following tasks:
- Learning rate reduction
- Early stopping
- Logging of various types
- Other custom callbacks

SpeedNN will also offer a ton of helper methods for evaluating model performance:
- Plot loss
- Plot accuracy
- Analyse fine-tuning performance gains

SpeedNN will be built on top of TensorFlow, so you can easily integrate additional TensorFlow functionality.