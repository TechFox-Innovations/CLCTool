# SpoinkCLCT

---

# Spoink - Custom Linux Configuration Tool

## Introduction

Spoink is a custom Linux configuration tool that reads and executes actions specified in a `.spoink` file. It provides a way to automate the installation of packages and the configuration of services on a Linux system.

## Usage

To use Spoink, follow these steps:

1. **Install Dependencies:**

   ```bash
   sudo pip install -r ./requirements.txt --break-system-packages
   ```

3. **Download Spoink Script:**
   Download the `spoink.py` script to your machine.

4. **Create a `.spoink` File:**
   Create a YAML file with the extension `.spoink` to define the packages and services you want to install and enable. Refer to the example below:

   ```yaml
   packages:
     - nginx
     - python3

   services:
     - nginx
   ```

5. **Run Spoink:**
   Open a terminal and run the Spoink script with the following command:

   ```bash
   sudo python spoink.py -i your_file.spoink
   ```

   Replace `your_file.spoink` with the path to your `.spoink` file.

## Command-Line Options

- `-i, --input`: Specify the path to the `.spoink` file to be executed.

## Example

Assuming you have an `.spoink` file named `custom_config.spoink`:

```bash
 sudo python spoink.py -i custom_config.spoink
```

This will read the `custom_config.spoink` file and execute the specified actions.

## Notes

- Spoink uses YAML format for the `.spoink` file. Ensure the file follows proper YAML syntax.

---
