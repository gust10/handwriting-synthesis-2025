# Valid Characters for Handwriting Synthesis

The model only supports a limited character set. Any character not in this list will cause an error.

## Complete Character List

### Letters (Uppercase)
**A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V, W, Y**

**Note:** Missing letters: **Q, X, Z** (uppercase)

### Letters (Lowercase)
**a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z**

**Note:** All lowercase letters are supported

### Numbers
**0, 1, 2, 3, 4, 5, 6, 7, 8, 9**

### Punctuation & Symbols
- **Space** ` ` (space character)
- **!** (exclamation mark)
- **"** (double quote)
- **#** (hash/pound)
- **'** (single quote/apostrophe)
- **(** (left parenthesis)
- **)** (right parenthesis)
- **,** (comma)
- **-** (hyphen/dash)
- **.** (period/dot)
- **:** (colon)
- **;** (semicolon)
- **?** (question mark)

### Special Character
- **\x00** (null character - used internally, not for user input)

## NOT Supported (Common Characters That Will Cause Errors)

❌ **=** (equals sign) → Use "equals" instead
❌ **/** (forward slash) → Use "divided by" or "per" instead
❌ **+** (plus sign) → Use "plus" instead
❌ **-** (minus sign) → Use "minus" or "negative" instead (but **-** is supported!)
❌ **×** or **\*** (multiplication) → Use "x" or "times" instead
❌ **²** (superscript 2) → Use "squared" instead
❌ **³** (superscript 3) → Use "cubed" instead
❌ **⁻¹** (superscript -1) → Use "per" or "to the negative one" instead
❌ **⁻²** (superscript -2) → Use "per squared" instead
❌ **√** (square root) → Use "square root" instead
❌ **π** (pi) → Use "pi" instead
❌ **θ** (theta) → Use "theta" instead
❌ **α** (alpha) → Use "alpha" instead
❌ **β** (beta) → Use "beta" instead
❌ **%** (percent) → Use "percent" instead
❌ **$** (dollar sign) → Use "dollars" instead
❌ **€** (euro) → Use "euros" instead
❌ **£** (pound) → Use "pounds" instead
❌ **@** (at sign) → Use "at" instead
❌ **&** (ampersand) → Use "and" instead
❌ **[** or **]** (square brackets) → Use parentheses instead
❌ **{** or **}** (curly braces) → Use parentheses instead
❌ **<** or **>** (angle brackets) → Use "less than" or "greater than" instead
❌ **|** (pipe) → Not supported
❌ **\** (backslash) → Not supported
❌ **~** (tilde) → Not supported
❌ **^** (caret) → Use "to the power of" instead
❌ **_** (underscore) → Not supported

## Examples: Converting Unsupported Characters

### Mathematical Equations

**Before (unsupported):**
```
v² = u² + 2as
s = (v² - u²) / (2a)
E = mc²
```

**After (supported):**
```
v squared equals u squared plus 2as
s equals (v squared - u squared) divided by (2a)
E equals mc squared
```

### Fractions

**Before (unsupported):**
```
x = 1/2
y = 3/4
```

**After (supported):**
```
x equals 1 divided by 2
y equals 3 divided by 4
```

### Units

**Before (unsupported):**
```
v = 12 m/s
a = 9.81 m/s²
```

**After (supported):**
```
v equals 12 m per s
a equals 9.81 m per s squared
```

### Currency

**Before (unsupported):**
```
Price: $10.99
Cost: €5.50
```

**After (supported):**
```
Price: 10 dollars and 99 cents
Cost: 5 euros and 50 cents
```

## Quick Reference

**Supported:**
- All lowercase letters (a-z)
- Most uppercase letters (A-Y, missing Q, X, Z)
- Numbers (0-9)
- Basic punctuation: `! " # ' ( ) , - . : ; ?`
- Space

**Not Supported:**
- Mathematical operators: `= + / * × ÷`
- Superscripts/subscripts: `² ³ ⁻¹`
- Special symbols: `@ $ % & [ ] { } < > | \ ~ ^ _`
- Greek letters: `α β θ π`
- Currency symbols: `$ € £ ¥`
- Other Unicode characters

## Tips

1. **Spell out mathematical operations**: Use "equals", "plus", "minus", "divided by", "times"
2. **Use words for superscripts**: "squared", "cubed", "to the power of"
3. **Avoid special symbols**: Replace with words or supported characters
4. **Test your text**: If you get a `ValueError: Invalid character`, check this list
5. **Use parentheses**: `()` are supported and can help structure equations

## Character Count

- **Total valid characters: 75**
- **Letters: 49** (23 uppercase + 26 lowercase)
- **Numbers: 10** (0-9)
- **Punctuation: 15** (space, !, ", #, ', (, ), ,, -, ., :, ;, ?)
- **Special: 1** (\x00 - internal use only)

