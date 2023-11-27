# PDF to TIFF Converter

## Tool to convert PDF files to TIFF format with customizable DPI settings, making it ideal for journal figure submissions.

### Installation
You'll need Python installed on your system and some dependencies to run this script.
First, clone this repository.
Then, navigate to the directory containing the script.
Install the required dependencies with:
```
pip install -r requirements.txt
```
### Usage
To use this tool, follow these simple steps:

Run the script with the command:
```
python pdf_to_tiff_converter.py --folder_path "path/to/your/pdf/folder" [--dpi your_dpi_value]
```
Replace "path/to/your/pdf/folder" with the path to your folder containing PDF files.

Optionally, you can specify the DPI with --dpi your_dpi_value. The default is 400 (standard for most journals).

### Output
The converted TIFF files will be saved in a new folder within the specified directory, named with the timestamp of the conversion run.
