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
#        try:
#            print(data)

            tweet = data.split(',"text":"')[1].split('","source')[0]
            saveThis = str(time.time())+'::'+tweet

            print(saveThis)
#            saveFile = open('twitDB.csv', 'a')
#            saveFile.writable(data)
#            saveFile.write('\n')
#            saveFile.close()
            return True
##        except BaseException:
##            print('failed ondata,',str())
##           time.sleep(1)

    def on_error(self, status_code):
        print(status_code)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["bieber"])