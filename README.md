# delete-google-photos
Delete all your Google Photos automatically.

This is a quick-and-dirty Python 3 script which tries its best to delete all your Google Photos automatically.

## Requirements

* Firefox (or another browser supported by Selenium)
* Selenium
* Selenium Python bindings. Run `pip install -r requirements.txt`

## Usage

* Adjust config.py with your Google account credentials
* run `python3 delete_google_photos.py`
* wait and refresh the browser window if stuck (I know…)

This script never finishes, so you have to check for yourself if there are still photos left to delete.