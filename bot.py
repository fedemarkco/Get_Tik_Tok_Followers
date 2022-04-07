import requests
import time
import sys


def getUserId(username, key):
  url = "https://scraptik.p.rapidapi.com/get-user"

  querystring = {"username": username}

  headers = {
      'x-rapidapi-host': "scraptik.p.rapidapi.com",
      'x-rapidapi-key': key
      }

  response = requests.get(url, headers = headers, params = querystring)

  try:
    return response.json()["user"]["uid"]
  except:
    return "error"

def getFollowers(userId, key):
  users = []
  minTime = 0

  while minTime != -1:
    try:
      url = "https://scraptik.p.rapidapi.com/list-followers"
      querystring = {"user_id": str(userId), "count": "200", "max_time": str(minTime)}

      headers = {
          'x-rapidapi-host': "scraptik.p.rapidapi.com",
          'x-rapidapi-key': "d0dbab0bd4mshf5a5d7bcc21586dp11cff1jsnee1d1f72792c"
          }

      response = requests.get(url, headers = headers, params = querystring)
      _json = response.json()["followers"]
      minTime = response.json()["min_time"]

      for j in _json:
        users.append(j["unique_id"])

      sys.stdout.write("\rFollowers " + str(len(users)))
      sys.stdout.flush()
      time.sleep(1)
    except:
      time.sleep(1)

  return users


if __name__ == "__main__":
  rapidapiKey = key
  print("Enter the username: ", end = "")

  username = input()
  userId = getUserId(username, key)

  if userId == "error":
    print("Username does not exist")
  else:
    users = getFollowers(userId, key)

    if len(users) > 0:
      print("\n")
      for user in users:
        print("@" + user)
