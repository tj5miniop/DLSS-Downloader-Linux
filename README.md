# DLSS Downloader for Linux

A simple tool to download a specific version of NVIDIA's DLSS utility to a directory of your choice.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Versions](#supported-versions)
- [Contributing](#contributing)
- [License](#license)

## Features

- Download specific versions of the DLSS utility.
- Simple command-line interface.
- Supports downloading to any specified directory.

## Prerequisites

- Linux (Obviously)
- DLSS Compatible GPU (All this does is change the version of DLSS a game uses)

## Installation

#Method 1 - Run directly from a local github repo - 
1. Clone the repository:
   ```bash
   git clone https://github.com/tj5miniop/DLSS-Downloader-Linux.git
   cd DLSS-Downloader-Linux
   ```

2. Make the script executable:
   ```bash
   chmod +x dlss_downloader.sh
   ```

# Method 2 - RECCOMENDED FOR ARCH/ARCH-BASED DISTROS ONLY! - Build/Download prebuilt package

1. Download the latest release from the releases page of the repo
2. Simply install the package with pacman -
   ```bash
   sudo pacman -U ./dlss_downloader-*.pkg.tar.zst
   ```

## Usage

To download a specific version of the DLSS utility, run the script with the desired version and target directory:

```bash
./dlss_downloader.sh <version> <target_directory>
```
## Supported Versions

Theoretically, Any Version of DLSS should work, but I only reccomend using versions higher/identical to the one that the game ships with in an attempt to avoid any gamebreaking errors.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request. Ensure to follow the coding standards and include tests for new features.

## License

This project is licensed under the GNU GPL v3 License. See the [LICENSE](LICENSE) file for details.


