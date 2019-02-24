# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device athene
%define vendor motorola

# Manufacturer and device name to be shown in UI
%define vendor_pretty Moto
%define device_pretty G4

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

