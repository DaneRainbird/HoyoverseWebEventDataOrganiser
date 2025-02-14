# Hoyoverse Web Event Data Organiser

A helper tool to organise the extracted assets from my [Hoyoverse Web Event Data Scraper](https://github.com/DaneRainbird/HoyoverseWebEventDataScraper).

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/DaneRainbird/HoyoverseWebEventDataOrganiser.git
    cd HoyoverseWebEventDataOrganiser
    ```

2. Run the script with Python3, and pass the full directory using the --path argument:
    ```sh
    python3 main.py --path /path/to/downloaded/folder
    ```

## What can I do with the extracted data?

Once this script has run, you will have a new folder called `sorted` in the same directory as the original folder. This folder will contain the following structure:

```
sorted
├── name
│   ├── name.png
│   ├── name.atlas
│   ├── name.json
...
```

There will also still be the `other_resources` folder, which contains anything that isn't immediately linkable to the atlas and json files.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Contributing

The format of these web events often changes, especially between games. This tool has been tested with Genshin Impact, Zenless Zone Zero, and Honkai Star Rail events, but I can't garuantee it will work with future events. If you find an event that doesn't work, please open an issue or submit a pull request.

## Acknowledgements

- Content created and owned by HoyoLAB, miHoYo Co., Ltd., and its licensors.