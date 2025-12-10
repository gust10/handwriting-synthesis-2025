# How to Use Handwriting Synthesis

## Basic Usage

```python
from hand import Hand

# Create a Hand instance (loads the pretrained model)
hand = Hand()

# Define your text as a list of lines
lines = [
    "Hello, world!",
    "This is line 2",
    "And this is line 3"
]

# Generate handwriting
hand.write(
    filename='output.svg',
    lines=lines
)
```

## Advanced Usage with Options

```python
hand = Hand()

lines = [
    "First line",
    "Second line",
    "Third line"
]

# Optional parameters:
biases = [0.75, 0.75, 0.75]  # Controls neatness (0.5-1.0, higher = neater)
styles = [9, 9, 9]           # Handwriting style (0-12, different styles)
stroke_colors = ['red', 'blue', 'green']  # Color for each line
stroke_widths = [2, 2, 2]    # Stroke thickness for each line

hand.write(
    filename='output.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)
```

## How It Works: Line Separation & Formatting

### 1. **Each Line is Processed Separately**

The key is in the `_draw` method (lines 111-149 in `hand.py`):

```python
# Each line gets its own stroke generation
for offsets, line, color, width in zip(strokes, lines, stroke_colors, stroke_widths):
    # Process each line independently
```

**What happens:**
- Each line in your `lines` list is sent to the neural network **separately**
- The RNN generates stroke coordinates (x, y, pen-up/pen-down) for **that specific line only**
- Each line is processed as an independent handwriting sample

### 2. **Vertical Spacing Between Lines**

The code uses a fixed `line_height = 60` pixels (line 115):

```python
line_height = 60  # Space between lines
view_height = line_height * (len(strokes) + 1)  # Total canvas height

initial_coord = np.array([0, -(3*line_height / 4)])  # Start position

# For each line:
# ... process and draw the line ...
initial_coord[1] -= line_height  # Move down for next line
```

**How it works:**
- Each line starts 60 pixels below the previous one
- The Y-coordinate is decremented by `line_height` after each line
- Empty lines (blank strings) still get spacing: `if not line: initial_coord[1] -= line_height`

### 3. **Horizontal Centering**

Each line is centered horizontally (line 137):

```python
strokes[:, 0] += (view_width - strokes[:, 0].max()) / 2
```

**What this does:**
- Calculates the width of the generated handwriting
- Centers it in the 1000-pixel-wide canvas
- Each line is centered independently

### 4. **No Word Wrapping - You Control Line Breaks**

**Important:** The model does NOT automatically wrap text. It treats each item in the `lines` list as a separate line.

```python
# This creates 1 line:
lines = ["This is one very long line that will not wrap"]

# This creates 3 lines:
lines = [
    "This is line 1",
    "This is line 2", 
    "This is line 3"
]
```

**Why it doesn't break:**
- Each line is limited to **75 characters max** (enforced in `write()` method, line 45)
- The neural network generates strokes for the entire line as one unit
- The RNN was trained to handle complete lines, not partial words

### 5. **Stroke Processing Pipeline**

For each line, the strokes go through several processing steps:

```python
# 1. Scale up the strokes (make them bigger)
offsets[:, :2] *= 1.5

# 2. Convert relative offsets to absolute coordinates
strokes = drawing.offsets_to_coords(offsets)

# 3. Smooth out noise/artifacts
strokes = drawing.denoise(strokes)

# 4. Correct for slant/rotation
strokes[:, :2] = drawing.align(strokes[:, :2])

# 5. Flip Y-axis (SVG coordinates)
strokes[:, 1] *= -1

# 6. Position relative to line position
strokes[:, :2] -= strokes[:, :2].min() + initial_coord

# 7. Center horizontally
strokes[:, 0] += (view_width - strokes[:, 0].max()) / 2
```

### 6. **SVG Path Generation**

Each line becomes an SVG path (lines 139-146):

```python
# Build SVG path string
p = "M{},{} ".format(0, 0)  # Move to start
for x, y, eos in zip(*strokes.T):
    # eos = end-of-stroke (pen up/down)
    if prev_eos == 1.0:
        p += 'M{},{} '.format(x, y)  # Move (pen up)
    else:
        p += 'L{},{} '.format(x, y)  # Line (pen down)
    prev_eos = eos

# Create SVG path element
path = svgwrite.path.Path(p)
path = path.stroke(color=color, width=width, linecap='round').fill("none")
dwg.add(path)  # Add to SVG document
```

## Example: Understanding the Flow

```python
lines = [
    "Hello",
    "World"
]

# Step 1: Neural network generates strokes for "Hello"
#   → Returns array of (x, y, pen_up) coordinates

# Step 2: Process "Hello" strokes
#   → Denoise, align, position at y=0

# Step 3: Draw "Hello" as SVG path

# Step 4: Move down 60 pixels (line_height)

# Step 5: Neural network generates strokes for "World"
#   → Returns array of (x, y, pen_up) coordinates

# Step 6: Process "World" strokes
#   → Denoise, align, position at y=-60

# Step 7: Draw "World" as SVG path

# Result: Two separate lines, 60 pixels apart, both centered
```

## Parameters Explained

### `biases` (0.5 to 1.0)
- **Lower (0.5)**: More natural, messier handwriting
- **Higher (0.75-1.0)**: Neater, more controlled handwriting
- One value per line

### `styles` (0 to 12)
- Different handwriting styles learned from training data
- Each number represents a different person's handwriting style
- One value per line (can vary per line for mixed styles)

### `stroke_colors` and `stroke_widths`
- Visual customization
- One value per line
- Default: black, width=2

## Limitations

1. **75 character limit per line** - Enforced to prevent model issues
2. **Limited character set** - Only supports characters in `drawing.alphabet`
3. **No automatic wrapping** - You must manually split long text into lines
4. **Fixed line spacing** - 60 pixels between lines (hardcoded)

## Tips

1. **For long text**: Split it yourself:
   ```python
   long_text = "This is a very long piece of text that needs to be split"
   lines = long_text.split()  # Split by spaces
   # Or manually:
   lines = [
       "This is a very long piece",
       "of text that needs to be",
       "split into multiple lines"
   ]
   ```

2. **For paragraphs**: Use empty strings for spacing:
   ```python
   lines = [
       "Paragraph 1 line 1",
       "Paragraph 1 line 2",
       "",  # Empty line for spacing
       "Paragraph 2 line 1"
   ]
   ```

3. **For different styles per line**:
   ```python
   styles = [0, 1, 2, 3]  # Different style for each line
   ```

4. **For emphasis**: Use different colors/widths:
   ```python
   stroke_colors = ['black', 'red', 'black']  # Middle line in red
   stroke_widths = [2, 3, 2]  # Middle line thicker
   ```

