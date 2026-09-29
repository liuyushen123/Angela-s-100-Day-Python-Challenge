# Day 65 — Understanding Color Theory

## Why Color Theory Matters

Color isn't decoration — it drives emotion, guides attention, signals meaning (errors in red, success in green), and reinforces brand identity. Getting it wrong makes a site feel cheap or confusing; getting it right makes design feel intentional even before a user reads any text.

---

## 1. The Color Wheel Basics

- **Primary colors** — Red, Blue, Yellow (can't be made by mixing others)
- **Secondary colors** — Green, Orange, Purple (made by mixing two primaries)
- **Tertiary colors** — mixes of a primary and a neighboring secondary (e.g. Red-Orange)

### Key relationships on the wheel:

| Relationship            | Description                                              | Effect                                                        |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------- |
| **Complementary**       | Colors directly opposite each other (e.g. blue & orange) | High contrast, vibrant, energetic — great for calls-to-action |
| **Analogous**           | Colors next to each other (e.g. blue, blue-green, green) | Harmonious, calm, easy on the eye                             |
| **Triadic**             | Three colors evenly spaced around the wheel              | Vibrant but balanced, more playful                            |
| **Monochromatic**       | Different shades/tints of a single color                 | Cohesive, minimal, elegant                                    |
| **Split-Complementary** | A base color + the two colors adjacent to its complement | High contrast but less tension than pure complementary        |

---

## 2. Hue, Saturation, Lightness (HSL)

Most CSS color pickers and design tools describe color using three properties:

- **Hue** — the color itself (0–360° on the color wheel: red, green, blue, etc.)
- **Saturation** — intensity/purity of the color (0% = gray, 100% = vivid)
- **Lightness** — how light or dark it is (0% = black, 100% = white)

```css
color: hsl(210, 80%, 50%); /* a vivid, medium blue */
```

Understanding HSL (rather than only hex codes) makes it much easier to create **consistent color variations** — e.g. keeping the same hue but adjusting lightness for hover states:

```css
.button {
  background-color: hsl(210, 80%, 50%);
}
.button:hover {
  background-color: hsl(210, 80%, 40%);
} /* darker on hover */
```

---

## 3. Warm vs. Cool Colors

| Type     | Colors              | Feel                                    |
| -------- | ------------------- | --------------------------------------- |
| **Warm** | Red, Orange, Yellow | Energy, urgency, excitement, appetite   |
| **Cool** | Blue, Green, Purple | Calm, trust, professionalism, stability |

Most sites use one temperature as the dominant tone and the other sparingly as an accent — e.g. a cool, trustworthy blue palette with a single warm orange "Buy Now" button to make it pop.

---

## 4. Color Psychology (General Associations)

| Color  | Common Association                                       |
| ------ | -------------------------------------------------------- |
| Red    | Urgency, passion, danger, appetite                       |
| Orange | Energy, friendliness, affordability                      |
| Yellow | Optimism, caution, attention                             |
| Green  | Growth, health, money, "go"/success                      |
| Blue   | Trust, calm, professionalism (most-used corporate color) |
| Purple | Luxury, creativity, wisdom                               |
| Black  | Sophistication, power, elegance                          |
| White  | Simplicity, cleanliness, space                           |

These are cultural generalizations, not universal rules — context, culture, and industry norms all shift what a color communicates.

---

## 5. Building a Website Color Palette

A simple, reliable structure most design systems use:

1. **Primary color** — your main brand color, used most often (nav bars, headers, links)
2. **Secondary color** — supports the primary, adds variety without competing
3. **Accent color** — used sparingly for calls-to-action (buttons, highlights) — should stand out clearly against the rest
4. **Neutral colors** — grays, blacks, whites for text, backgrounds, borders
5. **Semantic colors** — reserved meanings: red = error/danger, green = success, yellow = warning

**60-30-10 rule** (borrowed from interior design, applies well to UI):

- 60% dominant/neutral color (backgrounds)
- 30% secondary color (supporting elements)
- 10% accent color (buttons, highlights — the color you want the eye drawn to)

---

## 6. Contrast and Accessibility

Color choices must also account for **readability and accessibility**, not just aesthetics:

- Text needs sufficient contrast against its background to be readable (especially for visually impaired users)
- WCAG (Web Content Accessibility Guidelines) recommends a **contrast ratio of at least 4.5:1** for normal body text
- Never rely on color _alone_ to convey meaning (e.g. "click the green button" fails for colorblind users) — pair color with icons, labels, or text

Tools like [WebAIM's Contrast Checker](https://webaim.org/resources/contrastchecker/) let you test two colors against WCAG standards before finalizing a palette.

---

## 7. Practical Tools for Choosing Palettes

- **[Coolors.co](https://coolors.co)** — generate and lock in color palettes quickly
- **[Adobe Color](https://color.adobe.com)** — explore color wheel relationships visually
- **Google Fonts + Material Design color tool** — palettes designed with accessibility built-in

---

## Key Takeaways

- Use the color wheel relationships (complementary, analogous, triadic) to build intentional palettes, not random color guesses.
- HSL makes it easy to create consistent shade/tint variations (e.g. hover states) from a single hue.
- Warm colors energize, cool colors calm — most sites lean on one and use the other as an accent.
- Follow the 60-30-10 rule: dominant neutral, supporting secondary, small pop of accent color.
- Always check contrast ratios for accessibility — a beautiful palette that's unreadable is a failed palette.
