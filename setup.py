from setuptools import setup, find_packages

VERSION = '1.0.1' 
DESCRIPTION = 'Opinionated performance plotting for TensorFlow models.'
LONG_DESCRIPTION = """tf_plot_metrics provides a function to easily plot graphs for evaluating TensorFlow model performance.

See https://github.com/raj-pulapakura/tf_plot_metrics for documentation."""

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="tf_plot_metrics", 
        version=VERSION,
        author="Raj Pulapakura",
        author_email="<raj.pulapakura@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["matplotlib"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package', "tensorflow"],
        classifiers= [
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ],
        url="https://github.com/raj-pulapakura/tf_plot_metrics"
)