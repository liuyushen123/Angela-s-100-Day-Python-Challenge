# Day 65 — Understanding Typography and How to Choose Fonts

## Why Typography Matters

Typography is more than "picking a nice font" — it shapes how readable, trustworthy, and professional a website feels before a visitor reads a single word. Good typography guides the eye, establishes hierarchy, and reinforces a brand's tone (playful, serious, modern, traditional).

---

## 1. Anatomy of a Typeface

Key terms you'll see when reading about fonts:

- **Baseline** — the invisible line letters sit on
- **x-height** — the height of lowercase letters (like "x"), excluding ascenders/descenders
- **Ascender** — the part of a letter that rises above the x-height (e.g. the stem of "b", "d", "h")
- **Descender** — the part that drops below the baseline (e.g. the tail of "g", "p", "y")
- **Serif** — the small decorative stroke at the end of a letter's main strokes
- **Kerning** — the space between individual letter pairs
- **Tracking / Letter-spacing** — uniform spacing applied across a whole word or block of text
- **Leading / Line-height** — the vertical space between lines of text

---

## 2. Serif vs. Sans-Serif

| Type           | Description                                                                                    | Feel                             | Common Use                                 |
| -------------- | ---------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------ |
| **Serif**      | Has small strokes/feet at the end of letters (e.g. Times New Roman, Georgia, Playfair Display) | Traditional, formal, trustworthy | Newspapers, editorial sites, luxury brands |
| **Sans-serif** | No decorative strokes — clean, geometric (e.g. Helvetica, Arial, Roboto, Open Sans)            | Modern, clean, minimal           | Tech companies, startups, UI/dashboards    |

**Rule of thumb:** Sans-serif tends to be more legible on screens at small sizes, which is why most body text on websites defaults to it. Serif fonts often work well for large display headings where their character can shine.

---

## 3. Other Typeface Categories

- **Slab Serif** — thick, blocky serifs (e.g. Roboto Slab) → bold, confident, great for headlines
- **Script / Handwriting** — mimics cursive or handwritten text (e.g. Pacifico) → decorative, personal, use sparingly
- **Display** — highly stylized, made for large headlines, not body text (e.g. Lobster)
- **Monospace** — every character takes equal width (e.g. Courier, Fira Code) → used for code snippets, technical feel

---

## 4. Choosing Fonts for a Website

### a) Limit yourself to 2–3 fonts max

Too many typefaces on one page creates visual noise. A common, safe combination:

- **1 font for headings** (can have more personality/weight)
- **1 font for body text** (must be highly legible)
- _(Optional)_ 1 accent font for small details (buttons, labels)

### b) Pair fonts with contrast, not similarity

Good pairings usually combine **a serif + a sans-serif**, or **a display font + a simple sans-serif** for body text — this creates visual hierarchy without clashing. Pairing two very similar-looking fonts (e.g. two thin sans-serifs) often looks like a mistake rather than a design choice.

### c) Match the font's tone to your brand

Ask: does this font _feel_ like the brand?

- Rounded, soft fonts → friendly, approachable
- Sharp, geometric fonts → modern, tech-forward
- Serif with high contrast strokes → elegant, upscale
- Bold, condensed fonts → energetic, sporty

### d) Check legibility at multiple sizes

A font that looks great as a huge headline might become unreadable at 14px body-text size. Always test both.

---

## 5. Using Google Fonts (Practical Implementation)

Since this bootcamp uses Google Fonts throughout the web development section, the standard workflow is:

1. Go to [fonts.google.com](https://fonts.google.com)
2. Pick a font and select the weights/styles you need
3. Copy the `<link>` tag into your HTML `<head>`:
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com" />
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
   <link
     href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap"
     rel="stylesheet"
   />
   ```
4. Reference it in your CSS with a fallback stack:
   ```css
   body {
     font-family: "Poppins", sans-serif;
   }
   ```

**Always include a fallback font** (like `sans-serif` or `serif`) after your chosen font — if the custom font fails to load, the browser falls back to a similar system font instead of an unstyled default.

---

## 6. Establishing Type Hierarchy

Typography isn't just font choice — it's also about **size, weight, and spacing** to guide the reader:

```css
h1 {
  font-size: 3rem;
  font-weight: 700;
}
h2 {
  font-size: 2rem;
  font-weight: 600;
}
p {
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.6;
}
```

A good hierarchy means a user can scan a page and immediately understand what's most important, without reading every word.

---

## Key Takeaways

- Typography sets the tone of a website before any content is read.
- Stick to 2–3 fonts per project — one for headings, one for body text.
- Pair fonts with contrast (serif + sans-serif) rather than similarity.
- Always test legibility at real-world sizes, not just in a font preview.
- Use Google Fonts + a fallback font stack for reliable, free web fonts.
- Font size, weight, and line-height build hierarchy just as much as the typeface itself.
