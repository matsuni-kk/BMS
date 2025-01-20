# URL to Markdown Converter

This tool converts a given URL to a Markdown file using the `ToMarkdownLoader` from the `langchain-community` library.

## Installation

1. Install the required library:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `url_to_markdown.py` script and provide the URL you want to convert as an argument.

```bash
python url_to_markdown.py --url <your_url>
```

Replace `<your_url>` with the URL you want to convert.

2. The converted Markdown content will be printed to the console.

## Testing

To run the tests, use the following command:

```bash
pytest
```

## Notes

- The tool uses the `ToMarkdownLoader` which may produce different results depending on the structure of the web page.
- Make sure to set appropriate parameters when using asynchronous or chunking features.