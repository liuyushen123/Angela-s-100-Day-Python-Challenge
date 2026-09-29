# Day 65 — UX (User Experience) Design

## What Is UX Design?

UX (User Experience) design is the practice of shaping how a product **feels to use** — how easy, efficient, satisfying, and frustration-free the journey is from the moment a user arrives to the moment they accomplish their goal. It's not about how things look (that's UI); it's about how things _work_ for a real person.

A useful definition: **UX is the sum of every interaction a user has with a product**, and UX design is the deliberate practice of making that sum positive.

---

## 1. The Five Planes of UX (Jesse James Garrett's Model)

A widely-used framework for thinking about UX, from abstract to concrete:

| Plane         | Question It Answers                                       | Example                                         |
| ------------- | --------------------------------------------------------- | ----------------------------------------------- |
| **Strategy**  | What do we want to achieve, and what do users need?       | Business goals + user needs                     |
| **Scope**     | What features and content will the product include?       | Feature list, content requirements              |
| **Structure** | How is it organized, and how does a user move through it? | Information architecture, user flows            |
| **Skeleton**  | Where do elements sit on the page?                        | Wireframes, layout                              |
| **Surface**   | What does it actually look like?                          | Visual design (colors, typography — this is UI) |

UX work happens mostly in the first three planes; UI work happens mostly in the last two — but they overlap and inform each other constantly.

---

## 2. Core UX Principles

- **Usability** — can a user complete their goal without confusion or unnecessary steps?
- **Findability** — can users locate what they're looking for easily (navigation, search, labeling)?
- **Accessibility** — does the experience work for users with disabilities?
- **Credibility** — does the product feel trustworthy and professional?
- **Desirability** — does the experience evoke a positive emotional response, not just a functional one?
- **Value** — does the product actually deliver something useful to both the user and the business?

_(These six, plus "Usefulness," come from Peter Morville's "User Experience Honeycomb" — a well-known UX framework.)_

---

## 3. User Research: Understanding Who You're Designing For

Good UX starts before any design work — with understanding real users:

- **User Personas** — fictional profiles representing key user types (goals, frustrations, behaviors), used to keep design decisions grounded in real needs rather than assumptions
- **User Interviews / Surveys** — direct feedback from real or potential users
- **Competitive Analysis** — studying how similar products solve (or fail to solve) the same problems
- **Analytics Review** — using existing data (drop-off points, click patterns) to understand real behavior, not just stated preferences

---

## 4. Information Architecture (IA)

IA is how content and features are organized and labeled so users can navigate intuitively.

- **Navigation** — menus, breadcrumbs, and links that help users understand where they are and where they can go
- **Labeling** — using language users actually understand (not internal jargon) for menu items, buttons, and categories
- **Card Sorting** — a common UX research method where users group content themselves, revealing how they naturally expect information to be organized

---

## 5. User Flows and Journey Mapping

- **User Flow** — a step-by-step diagram of the path a user takes to complete a specific task (e.g. Sign up → Verify email → Complete profile → Dashboard). Used to spot unnecessary steps or friction points before any code is written.
- **User Journey Map** — a broader view of a user's entire experience with a product over time, including their emotions at each stage (frustration, delight, confusion) — helps identify not just _what_ happens but _how it feels_.

---

## 6. Wireframing and Prototyping

Part of UX work is translating research and flows into testable structure, before visual design begins:

- **Low-fidelity wireframes** — simple black-and-white sketches focused purely on layout and hierarchy, not colors or fonts. Fast to make and easy to change.
- **High-fidelity prototypes** — interactive, often clickable mockups (built in tools like Figma) that simulate the real experience closely enough to user-test before writing production code.

The goal of prototyping before development: catch usability problems **cheaply**, before time is spent building the wrong thing.

---

## 7. Usability Testing

Even well-researched designs need to be validated with real users:

- **Moderated testing** — watching a real user attempt tasks live, asking questions as they go
- **Unmoderated testing** — users complete tasks independently (often via remote tools), recorded for later review
- **A/B Testing** — showing two versions of a design to different user groups to see which performs better on a specific metric (conversions, time-on-task, etc.)

A common rule of thumb (Jakob Nielsen): **testing with just 5 users** typically uncovers the majority of major usability problems — you don't need hundreds of testers to find real issues.

---

## 8. Common UX Laws Worth Knowing

| Law              | What It Says                                                                                                                                   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hick's Law**   | The more choices you give someone, the longer it takes them to decide — simplify options where possible                                        |
| **Fitts's Law**  | The time to reach a target depends on its size and distance — make important buttons big and close to where users already are                  |
| **Jakob's Law**  | Users spend most of their time on _other_ sites, so they expect yours to work the same familiar way — don't reinvent conventions unnecessarily |
| **Miller's Law** | The average person can hold about 7 (±2) items in working memory — don't overload menus or forms                                               |

---

## 9. UX vs. UI — A Quick Recap

|              | UX                                             | UI                                         |
| ------------ | ---------------------------------------------- | ------------------------------------------ |
| Focus        | The experience and how it feels                | The visuals and how it looks               |
| Deliverables | Personas, user flows, wireframes, journey maps | Mockups, color palettes, typography, icons |
| Key Question | "Does this make sense and work well?"          | "Does this look good and match the brand?" |
| Tools        | Sticky notes, flow diagrams, research          | Figma, color tools, font pairing           |

Both are essential — a beautifully designed screen that confuses users fails just as much as an intuitive flow that looks unpolished and untrustworthy.

---

## Key Takeaways

- UX is about the _entire experience_ of using a product, not just how it looks.
- Good UX starts with research (personas, interviews, analytics) before any visual design happens.
- Information architecture and user flows reduce friction by organizing content the way users actually think.
- Wireframes/prototypes let you catch usability problems cheaply, before writing real code.
- Usability testing (even with just a handful of users) reveals real problems that assumptions miss.
- UX laws like Hick's, Fitts's, and Jakob's give concrete, testable guidance for reducing friction in design decisions.
