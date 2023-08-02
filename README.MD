

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

To use Emotify, follow these steps:

1. Download and install Python from [https://www.python.org](https://www.python.org).
2. Clone this repository to your local machine or download the ZIP file and extract it.
3. Place your emote images (in PNG format) in the respective folders - `Points_de_chaines`, `Discord`, and `Bits`.
4. Run the `emotify.py` script.
5. Emotify will automatically resize the images and save them in the appropriate folders.

## Installation

1. Ensure you have Python installed on your system. If not, download and install it from [https://www.python.org](https://www.python.org).
2. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Dartsgame974/Emotify.git



Alternatively, download the ZIP file and extract it to your desired location.

## How to Use

1. Navigate to the `emotify` directory in your terminal or command prompt.
2. Place the emote images you want to resize in the respective folders:
   - Twitch emotes (72x72, 36x36, 18x18): `Bits` folder
   - Discord emotes (256x256): `Discord` folder
   - Twitch channel points emotes (28x28, 56x56, 112x112): `Points_de_chaines` folder
3. Run the following command:

```bash
python emotify.py

