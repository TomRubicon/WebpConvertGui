# .GIF to .WEBP Converter
![batchwebpscreen](https://user-images.githubusercontent.com/1091484/152843081-eb81e709-90bd-4a7e-b1da-f0c601924376.png)

GUI for Google’s gif2webp conversion tool! I made this while working on a gif gallery website and couldn’t find any offline tools for converting a batch of gif files. 
-	Convert entire directories of gif files into webp with one click
-	Generate static thumbnail files during conversion

## Installation
Clone the repository and install the requirements with pip:

    $ git clone https://github.com/TomRubicon/WebpConvertGui.git
    $ pip install -r requirements.txt

Next download gif2webp/webpmux executables and place them in the script directory!

- [Download webp tools here!](https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html)

- [Webp tools documentation](https://developers.google.com/speed/webp/docs/gif2webp)

Finally run the script!

    $ python main.py
    
Enjoy!

## Made with
- Python 3.8.1
- PySide 6.0.2
