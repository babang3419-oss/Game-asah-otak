[app]
title = Asah Otak
package.name = asahotak
package.domain = org.game
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,sdl2,sdl2_image,sdl2_ttf
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.accept_sdk_license = True
android.archs = arm64-v8a
android.api = 31
android.min_api = 21
android.ndk = 23b

[buildozer]
log_level = 2
warn_on_root = 1
