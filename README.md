# Text finder in images

A Python script that search for specific texts in images by directory. 
The script uses [Tesseract](https://github.com/tesseract-ocr/tesseract) 

# Usage

## Development
To test the script you have to install Tesseract on your computer.
Then you can test the script via : 
```
$ Python index.py -test
```
## Production
To create the .exe file with embedded Tesseract, you can use PyInstaller :
```
 $ python -m PyInstaller --collect-data palettable --onefile index.py --add-data "C:\Program Files\Tesseract-OCR\;."
```

# License
The MIT License (MIT) 2023 - [Maxence Duboille](https://github.com/MaxDbll). Please have a look at the [LICENSE.md](LICENSE.md) for more details.
