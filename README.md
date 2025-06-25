# reddit-auto-poster
schedules posts for reddit automatically, so you can get them at the perfect time 

# Dependancies 
1. praw
2. dotenv (not needed per se, but super useful)
3. apscheduler

# App Link 
Use this jawn to actually set up your app https://old.reddit.com/prefs/apps

# Local files 
## Reddit posts/times
example_subreddit_times is an example of format you want for the file. You want your own copy in the root directory BITCH

# Dealing with virtual environments
# 1. Install Python if you haven't already
sudo pacman -S python

# 2. Create a new folder for your project (optional)
mkdir myproject
cd myproject

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
source venv/bin/activate

# 5. Install the package via pip
pip install <package-name>

# 6. Confirm installation
pip list
Once you're done working:

bash
Copy
Edit
# Deactivate the virtual environment
deactivate