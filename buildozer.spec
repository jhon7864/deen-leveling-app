[app]
title = Deen Leveling
package.name = deenleveling
package.domain = org.deenleveling

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.0

orientation = portrait
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, minimum API supported by buildozer/kivy right now
android.api = 33
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
