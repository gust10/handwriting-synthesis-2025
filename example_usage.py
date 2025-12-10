"""
Simple example showing how to use the handwriting synthesis tool
"""
from hand import Hand

# Initialize the Hand class (loads the pretrained model)
hand = Hand()

# Example 1: Basic usage (with style priming for better quality)
print("Example 1: Basic handwriting")
hand.write(
    filename='img/example1.svg',
    lines=[
        "Hello, world!",
        "This is simple handwriting."
    ],
    biases=[0.75, 0.75],
    styles=[9, 9]  # Style priming enabled for better quality
)

# Example 2: With custom styles and colors
print("Example 2: Custom styles and colors")
hand.write(
    filename='img/example2.svg',
    lines=[
        "Line 1 in style 0",
        "Line 2 in style 5",
        "Line 3 in style 9"
    ],
    biases=[0.75, 0.75, 0.75],
    styles=[0, 5, 9],
    stroke_colors=['red', 'blue', 'green'],
    stroke_widths=[1, 2, 3]
)

# Example 3: Different biases (neatness)
print("Example 3: Different neatness levels")
hand.write(
    filename='img/example3.svg',
    lines=[
        "Messy (bias 0.5)",
        "Normal (bias 0.75)",
        "Neat (bias 1.0)"
    ],
    biases=[0.5, 0.75, 1.0],
    styles=[9, 9, 9]
)

# Example 4: Essay on boredom and creativity
print("Example 4: Essay on boredom")
hand.write(
    filename='img/example4.svg',
    lines=[
        "In an age where every idle moment is filled with scrolling,",
        "notifications, and endless content, boredom has become the enemy.",
        "We treat it like a bug in the system rather than a feature.",
        "Yet boredom is one of humanity's most underappreciated superpowers.",
        "",
        "When the mind is under-stimulated, it doesn't shut down - it rebels.",
        "It starts connecting ideas that seemed unrelated, daydreaming scenarios",
        "that have no immediate payoff, and asking questions we're usually too",
        "busy to entertain. Most great insights, inventions, and works of art",
        "began in moments of what looked like wasted time. Newton watched an",
        "apple fall because he had nothing better to do that afternoon.",
        "J.K. Rowling sketched the first ideas of Harry Potter on a delayed",
        "train with only a pen and boredom as companions.",
        "",
        "Modern life has engineered boredom out of existence. The average person",
        "checks their phone 150 times a day. We have perfected the art of",
        "distraction so thoroughly that silence feels uncomfortable, empty space",
        "feels wrong. But creativity abhors a vacuum only when the vacuum is",
        "feared. When we learn to sit with emptiness, the mind floods it with",
        "something new.",
        "",
        "Children understand this intuitively. Give a child a cardboard box and",
        "twenty uninterrupted minutes, and it becomes a spaceship, a castle, a",
        "time machine. Adults have simply forgotten the rules of the game:",
        "boredom is the price of admission to imagination.",
        "",
        "We don't need more stimuli; we need more gaps. The courage to be bored",
        "- to stare out a window, to walk without podcasts, to lie in bed",
        "without reaching for the phone - is the closest thing our",
        "over-scheduled brains have to a reset button.",
        "",
        "In the end, the most productive thing you can do is sometimes nothing",
        "at all. Let yourself be bored. Something interesting is trying to",
        "find you."
    ],
    biases=[0.75] * 34,
    styles=[5] * 34
)

print("\nAll examples saved to img/ directory!")

