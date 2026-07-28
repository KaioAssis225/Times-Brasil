---
name: teach
description: Teach the user a new skill or concept statefully within a teaching workspace using personalized HTML lessons, learning records, and resources.
disable-model-invocation: true
argument-hint: "What would you like to learn about?"
---

The user has asked you to teach them something. This is a stateful request - they intend to learn the topic over multiple sessions.

## Teaching Workspace

Treat the current directory as a teaching workspace. The state of their learning is captured in this directory in several files:

- `MISSION.md`: A document capturing the _reason_ the user is interested in the topic. This should be used to ground all teaching. Use the format in [MISSION-FORMAT.md](./MISSION-FORMAT.md).
- `./reference/*.html`: A directory of reference materials. These are the compressed learnings from the lessons - cheat sheets, reference algorithms, syntax, glossaries. They are designed for quick reference.
- `RESOURCES.md`: A list of resources which can be explored to ground your teaching in contextual knowledge, or to acquire knowledge and wisdom. Use the format in [RESOURCES-FORMAT.md](./RESOURCES-FORMAT.md).
- `./learning-records/*.md`: A directory of learning records, which capture what the user has learned. These capture non-obvious lessons and key insights that steer future sessions (`0001-<dash-case-name>.md`). Use the format in [LEARNING-RECORD-FORMAT.md](./LEARNING-RECORD-FORMAT.md).
- `./lessons/*.html`: A directory of lessons. A **lesson** is a single, self-contained HTML output that teaches one tightly-scoped thing tied to the mission. This is the primary unit of teaching in this workspace.
- `./assets/*`: Reusable **components** shared across lessons.
- `NOTES.md`: A scratchpad for you to jot down user preferences, or working notes.

## Philosophy

To learn at a deep level, the user needs three things:
- **Knowledge**, captured from high-quality, high-trust resources
- **Skills**, acquired through highly-relevant interactive lessons
- **Wisdom**, which comes from interacting with practitioners and applying concepts

### Fluency vs Storage Strength
Focus on long-term retention (**storage strength**) via desirable difficulty:
- Retrieval practice (recall from memory)
- Spacing (distributing practice over time)
- Interleaving (mixing up related topics/skills)

## Lessons
Each lesson is one self-contained HTML file saved to `./lessons/0001-<dash-case-name>.html` with clean typography and interactive/clear exercises.
