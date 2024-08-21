import scrapetube

inputChannel = input('Input your channel ID:\n')
videos = scrapetube.get_channel(inputChannel)

f = open('urls.csv', 'w', encoding="utf-8")
urls = []

for video in videos:
    urls.append('`'+str(video['videoId'])+'`'+","+'`'+str(video['title']['runs'][0]['text'])+'`\n' )

    currLen = len(urls)
    if (currLen % 100) == 0:
        print(str(currLen) + " videos added to urls array.\n")


print("Finished.\nFinal length of URLS: " + str(len(urls))+"\n")

f.writelines(urls)
f.close()