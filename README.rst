Kindle Clippings: Extract, Transform, Load
==========================================

Building on the `Kindle Clippings library`_...

.. _`Kindle Clippings library`:  https://github.com/MilkShakeYoung/kindle-clippings

- This script will **Extract** your 'My Clippings.txt' file from your Kindle
- **Transform** the plain text into Book, Quote pairs 
- **Load** the resulting text into files of quotes for each individual book


**Note:**  At present this script is only implemented for OSX, please extend for Linux and Windows by 
adding the default path to "My Clippings.txt".  On OSX this is: /Volumes/Kindle/documents/My Clippings.txt

Usage
-----

1. Plug your Kindle into your computer
2. Download/Clone this directory
3. Install dependencies: `pip install -r requirements.txt`
4. Run `python kindle.py` on the command line 
