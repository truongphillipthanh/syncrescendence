# Ghostty Click Events Thread

Ghostty nightly now supports the `click_events` extension introduced by Kitty and supported by Fish. If you're using Fish 4.1+, you can click (no modifiers!) anywhere at a prompt to move the mouse. I believe Ghostty is the first to support this extension outside of Kitty.

As far as as I can find, the only shell to support this is Fish (4.1+) and the only terminal to support this previously is Kitty. It'd be great for more of both ecosystems to support this.

Other terminals do support moving the cursor with the mouse to some extent (Ghostty included since 1.0), but do so by another, more fragile mechanism: when you click, it just best-effort calculates a number of synthetic left arrow key inputs to pretend to move your cursor. This is super fragile because it can't take into account shell behaviors particularly around indention, multi-line, and if you're not at a prompt at all...

The `click_events` extension allows Ghostty to know when you're at a prompt line, and works by encoding a mouse click event while at a prompt line to the shell. The shell then takes over and handles all the logic of moving the cursor, which makes the most sense!

PR: https://github.com/ghostty-org/ghostty/pull/10536

(Description: Embedded video showing a terminal window with timestamp "Mon Feb 2 11:06:30 2026" and text reading "click_events example!" demonstrating the feature in action)

---

**11:07 AM · Feb 2, 2026**
340.5K Views | 65 replies | 80 reposts | 1.8K likes | 499 bookmarks

---

## Thread Responses

It's here, but you need to dig into the source or write dummy programs (I did the latter) to figure out how it works. I regret adding the fragile alt+click mechanism to xterm.js, I think it was a community contribution but it's flaky by design which isn't...

I'm implementing OSC133 `cl` support now, which I'm not sure... anyone? supports. But it'll help our own shell integration

---

I think iTerm2 supports nav via synthetic arrow keys, but I'm not sure what their full OSC133 story is. Ghostty has the synthetic arrow keys fallback too for non-OSC133 enabled shells, but it has the various limitations noted in my original post.

---

Search has been in nightly since the fall

---

I use Nu, but Fish is dramatically better than Zsh. :)

---

March. We do 6 month cycles.

---

I use Nu haha.

---

Been there since like October or Nov, it's in nightly

---

Man I hope they did this right, but I'm suspicious. I'll have to try a build. Note this is different from my tweet though, Zsh appears to be supporting `cl=m`, not `click_events`.

---

Fish or Nu.

---

It uses a completely different mechanism

---

Warps great and their editor experience is top notch for a terminal but they use a different mechanism.

---

Yep

---

Please be more specific, there are no known memory leaks in Ghostty presently. If you have core dumps or other metadata we can look at to debug, I'll of course drop everything to do so. Most reports on X are memes.

---

macOS does its fully automated

---

I said that, wishing you the best in your learning to read journey 🙏