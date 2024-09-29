#**Developer:** @Gh0stDeveloper
#**Channel:** @TEAM_CHICO_CP

import json
import os
import random
from instabot import Bot

json_file_path = "instagram_users.json"
comments_file_path = "comments.json"

def create_example_json():
    example_data = {
        "users": [
            {"username": "example_user1", "password": "example_password1"},
            {"username": "example_user2", "password": "example_password2"}
        ]
    }
    with open(json_file_path, 'w') as json_file:
        json.dump(example_data, json_file, indent=4)
    print(f"Archivo {json_file_path} creado con ejemplos. Por favor, rellénalo con los datos de los usuarios.")

def create_comments_json():
    example_comments = {
        "comments": [
            "Great post!",
            "You're the best!",
            "Keep it up!"
        ]
    }
    with open(comments_file_path, 'w') as json_file:
        json.dump(example_comments, json_file, indent=4)
    print(f"Archivo {comments_file_path} creado con ejemplos. Por favor, rellénalo con más comentarios si lo deseas.")

def read_users_from_json():
    if not os.path.exists(json_file_path):
        create_example_json()
        return []

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get("users", [])

def read_comments_from_json():
    if not os.path.exists(comments_file_path):
        create_comments_json()
        return []

    with open(comments_file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get("comments", [])

def login_and_interact(username, password, username_to_search):
    bot = Bot()
    bot.login(username=username, password=password)
    
    user_id = bot.get_user_id_from_username(username_to_search)
    bot.follow(user_id)
    print(f"Followed user: {username_to_search}")

    media_ids = bot.get_user_medias(user_id, filtration=True)
    if not media_ids:
        print("The user has no posts.")
        return

    comments = read_comments_from_json()
    if not comments:
        print("The comments file is empty. Please fill it with more comments.")
        return

    for media_id in media_ids:
        bot.like(media_id)
        print("Liked the post")

        random_comment = random.choice(comments)
        bot.comment(media_id, random_comment)
        print(f"Commented: {random_comment}")

def main():
    if not os.path.exists(json_file_path):
        create_example_json()
    if not os.path.exists(comments_file_path):
        create_comments_json()

    users = read_users_from_json()
    if not users:
        print("The users JSON file is empty. Please fill it with user data.")
        return

    username_to_search = input("Enter the username to search: ").strip()
    for user in users:
        login_and_interact(user["username"], user["password"], username_to_search)

if __name__ == "__main__":
    main()