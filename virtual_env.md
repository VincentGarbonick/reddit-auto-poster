## Dealing with virtual environments
### 1. Install Python if you haven't already
sudo pacman -S python

### 2. Create a new folder for your project (optional)
mkdir myproject
cd myproject

### 3. Create a virtual environment
python -m venv venv

### 4. Activate the virtual environment
source venv/bin/activate

### 5. Install the package via pip
pip install <package-name>

### 6. Confirm installation
pip list

### Deactivate the virtual environment
deactivate