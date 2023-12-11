import matplotlib.pyplot as plt

def tf_plot_metrics(model, metrics=["loss", "accuracy"], plot_val=True, row=True, grid=True, figsize=None):
    try:
        hist = model.history.history
        if figsize is None:
            figsize=(20, 5) if row else (20, 20)
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
    except AttributeError:
        print("Model has not been fitted yet.")