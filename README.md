# Tailo Typer GUI

Tailo Typer GUI is a small Windows desktop app for converting Taiwanese Hokkien Tai-lo written with tone numbers into tone-marked Tai-lo.

For example, you can type:

```text
ta2 si7
```

and the app will convert it to:

```text
tá sī
```

The app runs locally on your computer. It does not use the internet, does not use global hotkeys, and does not require AutoHotkey.

## What Is Included

Keep these files together in the same folder:

```text
tailo-typer-gui
├── Basic-Tones_v2.png
├── README.md
└── src
    ├── __init__.py
    ├── gui_app.py
    └── tailo_converter.py
```

The most important files are:

- `src\gui_app.py`: the Windows desktop app.
- `src\tailo_converter.py`: the conversion engine.
- `Basic-Tones_v2.png`: the tones chart shown in the app.
- `README.md`: these instructions.

Do not move `gui_app.py` away from the `src` folder unless you know how to update the file paths.

## What You Need Before Running It

You need a Windows computer with Python installed.

Use Python 3.10 or newer. Python 3.11 or 3.12 is also fine.

You do not need to install any extra Python packages.

## Step 1: Check Whether Python Is Already Installed

1. Click the Windows Start button.
2. Type `PowerShell`.
3. Open **Windows PowerShell**.
4. Type this command and press Enter:

```powershell
py --version
```

If Python is installed, you should see something like:

```text
Python 3.12.3
```

The exact version number may be different. That is okay as long as it is Python 3.10 or newer.

If you see an error saying `py` is not recognized, try this command:

```powershell
python --version
```

If that shows a Python version, you can still run the app. Use `python` in the run commands instead of `py`.

If neither command works, install Python using the next section.

## Step 2: Install Python If Needed

1. Go to the official Python website:

   <https://www.python.org/downloads/windows/>

2. Download the latest Windows installer.
3. Open the installer.
4. On the first installer screen, check the box that says:

```text
Add python.exe to PATH
```

5. Click **Install Now**.
6. Wait for installation to finish.
7. Close and reopen PowerShell.
8. Check the install by running:

```powershell
py --version
```

If you see a Python version, you are ready.

## Step 3: Open the App Folder

Put the `tailo-typer-gui` folder somewhere easy to find, such as your Desktop or Documents folder.

For example, your project folder might be located at:

```text
C:\Path\To\tailo-typer-gui
```

Use the actual folder location on your own computer in the commands below.

## Step 4: Run the App From PowerShell

1. Open PowerShell.
2. Go to the app folder by typing:

```powershell
cd C:\Path\To\tailo-typer-gui
```

3. Run the app:

```powershell
py src\gui_app.py
```

If your computer uses `python` instead of `py`, run this instead:

```powershell
python src\gui_app.py
```

A window titled **Tailo Typer GUI** should open.

## Step 5: Run the App by Double-Clicking

You may also be able to run the app by double-clicking this file:

```text
src\gui_app.py
```

If double-clicking works, the Tailo Typer GUI window will open.

If double-clicking does not work, use the PowerShell method above. The PowerShell method is more reliable.

## How To Use The App

1. Look at the tones chart at the top of the window.
2. Type tone-number Tai-lo in the input box.
3. Click **Convert**.
4. The tone-marked Tai-lo appears in the output box.
5. Click **Copy Output** if you want to copy the converted text.
6. Paste the copied text wherever you need it.
7. Click **Clear** to empty the input and output boxes.

## Example Input And Output

Input:

```text
ta2 si7 kap4 sih8
```

Output:

```text
tá sī kap si̍h
```

Tone 4 usually has no written tone mark, so `kap4` becomes `kap`.

Tone 8 is shown with a vertical mark, so `sih8` becomes `si̍h`.

## Tone 4 And Tone 8 Warnings

Tailo Typer GUI includes an optional warning check for tone 4 and tone 8.

In Tai-lo, syllables with tone 4 or tone 8 usually end in one of these letters:

```text
p, t, k, h
```

Examples that look okay:

```text
kap4
sih8
pak4
lik8
```

Examples that will show a warning:

```text
ta4
a8
si8
loo4
```

The warning does not stop the conversion. It is only a reminder to check the spelling.

If you type:

```text
ta4 a8
```

The app will still convert the text, but the warning area below the output box will say that those syllables use tone 4 or tone 8 without ending in `p`, `t`, `k`, or `h`.

## Copy Output Button

The **Copy Output** button copies the converted text to your Windows clipboard.

That means it replaces whatever you previously copied.

This is normal clipboard behavior.

## Clear Button

The **Clear** button removes:

- the input text
- the output text
- the warning/status message

After clearing, you can type a new example.

## Troubleshooting

### The App Does Not Open When I Double-Click It

Use PowerShell instead:

```powershell
cd C:\Path\To\tailo-typer-gui
py src\gui_app.py
```

If that does not work, try:

```powershell
cd C:\Path\To\tailo-typer-gui
python src\gui_app.py
```

### PowerShell Says `py` Is Not Recognized

Try:

```powershell
python --version
```

If that works, run the app with:

```powershell
python src\gui_app.py
```

If `python` is also not recognized, install Python from the official website:

<https://www.python.org/downloads/windows/>

### The Tones Chart Does Not Appear

Make sure this file is still in the main project folder:

```text
Basic-Tones_v2.png
```

The app expects the image to be next to `README.md`, not inside the `src` folder.

### The App Opens But Conversion Looks Wrong

Check that you are typing tone numbers immediately after each syllable, like this:

```text
ta2 si7 kap4
```

Do not put a space between the syllable and its tone number.

Use this:

```text
ta2
```

Not this:

```text
ta 2
```

## Safety Notes

This app is designed to be simple and local.

It does not:

- connect to the internet
- send your text anywhere
- read personal files
- use AutoHotkey
- use global hotkeys
- install background services

It only converts text typed into the app window.

The **Copy Output** button writes the converted output to your clipboard when you click it.

## Sharing With Friends

The safest transparent way to share this app is to share the folder as source files instead of sending an `.exe`.

That means your friends can see the Python files before running them.

To share it, send the whole `tailo-typer-gui` folder, including:

```text
Basic-Tones_v2.png
README.md
src\gui_app.py
src\tailo_converter.py
src\__init__.py
```

Your friends will need Python installed. Then they can run:

```powershell
cd path\to\tailo-typer-gui
py src\gui_app.py
```

Replace `path\to\tailo-typer-gui` with the real folder location on their computer.

## Command-Line Converter

The original command-line converter is still available.

From the project folder, run:

```powershell
py src\tailo_converter.py ta2 si7
```

This should print:

```text
tá sī
```


