# Handwriting Synthesis 2025 - Setup Guide

## Project Overview

This project implements handwriting synthesis using Recurrent Neural Networks (RNNs), based on the paper "Generating Sequences with Recurrent Neural Networks" by Alex Graves. It generates realistic handwritten text in SVG format.

## Project Structure

### Core Files
- **`hand.py`** - Main `Hand` class that provides the API for generating handwriting
- **`demo.py`** - Demo script showing various usage examples
- **`rnn.py`** - RNN model implementation
- **`rnn_cell.py`** - Custom LSTM attention cell implementation
- **`rnn_ops.py`** - Custom RNN operations
- **`drawing.py`** - Utilities for drawing and processing strokes
- **`data_frame.py`** - Data handling utilities
- **`tf_base_model.py`** - Base TensorFlow model class
- **`tf_utils.py`** - TensorFlow utility functions

### Data Files
- **`checkpoints/`** - Contains pretrained model checkpoints
- **`styles/`** - Contains style files for different handwriting styles
- **`data/`** - Training data (if you want to train your own model)
- **`img/`** - Output SVG files

## Setup Status

### ✅ Completed
1. **Fixed requirements.txt** - Removed malformed Python version constraints and updated TensorFlow version
2. **Created virtual environment** - Set up Python virtual environment
3. **Installed dependencies** - All required packages installed:
   - TensorFlow 2.20.0
   - TensorFlow Probability 0.25.0
   - tf-keras 2.20.1
   - matplotlib, pandas, scikit-learn, scipy, svgwrite
4. **Fixed TensorFlow Probability compatibility** - Upgraded to version compatible with TF 2.20

### ✅ All Issues Resolved

**RNNCell API Compatibility**: Fixed by using TensorFlow's internal API `tensorflow.python.ops.rnn_cell_impl` which still provides the RNNCell class and LSTMCell implementation needed by the code.

**NumPy Deprecation**: Fixed deprecated `numpy.ndarray.tostring()` by replacing it with `tobytes()`.

The project is now fully functional and ready to use!

## Installation Instructions

### Prerequisites
- Python 3.13.7 (or compatible version)
- pip

### Steps

1. **Navigate to project directory:**
   ```bash
   cd handwriting-synthesis-2025
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies (if not already done):**
   ```bash
   pip install -r requirements.txt
   pip install tf-keras  # Required for TensorFlow Probability
   ```

## Usage

The project is now fully functional! You can use it like this:

### Basic Usage

```python
from hand import Hand

hand = Hand()

lines = [
    "Hello, world!",
    "This is handwriting synthesis."
]
biases = [0.75, 0.75]  # Controls neatness (0.5-1.0)
styles = [9, 9]  # Style number (0-12)

hand.write(
    filename='img/output.svg',
    lines=lines,
    biases=biases,
    styles=styles
)
```

### Advanced Usage

```python
lines = [
    "Now this is a story all about how",
    "My life got flipped turned upside down",
]
biases = [.75 for i in lines]
styles = [9 for i in lines]
stroke_colors = ['red', 'green']
stroke_widths = [1, 2]

hand.write(
    filename='img/usage_demo.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)
```

### Running the Demo

```bash
python demo.py
```

This will generate several SVG files in the `img/` directory.

## Dependencies

- **TensorFlow 2.20.0** - Deep learning framework
- **TensorFlow Probability 0.25.0** - For probability distributions
- **tf-keras 2.20.1** - Required for TensorFlow Probability compatibility
- **matplotlib** - Plotting
- **pandas** - Data manipulation
- **scikit-learn** - Machine learning utilities
- **scipy** - Scientific computing
- **svgwrite** - SVG file generation
- **numpy** - Numerical computing

## File Descriptions

### `hand.py`
The main interface for generating handwriting. The `Hand` class:
- Loads the pretrained model
- Provides the `write()` method to generate handwriting
- Handles text encoding and stroke generation
- Converts strokes to SVG format

### `rnn.py`
Implements the RNN model:
- Defines the model architecture
- Handles training and inference
- Manages model checkpoints

### `rnn_cell.py`
Custom LSTM cell with attention mechanism:
- Implements the attention mechanism for character alignment
- Uses 3 LSTM layers
- Generates stroke parameters using mixture models

### `drawing.py`
Utilities for:
- Encoding/decoding text to/from the model's alphabet
- Converting stroke offsets to coordinates
- Aligning and denoising strokes
- Drawing strokes to SVG

### `demo.py`
Example usage showing:
- Basic handwriting generation
- Style variation
- Bias variation
- Custom colors and stroke widths

## Verification

The project has been tested and verified to work correctly:

1. ✅ **RNNCell compatibility** - Fixed by using internal TensorFlow API
2. ✅ **NumPy deprecation** - Fixed by using `tobytes()` instead of `tostring()`
3. ✅ **Demo script** - Runs successfully and generates SVG output files
4. ✅ **Output files** - All demo SVG files are generated correctly in the `img/` directory

You can now run the demo with:
```bash
source venv/bin/activate
python demo.py
```

This will generate several SVG files demonstrating different handwriting styles and biases.

## Resources

- Original paper: [Generating Sequences with Recurrent Neural Networks](https://arxiv.org/abs/1308.0850)
- Original repository: [jpangburn/handwriting-synthesis](https://github.com/jpangburn/handwriting-synthesis)
- Fork repository: [spotshare-nick/handwriting-synthesis-2025](https://github.com/spotshare-nick/handwriting-synthesis-2025)

## Notes

- The project uses TensorFlow v1 compatibility mode (`tf.compat.v1`)
- Deprecation warnings are expected and can be ignored for now
- The pretrained model is included in the `checkpoints/` directory
- Style files are in the `styles/` directory (styles 0-12)

