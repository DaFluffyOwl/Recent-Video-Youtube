import json #Import dependencies
import requests
import os
api_key = '' #INSERT YOUR API KEY HERE!!!
def look_for_new_video():
    base_video_url = 'https://youtube.com/watch?v=' #Used to look up video
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?' #Used to search the video on a channel with the API
    params = {'part':'snippet', 'key': api_key, 'order': 'date', 'channelId': channel_name, 'maxResults': 1} #Creates the params for the API link
    response = requests.Session().get(base_search_url, params=params) #Gets a response code
    if response.status_code != 200: #Checks if code is not 200
        print("Error Code:{}".format(response.status_code))#Prints the status code if there is an error
    else:
        pass
    jresponse = json.loads(response.content) #Parses the JSON file from API
    try:
        for i in jresponse['items']: #Looks for all the elements in ['list'] and gets specific elements ['videoId'] and ['channelTitle'] and more
            global videoid #Sets some global variables
            global channel
            global title
            videoid = i['id']['videoId'] #Scans for specific elements and sets them to a variable
            channel = i['snippet']['channelTitle']
            title = i['snippet']['title']
        print(channel+": {}".format(title).replace('&quot;', '\"').replace('&#39;', '\'')) #Prints the channels name as well as the title
        print(base_video_url + videoid+"\n") #Prints the youtube link
    except:
        print(jresponse['error']['message']) #Extra Error Handling
with open('Channels.txt') as fp: #Opens the 'Channels' text file and reads each line 1 by one and runs the look_for_new_video function for each line
    line = fp.readline()
    while line:
        channel_name = line.strip()
        line = fp.readline()
        look_for_new_video()
fp.close() #Closes 'Channels' text file
os.system('pause') #(For cmd) makes it so that it does not close cmd when code is finished
