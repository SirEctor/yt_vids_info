# from pyyoutube import Client
import googleapiclient.discovery
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

#https://accounts.google.com/o/oauth2/auth?client_id={client_id}&response_type=token&redirect_uri={redirect_uri}&scope={scope}
#http://localhost:8080/flowName=GeneralOAuthFlow 

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# given_key = input("Enter your YT API Key.\n")

# client = Client(api_key=given_key)

# cId = input("Enter the channel's id.\n")

accessToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
f = open('urls.csv', 'r', encoding="utf-8")

api_service_name = 'youtube'
api_version = 'v3'

#https://console.cloud.google.com/apis/credentials

# flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#         "client_secrets1.json", scopes)
#credentials = flow.run_local_server()
creds = Credentials(accessToken)

youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=creds)

g = open('fileNames.csv', 'w', encoding="utf-8")

fileNameLines = []

for line in f:
        actualLine = line[:-1]
        splitLines = [x[1:-1] for x in actualLine.split(",")]
        currVideoID = splitLines[0]
        currTitle = splitLines[1]
        print(splitLines)    
        # channels_list = client.videos.list(video_id=currVideoID).to_dict()

        request = youtube.videos().list(part="fileDetails", id=currVideoID)
        response = request.execute()

        fileDetails = response['items'][0]['fileDetails']['fileName']

        fileNameLines.append(actualLine + "," + "`"+ fileDetails + "`" +"\n")

        currLen = len(fileNameLines)
        if (currLen % 100) == 0:
                print(str(currLen) + " videos added to fileNameLines array.\n")

print("Finished.\nFinal length of URLS: " + str(len(fileNameLines))+"\n")

f.close()

g.writelines(fileNameLines)
g.close()