import matplotlib.pyplot as plt
from typing import List, Tuple

def tf_plot_metrics(model, metrics:List[str]=["loss", "accuracy"], plot_val:bool=True, row:bool=True, grid:bool=True, figsize:Tuple[int]=None):
    """Plots metrics of a TensorFlow model after it has been trained.

    Parameters
    ----------
    model : tf.keras.Model | tf.keras.Sequential, required
        Plot metrics of this model.

    metrics : list[str], optional
        The metrics to plot.\n
        These metrics should be defined when the model was compiled using the .compile() method.\n
        Default is `["loss", "accuracy"]`.

    plot_val : bool, optional
        If `True`, the validation metrics will be plotted.\n 
        If `False`, they will not be plotted.\n
        Default is `True`.

    row : bool, optional
        If `True`, plots will be arranged in a row.\n
        If `False`, plots will be arranged in a column.\n
        Default is `True`.

    grid : bool, optional
        If `True`, plots will show grid lines. \n
        If `False`, plots will not show grid lines.\n
        Default is `True`.

    figsize : tuple[int], optional
        Passed as `figsize` parameter to `plt.figure()`.\n
        Controls the size of the figure generated.\n
        Default is `None`, in which case a `figsize` will automatically be calculated.

        
    Raises
    ------
    NotImplementedError
        If no sound is set for the animal or passed in as a
        parameter.
    """
    
    try:
        hist = model.history.history
    except AttributeError:
        raise ModelNotFittedError("Model has not been fitted yet.")
    
    if len(metrics)==0:
        raise NoMetricsProvidedError("No metrics have been provided.")

    if figsize is None:
        figsize = (20, 5) if row else (20, 20)

    plt.figure(figsize=figsize)

    for i, metric in enumerate(metrics):
        plt.subplot(1 if row else len(metrics), 1 if not row else len(metrics), i+1)
        plt.plot(hist[metric], label=f"Training {metric}")
        if plot_val: plt.plot(hist[f"val_{metric}"], label=f"Validation {metric}")
        plt.xlabel("Epoch")
        plt.ylabel(metric.upper())
        plt.title(metric.upper())
        plt.legend()
        plt.grid(grid)

    plt.show()


class ModelNotFittedError(Exception):
    """Raised when model has not been fitted yet, so metrics are unavailable."""
    pass


class NoMetricsProvidedError(Exception):
    """"Raised when no metrics have been provided to plot."""
    pass