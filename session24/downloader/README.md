# Fast Downloader

Fast Downloader is a Python application that allows users to download files concurrently using threading. It features a PySide6-based GUI with a dark mode theme, enabling users to input multiple URLs, select an output directory, and start the download process with ease.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Concurrent Downloads**: Utilizes threading to download multiple files simultaneously.
- **Dark Mode UI**: Modern dark-themed user interface using PySide6.
- **User-friendly**: Allows users to input URLs, select an output directory, and start the download process with a single click.
- **Error Handling**: Displays error messages for invalid inputs and download failures.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fast-downloader.git
   cd fast-downloader

2. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install the dependencies:
   ```bash
   pip install requests PySide6
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py

2. **Enter the URLs**: In the application window, enter the URLs of the files you wish to download, one per line.

3. **Select Output Directory**: Click on the "Select Output Directory" button to choose where the downloaded files will be saved.

4. **Start Download**: Click on the "Start Download" button to begin downloading the files concurrently.
 





