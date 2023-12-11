# tf_plot_metrics

Opinionated performance plotting for TensorFlow models.

# Pip install

```
pip install tf_plot_metrics
```

# Usage

```py
import tensorflow as tf
from tf_plot_metrics import tf_plot_metrics

model = tf.keras.Sequential([...])
model.compile(...)
model.fit(...)

# use tf_plot_metrics()
tf_plot_metrics(model)
```

# Example output
![plot](https://github.com/raj-pulapakura/tf_plot_metrics/assets/87762282/ac9a9ef4-d6cd-4191-aee4-b4e8cd5071de)

