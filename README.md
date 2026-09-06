# Deen Leveling — Kivy App (buildable to APK)

This is a real, runnable Kivy version of the app UI — same emerald/gold
theme as the HTML mockup, but this one can actually be compiled into an
installable Android `.apk`.

It currently uses placeholder numbers (see the `NumericProperty`
defaults in `main.py`). Swap the `TODO` in `log_quran()` — and add
similar calls elsewhere — to wire it up to the `deen_leveling` Python
package from earlier.

## Why I can't build the APK for you directly

Compiling an APK needs the Android SDK, NDK, and Gradle — several
gigabytes of tooling that has to be downloaded from the internet. The
environment I run in has no network access, so I can hand you a
project that builds correctly, but the actual build step has to happen
somewhere with internet access. Below are two ways to do that.

---

## Path A — Build in the cloud with GitHub Actions (recommended, no Linux needed)

This runs the whole Android toolchain on GitHub's servers for free —
you don't need Linux, Android Studio, or any local setup.

1. **Create a free GitHub account** if you don't have one (github.com).
2. **Create a new repository** (e.g. `deen-leveling-app`), and upload
   everything in this folder to it — `main.py`, `buildozer.spec`, and
   the `.github/workflows/build-apk.yml` file (keep that folder
   structure exactly as-is).
3. Go to the **Actions** tab of your new repo. You should see a
   workflow called "Build APK". Click it, then click **"Run workflow"**
   (or just push a commit — it also runs automatically on push to
   `main`).
4. Wait 10–20 minutes for the first build (it's downloading the
   Android SDK/NDK fresh). Later builds are much faster.
5. When it finishes, open the completed run and scroll to
   **Artifacts** — download `deen-leveling-apk`. Unzip it to get your
   `.apk` file.
6. Transfer that `.apk` to your phone (email it to yourself, Google
   Drive, USB cable — any method works).
7. On your phone: open the file. Android will ask to allow installs
   from this source (Settings → apps → allow "install unknown apps"
   for whichever app you used to open it) — approve it, then tap
   Install.

That's it — a real installed app icon on your home screen.

---

## Path B — Build locally with Buildozer (needs Linux or WSL2)

Buildozer only runs on Linux (or macOS, with more manual setup) — not
natively on Windows. If you're on Windows, install **WSL2** first
(Microsoft's official Linux-inside-Windows tool), then follow these
inside your Linux/WSL terminal:

1. Install system dependencies:
   ```
   sudo apt update
   sudo apt install -y python3-pip build-essential git python3-venv \
       zlib1g-dev libncurses5-dev libffi-dev libssl-dev autoconf \
       libtool pkg-config zip unzip openjdk-17-jdk
   ```
2. Install Buildozer:
   ```
   pip3 install --user buildozer cython
   ```
3. `cd` into this project folder (the one with `buildozer.spec` in it).
4. Run:
   ```
   buildozer android debug
   ```
   The first run downloads the Android SDK/NDK automatically (a few
   GB) — this can take 30–60+ minutes depending on your connection.
5. When it finishes, your APK is in `bin/deenleveling-0.1-debug.apk`.
6. Transfer it to your phone the same way as in Path A, step 6–7.

---

## After installing

This build uses placeholder data (86 Baraka, 4-day streak, etc.) — it
looks and taps like the app but doesn't persist real logs yet.
Connecting `deen_leveling/user.py` behind the "Log today's reading"
button (and similar for salah/fasting) is the next real step.
