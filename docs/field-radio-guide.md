# Field Radio Guide

## What Is Field Radio?

Field Radio is a **station of short audio notes** on monitoring, evaluation and development practice from the ImpactMojo team. It is not a podcast: there are no numbered episodes, no seasons, and nothing to subscribe to. You press play and listen in. Video explainers moved to [Field Talkies](/field-talkies.html) on 13 November 2026.

Field Radio is **free, browser-based, and requires no login**. Every clip streams on the page and carries a full transcript, so it is readable as well as listenable.

### How Field Radio Differs from the Podcast

- **The Podcast** ([Between the Logframes](podcast-guide.md)) is a produced, long-form show: structured conversations, edited, released as episodes.
- **Field Radio** is the opposite: short audio notes, most of them under two minutes, each on one idea from practice. One voice, one point, no production.

If you want a deep conversation, use the podcast. If you want one idea in a minute or two, tune in to Field Radio.

---

## What's on the Station

Field Radio currently carries **12 clips**, all audio, across ImpactMojo's thematic tracks. Each clip lists:

- **Speaker and role**, who is talking and what they do.
- **Track**: the thematic area (MEL, gender, data, facilitation, and so on).
- **Duration and date.**
- **Transcript**: the full text of the clip, for accessibility and for readers who prefer to skim.

Browse the station at [/field-radio.html](/field-radio.html).

---

## Finding a Clip

Every clip has its own entry in site search, so you can reach one without listening through the station. Three things will find it:

- **The title or what it argues**: searching `weekly challenge` or `logframe` returns the clips that cover it.
- **The speaker or the track**: searching `Vandana` or `MEL & Research` returns their clips.
- **Something that was said in it.** Transcripts are searched too, so a half-remembered phrase works: `invisible if statements`, `visit registers`, `transport or digital devices`. These matches are listed after the title matches, so searching for a course still returns the course first.

Each result links straight to its clip, `/field-radio.html#fr-08` opens the station with that clip loaded and paused, ready to play. The same link works for sharing a single clip with someone. An older link to a video clip, such as `/field-radio.html#vs-08`, now opens that film on Field Talkies.

---

## How Clips Are Organised

Field Radio is deliberately un-structured to listen to, you can just press play and let it run, but under the hood every clip is tagged by **track** so the station can be filtered. There is no algorithm and no ranking: clips are surfaced by track and recency, not by popularity.

The station data lives in `data/field-radio.json`; each entry has an `id`, `type`, `title`, `speaker`, `role`, `track`, `src`, `duration`, `date`, and `transcript`.

---

## Contributing a Clip

Practitioners are welcome to send in their own voice notes. The clips on the station today come from the ImpactMojo team. If you have a reflection, a field tip, or an honest question from your work, you can contribute:

- Keep it short (roughly 30 seconds to two minutes).
- Say who you are and what track it belongs to.
- Record it however you can: a phone voice note is perfect.

See [How to Contribute](contributing.md) or write to `hello@impactmojo.in` to get a clip on the station.

---

## Accessibility

Every clip ships with a **full transcript**, so Field Radio works whether you listen or read. The station's play, previous and next buttons are keyboard-operable. There is no autoplay.

---

## Related

- [Field Talkies](/field-talkies.html): the video explainers, including the films that used to play on this station.
- [Podcast Guide](podcast-guide.md): the produced long-form show.
- [Reading Companions Guide](book-summaries-guide.md): interactive companions to key texts.
- [How to Contribute](contributing.md): how community members add content.
