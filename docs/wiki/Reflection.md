**English** · [Dansk](Reflection-da) · [Bahasa Malaysia](Reflection-ms)

# Reflection

The assignment ends with a reflection: how the project was approached, what was hard and easy, and what to do differently. This is a draft; the Product Owner rewrites it in their own words.

## How did I approach the project?

I wrote the plan and the design before the code: who the program is for, one use case (upload, add a watermark, save), a domain model and a class diagram. Then I built it in four steps, one branch and one pull request per step, with a screenshot for each, so every step could be checked on its own.

## What was hard?

- **Tkinter alone is not enough.** It cannot read JPEG files or blend a watermark with transparency, so Pillow became the one runtime dependency.
- **Keeping the window apart from the rules.** The picture and the watermark rules live in layers that do not know Tkinter; the window only shows them. It took more thought at the start and paid back later.
- **Testing a window.** A graphical test must not take over the desktop, so graphical tests and screenshots run in a Linux container with a virtual display.

## What was easy?

- Placing a watermark in one of nine places is plain arithmetic once the margin rule is written down.
- The rules of the watermark were easy to test, because they need no window.

## What was my biggest learning?

Writing down the use case and the contracts first made each step small and clear. The code mostly followed the design, and when it did not, I changed the design on purpose and reviewed it again.

## What would I do differently?

- Start with the Pillow decision, so the first picture-reading code is written once.
- Take the screenshots from the first step on, instead of adding the harness later.
- Try a second watermark at the same time (text and logo together) and a batch of pictures, as the next project.
