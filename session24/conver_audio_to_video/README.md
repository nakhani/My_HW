# Video to Audio Converter

This folder contains two Python scripts for converting video files to audio files. One script uses multi-threading for concurrent processing, and the other processes files sequentially without multi-threading. The performance comparison shows the difference in conversion times between the two approaches.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Multi-threaded Version](#multi-threaded-version)
  - [Non-threaded Version](#non-threaded-version)
- [Performance Comparison](#performance-comparison)


## Overview

### Multi-threaded Version

This script uses Python's `threading` module to convert video files to audio files concurrently. It significantly reduces the total processing time by leveraging multiple threads.

### Non-threaded Version

This script converts video files to audio files sequentially, processing one file at a time. It does not use any concurrent processing, resulting in longer total processing times.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/video-to-audio-converter.git
   cd video-to-audio-converter

2. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt


## Performance Comparison

The performance of the two scripts was measured by converting five video files to audio files. The results are as follows:

- **Multi-threaded Version**: 3.1 seconds
- **Non-threaded Version**: 4.6 seconds

## Analysis

- The multi-threaded version is significantly faster (approximately 33% reduction in processing time) than the non-threaded version.

- Multi-threading allows multiple files to be processed concurrently, leveraging available CPU cores more effectively and reducing the total processing time.

- The non-threaded version processes files sequentially, resulting in longer total processing times.