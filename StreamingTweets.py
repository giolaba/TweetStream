from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'FoRKiRVFYdYeR32fJaC8gYH1W'
csecret = 'DaWzsDW41r589T7zm1EYLW06UVY1GPJrVKnNjmWIJOyVMMyNaf'
atoken = '2488593914-1358WsLPzLaizzKFJiExBA0Ainft8J4AYYUxTJ2'
asecret = '246pWuh4542CIF7iNQd5rbuMyTpOlCUuryCVkQffUKR3p'

class listener (StreamListener):
    def on_data(self, data):
            try:
    #            print(data)

                tweetId = data.split(',"id_str":"')[1].split('","text')[0]
                tweet = data.split(',"text":"')[1].split('","source')[0]

                userId = data.split('"user":{"id":')[1].split(',"id_str":"')[0]
                userName = data.split(',"name":"')[1].split('","screen_name')[0]
                usreScName = data.split(',"screen_name":"')[1].split('","location')[0]

                tcTime = data.split('"created_at":"')[1].split('","id')[0]
                tcTimeTuple = time.strptime(tcTime, "%a %b %d %H:%M:%S %z %Y")
                tcTimeEpoch = time.mktime(tcTimeTuple)

                ucTime = data.split(',"created_at":"')[1].split('","utc_offset')[0]
                ucTimeTuple = time.strptime(ucTime,"%a %b %d %H:%M:%S %z %Y")
                ucTimeEpoch = time.mktime(ucTimeTuple)


                saveThis =tweetId+'::'+str(tcTimeEpoch)+'::'+tweet+'::'+userId+'::'+str(ucTimeEpoch)+'::'+userName+'::'+usreScName

                print(saveThis)
                saveFile = open('twitDB.csv', 'a')
                saveFile.write(saveThis)
                saveFile.write('\n')
                saveFile.close()
                return True
            except BaseException:
                print('failed ondata')
                time.sleep(1)

    def on_error(self, status_code):
        print(status_code)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["bieber"])