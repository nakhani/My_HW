import instaloader
import getpass



f = open("follower.txt", "r")
old_followers = []
for line in f :
    old_followers.append(line)
f.close()

L = instaloader.Instaloader()

user_name = input("plaese enter user name:")
password = getpass.getpass("please enter your password:")


L.login(user_name, password)
print("you login seccsessfuly")


profile = instaloader.profile.from_username(L.context,"n.j.k")


new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)


f = open("follower.txt","w")
for follower in new_followers:
    f.write(follower+"\n")
f.close()