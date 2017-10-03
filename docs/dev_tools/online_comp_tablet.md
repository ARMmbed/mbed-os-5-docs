# Guide to the mbed Online Compiler on tablet devices

You can log in to the mbed Online Compiler from any PC and continue where you left off. We've pushed that portability one step further by adding touch support for tablet devices.

The mbed Online Compiler uses touch control to deliver state-of-the-art editing and intuitive workspace management. The following guide explains the basics, limitations and workarounds to enable efficient workflow.

This guide is applicable to Android- and iOS-enabled tablet devices. We'll update it once we add support for tablets based on other platforms, such as Surface and ChromeOS.

## Browser choices and limitations
Choosing a browser is the first and most important step because it defines how the compiled program binaries are handled, how fast the mbed Online Compiler performs and how it uses the screen space.

**Android** is liberal toward changing the default browser and open access to the file system. The default Android browser will not let you save the compiled binary files if you intend to connect the mbed board to the tablet. We recommend the Chrome and Dolphin browsers over the default one because both of them handle the download of binary files gracefully, and Dolphin can enable a full screen view of the mbed Online Compiler, which increases the usable screen space. You can then move the downloaded programs to the mbed flash drive using a file manager, such as Astro or EStrong File Manager from the Google Play store.

**iOS** is strict toward security, and changing the default browser might not be the better choice because the default browser, Safari, receives JavaScript Nitro acceleration through the OS. The Safari browser also allows adding the mbed Online Compiler as the native home screen application (see the images below), which is a helpful shortcut and enables full screen mode.

<span class="images">![](images/add_to_homescreen_1.png)</span>
<span class="images">![](images/add_to_homescreen_2.png)</span>

Due to iOS restrictions, you cannot directly access the filesystem on the mbed board (given that it's connected via iPad/iPhone USB adapter, which also means that **you cannot save the compiled binary files to an mbed board**.

## Touch control method
The mbed Online Compiler touch support consists of two different control methods - editing and workspace management.

### Editor
 * Single tap - Moves the cursor to the tapped position.
 * Double tap - Selects text on the tapped word and opens context menu.
 * Triple tap - Selects text on the tapped row and opens context menu.
 * Tap-hold - Opens the context menu.
 * Tap-drag - Begins text selection mode until the touch is released (and opens context menu).

### Compiler IDE
 * Single tap - Equivalent to single mouse click.
 * Double tap - Equivalent to double mouse click.
 * Tap-hold - Equivalent to right click (context menu).
 * Tap-drag - Equivalent to mouse dragging.

They are different, but each is intuitive for the type of task for which it is designed.

## Editing input methods
Although using the touch control method can be comfortable and intuitive, many developers don't find the virtual keyboard capable of long development cycles, mainly due to the lack of physical separation between the keyboard buttons and the lack of key click feedback. Both can cause typing errors. The two-finger shortcuts present on Android (they are not available on iOS) can be problematic. There is also a lack of tab key and copy/paste shortcuts. All of these issues can reduce the editing capabilities.

To solve these problems, several editing input options are available. Some of them are valuable, and others are proof of concept.

#### Virtual keyboard
The **Android** platform offers virtual keyboard skinning, keyboard gesturing and other input methods as part of the platform design. Each hardware vendor extends the Android default virtual keyboard with its own implementation(s), and the Google Play store offers even more virtual keyboard solutions. There are various development-friendly layouts that will make development easier and more enjoyable.

The **iOS** platform doesn't allow customized keyboard layouts, and the most common special characters, such as Tab, brackets, braces, parentheses, greater than and less than symbols, Colon, Semicolon and numbers are two or three taps away on the default keyboard layout or nowhere to be found.

A visual workaround for the iOS 5+ virtual keyboard is to split it using the two-finger split gesture:

<span class="images">![](images/split_keyboard.png)</span>

This reduces the size the of keyboard and makes it semitransparent but doesn't extend the set of keys.

You can also reposition the virtual keyboard by dragging the right side of the button on the lower right (the horizontal stripes).

#### Cover/built-in keyboard
Some tablets, such as the [Asus Transformer](http://en.wikipedia.org/wiki/Asus_Eee_Pad_Transformer) are bundled with a nicely designed, state-of-the-art, space-saving, tablet-protecting keyboard cover, which turns the tablet into a thin, lightweight, 10" laptop-like device.

Others, such as the iPad, use hard covers, such as the [Logitech Keyboard Case](http://www.google.com/search?q=logitech+keyboard+case&tbm=isch), for an extra cost, which enable the complete set of keys.

#### Mini Bluetooth keyboard
There are various [mini bluetooth keyboards](http://www.google.com/search?q=mini+bluetooth+keyboard&tbm=isch) that vary in price. Although they are not popular for daily use, once you get used to one, you can type quickly on it.

#### Wired keyboard
Both Android- and iOS-based tablets support a USB attached keyboard because they contain a normal USB port, either natively or through an adapter.

However, if you are carrying a wired keyboard, you may as well use a laptop.

## Workflow
See our walk-through video about touch control features (best preview in full screen, 1080p).

<span class="images">[![Video tutorial](http://img.youtube.com/vi/PI1Kq9RSN_Y/0.jpg)](http://www.youtube.com/watch?v=YEHrlvhvhDM)</span>

Note that the actual performance is much better than shown in the video. The screen recording in 2048x1536 resolution took a large chunk of the tablet CPU performance!

## Conclusion
Tablets are powerful, lightweight, portable devices with intuitive and relatively accurate pointing precision that are capable of delivering both platform-based and web-based applications, the key ingredient for the mbed Online Compiler to exist on a tablet ecosystem.

Although tablets lack a physical keyboard, you can still manage your workspace, publish, import and make minor source code modifications. If you plan to fully develop on a tablet though, buy a keyboard extension/bundle, and save yourself the frustration of the virtual keyboard.

If you plan to connect an mbed board, remember that the iOS platform is restrictive toward file access, and even if you're able to download and save the program binary, you can't save it directly on the mbed board. This is unfortunate because the (retina) screen of iOS-based tablets is in comfortable 4:3 format, and the platform manages to deliver sleek performance with no slowdown or problems.

On the performance side, Android isn't too far behind iOS, especially after the Android 4.0.4 update. Most importantly, it doesn't have the restrictions of iOS. Therefore, **Android is the first platform fully capable of rapid prototyping: create in the mbed Online Compiler, experiment on an mbed board and share on the mbed website with the mbed community**.

## Compatibility list
Different mbed boards have different power consumption ratings, and different tablets can deliver different amounts of power to USB ports. Use this mbed microcontroller compatibility list if only the tablet USB port is powering an mbed board, and there are no other consumers or devices attached to the mbed board itself.

All mbed boards are designed to run on backup battery power with minimal USB power drain, which makes it possible to use an mbed board on a tablet that has limited USB power.

**Legend:**

 * <span class="images">![](images/check_ok.png)</span> - The board is powered and accessible.
 * <span class="images">![](images/check_not.png)</span> - The board isn't powered or hardware limitation occurs.
 * o - The filesystem is restricted by the platform.
 * w - The filesystem cannot be accessed due to insufficient power.
 * p - The filesystem can be accessed but errors may occur due to power fluctuations.
 * * - There is an issue or regression - see the comments below.
 * ? - Untested.

|Tablet|mbed NXP LPC11U24|mbed NXP LPC1768|mbed NXP LPC2368|
|---:|---:|---:|---:|
|Apple iPad 1|<span class="images">![](images/check_ok.png)</span>o?|<span class="images">![](images/check_not.png)</span>wo|<span class="images">![](images/check_not.png)</span>wo|
|Apple iPad 2/3|<span class="images">![](images/check_ok.png)</span>o|<span class="images">![](images/check_not.png)</span>wo|<span class="images">![](images/check_not.png)</span>wo|
|Asus EEE Transformer TF101|<span class="images">![](images/check_ok.png)</span>|<span class="images">![](images/check_ok.png)</span>*|?|
|Motorola Xoom|<span class="images">![](images/check_ok.png)</span>|?|?|

Do you have a tablet not listed above? Do you want to contribute to the list? Please send us the details corresponding to the compatibility list, and we will add it.