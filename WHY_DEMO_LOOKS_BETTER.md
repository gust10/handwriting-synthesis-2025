# Why demo.py Has Really Good Output

## Key Differences

### 1. **Style Priming (Most Important!)**

When you provide `styles`, the model uses **style priming** - a technique that dramatically improves output quality.

**What happens:**
- The model loads example strokes from the style file (e.g., `styles/style-9-strokes.npy`)
- It prepends these example strokes to your text as a "reference"
- The neural network sees: `[example handwriting] + " " + [your text]`
- This teaches the model the handwriting style before generating your text

**In demo.py:**
```python
styles = [9 for i in lines]   # ✅ Style priming enabled
styles = [12 for i in lines]  # ✅ Style priming enabled
styles = [7 for i in lines]  # ✅ Style priming enabled
```

**In example_usage.py:**
```python
# Example 1: No styles - NO priming ❌
hand.write(lines=[...])  # Missing styles parameter

# Examples 2-4: Has styles - priming enabled ✅
styles=[9, 9, 9]  # Style priming enabled
```

**Code evidence (hand.py lines 75-87):**
```python
if styles is not None:  # If styles provided
    # Load example strokes from that style
    x_p = np.load('styles/style-{}-strokes.npy'.format(style))
    c_p = np.load('styles/style-{}-chars.npy'.format(style))
    
    # Prepend example to your text
    c_p = str(c_p) + " " + cs  # Example + " " + Your text
    
    # Use this for priming
    x_prime[i, :len(x_p), :] = x_p  # Prime with example strokes
```

**Result:** Style priming makes the output much more consistent and realistic because the model has a reference example to follow.

---

### 2. **Better Style Numbers**

Different style numbers represent different handwriting samples from the training data. Some styles are better quality than others.

**demo.py uses:**
- Style **9** - appears to be a well-trained style
- Style **12** - another good style
- Style **7** - also good quality

**example_usage.py uses:**
- Style **0, 5, 9** - mixed quality (style 0 might be less polished)
- Style **9** - same as demo, should be good

**Tip:** Styles 7, 9, and 12 seem to be particularly well-trained. Try different styles to find which ones work best for your use case.

---

### 3. **Longer, More Natural Text**

**demo.py:**
```python
lines = [
    "Now this is a story all about how",
    "My life got flipped turned upside down",
    # ... longer, natural sentences
]
```

**example_usage.py:**
```python
lines = [
    "Hello, world!",  # Short, simple
    "This is simple handwriting."  # Short, simple
]
```

**Why this matters:**
- The model was trained on longer sequences
- Longer text gives the model more context to work with
- Natural language flows better than short phrases
- The attention mechanism works better with more characters

---

### 4. **Consistent Bias = 0.75**

**demo.py:**
```python
biases = [.75 for i in lines]  # Consistent 0.75
```

**example_usage.py:**
```python
biases=[0.75, 0.75]  # Also 0.75, but...
biases=[0.5, 0.75, 1.0]  # Example 3 varies
```

**Why 0.75 is good:**
- Balance between natural (0.5) and neat (1.0)
- Not too messy, not too rigid
- Sweet spot for realistic handwriting

---

## How to Get Better Output

### ✅ Always Use Style Priming

```python
hand.write(
    filename='output.svg',
    lines=['Your text'],
    styles=[9]  # ← Always include this!
)
```

### ✅ Use Well-Trained Styles

Try these styles (in order of quality):
- **Style 9** - Very good (used in demo)
- **Style 12** - Very good (used in demo)
- **Style 7** - Good (used in demo)
- **Style 0-6, 8, 10-11** - Varies, test them

### ✅ Use Longer, Natural Text

```python
# Good:
lines = [
    "This is a longer sentence that flows naturally.",
    "The model works better with complete thoughts."
]

# Less ideal:
lines = [
    "Short",
    "Text"
]
```

### ✅ Use Bias 0.75

```python
biases = [0.75 for i in lines]  # Sweet spot
```

### ✅ Complete Example

```python
from hand import Hand

hand = Hand()

hand.write(
    filename='best_output.svg',
    lines=[
        "This is a longer sentence for better results.",
        "Style priming makes a huge difference!",
        "Always specify a style number."
    ],
    biases=[0.75, 0.75, 0.75],  # Consistent neatness
    styles=[9, 9, 9]  # ✅ Style priming enabled!
)
```

---

## Summary

**The #1 reason demo.py looks better: Style Priming**

When you provide `styles`, the model:
1. Loads example handwriting from that style
2. Uses it as a reference/prime
3. Generates your text in that same style
4. Results in much more consistent, realistic output

**Always include `styles=[9]` (or another style number) for best results!**

