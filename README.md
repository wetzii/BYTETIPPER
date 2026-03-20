# BYTETIPPER 🤖

An auto-typer script that automatically sends keystrokes to your active window using Python.

> ⚠️ **Disclaimer:** This tool is intended for **personal automation and gaming purposes only** (e.g., Roblox auto-clickers/openers). **Do NOT use this to fake activity at work or school.** Using it to simulate presence or work output is dishonest and may violate your employer's or institution's policies.

---

## What it does

BYTETIPPER uses [`pyautogui`](https://pyautogui.readthedocs.io/) to simulate keyboard input on your computer. In its default configuration, it types the shortcut `syso` followed by `Enter` — which in IDEs like Eclipse or IntelliJ auto-expands to `System.out.println()` in Java.

You can easily adapt the script to type any key sequence you want, for example to automate repetitive in-game actions in Roblox.

---

## Requirements

- Python 3.x
- `pyautogui` library

Install the dependency with:

```bash
pip install pyautogui
```

---

## How to use

1. **Open the target window** (your game, IDE, etc.)
2. **Run the script:**

```bash
python BYTETIPPER.py
```

3. **Click into the target window quickly** — `pyautogui` will send keystrokes to whatever window is currently focused.

> 💡 **Tip:** You have about 1 second after running the script before it starts typing. Switch to your target window in that time.

---

## Customization

You can easily change what gets typed by editing the `pyautogui.press()` calls in `BYTETIPPER.py`.

### Example: Type something different

```python
# Original: types "syso" + Enter
pyautogui.press('s')
pyautogui.press('y')
pyautogui.press('s')
pyautogui.press('o')
pyautogui.press('enter')
```

### Example: Type a full string at once

```python
import pyautogui
import time

time.sleep(2)  # Give yourself time to switch windows
pyautogui.typewrite('hello world', interval=0.1)
pyautogui.press('enter')
```

### Example: Repeat the action in a loop

```python
import pyautogui
import time
import random

time.sleep(2)

for _ in range(10):
    pyautogui.press('e')          # e.g., open an egg in Roblox
    pyautogui.press('enter')
    time.sleep(random.uniform(1, 3))  # random delay to seem more natural
```

---

## The `givRandTime()` function

The script includes a helper function that returns a random wait time between 1 and 3 seconds:

```python
def givRandTime() -> int:
    return random.randint(1, 3)
```

You can use this with `time.sleep(givRandTime())` inside a loop to add randomized delays between actions — useful for avoiding detection in games or making the automation feel less robotic.

---

## ⚠️ Important Notes

- `pyautogui` takes control of your keyboard and mouse. **Move the mouse to a corner of the screen to abort** (this triggers pyautogui's fail-safe).
- Always make sure the **correct window is focused** before the script runs.
- Some games or applications may block or detect automated input.

---

## License

See `LICENSE` for details.