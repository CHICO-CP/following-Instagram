# Instagram Automation Script

This Python script automates interactions on Instagram. It allows you to log in with multiple accounts, follow users, like their posts, and leave comments automatically.

## Features

- Log in to Instagram with multiple accounts.
- Search for users by username.
- Automatically follow users.
- Like and comment on their posts.

## Requirements

- Python 3.x
- [Instabot](https://github.com/instaloader/instaloader) library

You can install Instabot using pip:

```bash
pip install instabot
```
# Setup

1. Clone this repository:
```bash
git clone https://github.com/CHICO-CP/following-Instagram.git
```
Replace your_username with your actual GitHub username.


2. Create two JSON files for user credentials and comments:

instagram_users.json: This file should contain a list of users with their usernames and passwords in the following format:

```bash
{
  "users": [
    {"username": "your_username1", "password": "your_password1"},
    {"username": "your_username2", "password": "your_password2"}
  ]
}
```
comments.json: This file should contain a list of comments in the following format:

```bash
{
  "comments": [
    "Great post!",
    "You're the best!",
    "Keep it up!"
  ]
}
```

The script will create these files automatically if they do not exist.

Usage

Run the script using Python:
```bash
python following-Instagram.py
```
You will be prompted to enter the username of the user you want to interact with.

# Disclaimer

Use this script responsibly and ensure you comply with Instagram's terms of service. Automated actions can lead to account restrictions or bans if misused.

# Developer

**Developer:** @Gh0stDeveloper
**Channel:** @TEAM_CHICO_CP
