## Installation guide for `normcap` and Dependencies on Kali Linux

### 1. Install normcap using pip:

 Open a terminal in Kali Linux and run the following command to install normcap:

* `pip install normcap`

This command will download and install `normcap` along with most of it's dependencies.

### 2. Install missing system dependencies:

After installing `normcap`, you may encounter errors related to missing system dependencies such as Qt platform plugins and Tesseract. To resolve these issues, you need to install the required system packages.

#### a. Install libxcb1 and libxcb-cursor0:

Run the following command to install `libxcb1` and `libxcb-cursor0`:

* `sudo apt update`
* `sudo apt install libxcb1 libxcb-cursor`

These packages provide necessary dependencies for Qt platform plugins.

#### b. Install Tesseract OCR:

Tesseract OCR is required for text recognition in `normcap`. Install it using the following command:

* `sudo apt install tesseract-ocr`

### 3. Update PATH environment variable:

To ensure that Tesseract binaries are accessible to normcap, you need to add their directory to the PATH environment variable.

#### a. Open ~/.zshrc file:

Use a text editor (vim, nano, etc...) to open the `~/.zshrc` file:
* `vim ~/.zshrc`

#### b. Add Tesseract binary directory to PATH:

Add the following line at the end of the file:

    export PATH="$PATH:/usr/bin"

#### c. Save and reload the configuration:

Save the changes and exit the text editor. Then, reload the shell configuration:
* `source ~/.zshrc`

### 4. Run normcap:

After completing the above steps, try running normcap:
*`normcap`
