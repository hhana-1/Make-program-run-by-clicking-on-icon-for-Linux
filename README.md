Dont read me;

all important commands


<h1>How to configure Python program and it's icon to run from your computer as a program when you click it's cool icon</h1>

🐍 Python Virtual Environment & Manual Run
```bash
• source .venv/bin/activate — Activates your virtual environment.
• python3 stretch_reminder.py — Runs the script directly (closes if terminal closes).
• python3 stretch_reminder.py & disown — Runs the script in the background and disconnects it from the terminal so you can close it safely.
```


📦 PyInstaller Packaging
```bash
• pyinstaller --noconsole --onefile stretch_reminder.py — Bundles your script into a single, standalone background binary.
• pyinstaller --noconsole --onefile "stretch_reminder(copy).py" — Handles filenames containing parentheses by escaping them with quotes.
• ./dist/stretch_reminder — Executes your compiled application binary directly from the terminal for testing.
```


📁 Managing the Desktop Shortcut Launcher
```bash
• nano ~/.local/share/applications/stretch.desktop — Opens the editor to create or modify your application menu shortcut.
• chmod +x ~/.local/share/applications/stretch.desktop — Grants execution permissions to make the shortcut functional.
• update-desktop-database ~/.local/share/applications — Forces the desktop system to scan for changes to your local user shortcuts.
• cat ~/.local/share/applications/stretch.desktop — Prints out the contents of your shortcut file to verify paths or icons.
```


⚙️ Startup & Automation
```bash
• mkdir -p ~/.config/autostart — Creates the system folder for startup programs if it doesn't already exist.
• cp ~/.local/share/applications/stretch.desktop ~/.config/autostart/ — Copies your shortcut to the startup folder so it launches automatically at login.
• chmod +x ~/.config/autostart/stretch.desktop — Ensures the startup shortcut has permission to execute.
• rm ~/.config/autostart/stretch.desktop — Removes the application from the automatic startup routine.
```


🛑 Troubleshooting & Stopping the Script
```bash
• ls -l /home/hhulic/Documents/stretch_script/icon.svg — Verifies that your icon file exists exactly where specified and checks its spelling.
• pgrep -f stretch_reminder — Finds the process ID (PID) of the reminder script if it is running invisibly in the background.
• pkill -f stretch_reminder — Forcefully terminates all running background instances of your stretch reminder program.
Would you like me to show you how to troubleshoot the canvas window transparency layout on your desktop, or are the background reminders running smoothly now?
```


change in "• nano ~/.local/share/applications/stretch.desktop" to check if icon is working
```bash
Icon=accessories-calculator
Icon=/home/hhulic/Documents/stretch_script/icon.svg
```


If you want to make change go to your file

```bash
/home/hhulic/Documents/stretch_script/stretch_reminder.py
```
save your changes and then
re-run the PyInstaller bundle command to generate an updated executable:

```bash
pyinstaller --noconsole --onefile stretch_reminder.py
```

all of this is for Linux Ubuntu