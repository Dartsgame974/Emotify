

# Emotify - Image Resizer for Twitch and Discord Emotes

![Emotify Logo](https://github.com/Dartsgame974/Emotify/blob/main/icon.png?raw=true)

Emotify is a Python script with a simple UI that allows you to resize images to the correct formats for Twitch emotes, Twitch bits, Twitch channel points, and Discord emotes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Future Features](#future-features)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Emotify is a handy tool for streamers and Discord server owners who need to resize their custom emotes to the required dimensions for Twitch and Discord. The script automatically organizes the resized emotes into separate folders based on their types - Points de chaines, Discord, and Bits.

### Supported Resizing Dimensions

- Twitch: 72x72, 36x36, 18x18
- Discord: 256x256
- Points de chaîne: 28x28, 56x56, 112x112

## Features

- Simple and user-friendly UI
- Easily resize multiple files at once
- Automatic organization of emotes into appropriate folders
- Supports PNG image format

## Usage



```bash
git clone https://github.com/Dartsgame974/Emotify.git



Alternatively, download the ZIP file and extract it to your desired location.

## How to Use

1. Launch the executable file "Emotify.exe" or run in cmd with
```bash
main.py

2. Choose the directory of folder contains allthe emote  you want to resize:
   - Twitch emotes (72x72, 36x36, 18x18): `Bits` folder
   - Discord emotes (256x256): `Discord` folder
   - Twitch channel points emotes (28x28, 56x56, 112x112): `Points_de_chaines` folder
3. Run the following command:

```bash
python emotify.py

