# tf_plot_metrics

Opinionated performance plotting for TensorFlow models.

# Usage

```py
import tensorflow as tf
import tf_plot_metrics

model = tf.keras.Sequential([...])
model.compile(...)
model.fit(...)

# use tf_plot_metrics()
tf_plot_metrics(model)
```