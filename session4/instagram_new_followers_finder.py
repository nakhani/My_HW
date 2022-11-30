import instaloader
import getpass


#read old followers
f = open("follower.txt", "r")
old_followers = []
for line in f :
    old_followers.append(line)
f.close()

#get username and password
L = instaloader.Instaloader()

user_name = input("plaese enter user name:")
password = getpass.getpass("please enter your password:")

#login
L.login(user_name, password)
print("you login seccsessfuly")

#get  new followers
profile = instaloader.profile.from_username(L.context,"n.j.m.e")


new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

#compare  new follower
for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower+"\n")


#save new follower
f = open("follower.txt","w")
for follower in new_followers:
    f.write(follower+"\n")
f.close()