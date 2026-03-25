# Design System Document: The Industrial Alchemist

## 1. Overview & Creative North Star
**Creative North Star: "The Industrial Alchemist"**
This design system moves away from the sterile, "template-ready" look of standard academic portals. Instead, it embraces a high-end editorial aesthetic that mirrors a modern industrial laboratory: precise, sophisticated, and intentionally layered. 

We break the "standard grid" by utilizing **asymmetric whitespace** and **tonal depth**. The UI is not a flat plane; it is a series of stacked, semi-transparent materials. By utilizing heavy "Manrope" display type against the utilitarian "Inter" body text, we create a visual dialogue between authoritative research and functional data.

---

## 2. Colors & Surface Philosophy
The palette is rooted in the "Deep Forest" of Kasetsart University, transitioned into a high-tech laboratory context.

### The "No-Line" Rule
**Prohibit 1px solid borders for sectioning.** Boundaries must be defined solely through background color shifts or subtle tonal transitions. A `surface-container-low` section sitting on a `surface` background provides enough contrast to define a zone without the visual "noise" of a stroke.

### Surface Hierarchy & Nesting
Treat the UI as physical layers of frosted glass and heavy vellum.
*   **Base Layer:** `surface` (#f8faf9)
*   **Secondary Zones:** `surface-container-low` (#f2f4f3)
*   **Interactive Cards:** `surface-container-lowest` (#ffffff)
*   **High-Priority Overlays:** `surface-bright` (#f8faf9) with a 60% opacity backdrop blur.

### The "Glass & Gradient" Rule
To avoid a flat "Bootstrap" feel, use **Glassmorphism** for floating sidebars or headers. 
*   **Formula:** `background: surface-container-lowest` at 80% opacity + `backdrop-filter: blur(12px)`.
*   **Signature Textures:** Apply a subtle linear gradient to primary actions: `primary` (#00534e) to `primary_container` (#016d67). This adds a "machined metal" sheen appropriate for an industrial lab.

---

## 3. Typography: The Editorial Edge
We use typography as a structural element, not just for legibility.

*   **Display & Headlines (Manrope):** These are your "Anchors." Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for hero sections. This conveys the "Academic Authority."
*   **Body & Labels (Inter):** These are your "Instruments." Inter’s high x-height ensures that complex laboratory data in tables remains legible even at `body-sm`.
*   **Hierarchy Note:** Always pair a `headline-sm` in Dark Green (`primary`) with a `label-md` in `outline` (#6e7978) to create a sophisticated, high-contrast metadata lockup.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are too "web-standard." We use **Ambient Depth**.

*   **The Layering Principle:** Place a `surface-container-lowest` card on a `surface-container-low` section. This creates a soft, natural "lift."
*   **Ambient Shadows:** For floating modals, use a "Shadow-Tint."
    *   *Blur:* 40px | *Opacity:* 6% | *Color:* `on-surface` (#191c1c). This mimics natural laboratory lighting.
*   **The Ghost Border Fallback:** If a border is required for accessibility in forms, use `outline_variant` at **20% opacity**. Never use 100% opaque borders.
*   **Glassmorphism:** Use for "Lab Status" floating widgets to ensure the underlying data tables remain partially visible, maintaining the user's context.

---

## 5. Components: Precision Instruments

### Buttons
*   **Primary:** A "Machined" look. Background: Gradient of `primary` to `primary_container`. Radius: `md` (0.375rem). Use `on_primary` text.
*   **Secondary:** `surface-container-high` background with `primary` text. No border.
*   **Tertiary:** Ghost style. No background; `primary` text. On hover, shift background to `primary_fixed` at 10% opacity.

### Data Tables (The Lab Ledger)
*   **Forbid Divider Lines:** Separate rows using a subtle `surface-container-low` background on hover. 
*   **Header:** `label-md` in `on_surface_variant`, all-caps with 0.05em tracking.
*   **Cells:** Use `body-md`. For numerical data, use tabular lining figures to ensure columns align perfectly.

### Input Fields & Forms
*   **Styling:** Fields should be `surface-container-lowest` with a "Ghost Border" (10% `outline_variant`). 
*   **Focus State:** Instead of a thick border, use a 2px outer "glow" using `primary_fixed` and transition the background color slightly to `white`.

### Laboratory Chips
*   **Usage:** For material types (e.g., "Polypropylene," "HDPE").
*   **Style:** `secondary_container` background with `on_secondary_container` text. Use `sm` (0.125rem) roundedness for a more "industrial tag" feel rather than a "social media" pill.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** use asymmetrical margins (e.g., a wide left margin for titles, narrow for content) to create an editorial feel.
*   **Do** use `spacing-24` (5.5rem) to separate major research sections. Breathable space equals professional clarity.
*   **Do** use the `tertiary` (#74381f) sparingly for "Warning" or "High-Heat" lab alerts—it provides a sophisticated "industrial rust" contrast to the green.

### Don’t:
*   **Don’t** use 1px black or grey borders. Use background color shifts.
*   **Don’t** use standard "Drop Shadows." Use Tonal Layering or Ambient Shadows.
*   **Don’t** crowd data tables. Use `spacing-4` (0.9rem) of vertical padding within rows to allow data to breathe.
*   **Don’t** use pure black (#000). Always use `on_surface` (#191c1c) for text to maintain a premium, ink-on-paper look.