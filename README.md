 ``` 
  _   _ ____  ____     _     _ 
 | | | / ___||  _ \   | |   | |
 | | | \___ \| |_) |  | |_  | |
 | |_| |___) |  __/ |_| | |_| |
  \___/|____/|_|   \___/ \___/ 
```                               

# USPJJ – UpSet Plot Generator

USPJJ is a lightweight tool designed to generate **UpSet plots** from Excel datasets containing binary (0/1) values. It provides a simple interface for visualizing how different combinations of attributes appear across your data.

The tool is intended for both technical and non-technical users and is available as a standalone Windows executable as well as a Python script.

---

## Features

- Accepts Excel files (`.xlsx` or `.xls`) **with binary data**  
- Supports filtering on `0` or `1` values  
- Automatically drops the first column (e.g. client IDs or names)  
- Generates high-resolution PNG images  
- Windows-compatible standalone executable (`.exe`)  
- CLI script available for Python environments  

---

## Input File Requirements

Before running the tool, make sure your Excel file follows this structure:

- The first row must contain column headers  
- The first column will be dropped automatically (e.g. client names or IDs)  
  - Ensure it does not contain meaningful data used in grouping  
- All other columns must contain only `0` or `1` values  

### Important

Make sure the Excel file is **closed** before running the tool.  
If the file is open (for example in Excel or OneDrive preview), the program may fail with a permission error.

---

## Output

During execution, the tool will prompt you to choose whether the combinations should be generated based on:

- `1` values (matching criteria), or  
- `0` values (not matching criteria)

The resulting UpSet plot will be saved as *UpSet_plot.png* in the same folder as your input Excel file.

---

## Usage

### Standalone Executable (Windows)

1. Double-click the `.exe` file  
2. Read the instructions and click **OK**  
3. Select your Excel file  
4. Choose whether to group by `0` or `1` values  
5. The plot will be generated automatically  

No Python installation is required.

---

### Python Script

If you prefer running the script directly:

```
python UpSetPlot.py
```
#### Requirements (for script version)

- Python 3.11+
- Required libraries:
  - matplotlib
  - pandas
  - upsetplot
  - openpyxl

Install dependencies with:
```
pip install matplotlib pandas upsetplot openpyxl
```

## Typical Use Cases

- Visualizing overlaps between system flags or configuration states
- Analyzing feature combinations in datasets
- Auditing compliance indicators
- Exploring logical dependencies between attributes

## Project Status
- Stable — actively used in production environments.
- Future improvements may include:
  - macOS build
  - CSV file support
  - Drag & drop input

## Support

If you encounter issues or have suggestions, please open an issue in the GitHub repository.

## License

This project is released under the MIT License.
