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
            print(data)

            tweetid = data.split(',"id_str":"')[1].split('","text')[0]
            tweet = data.split(',"text":"')[1].split('","source')[0]
            userid = data.split('"user":{"id":')[1].split(',"id_str":"')[0]
            username = data.split(',"name":"')[1].split('","screen_name')[0]
            usrescname = data.split(',"screen_name":"')[1].split('","location')[0]
            tctime = data.split('"created_at":"')[1].split('","id')[0]
            tm = time.strptime("30 Nov 00", "%d %b %y")

            saveThis = tctime+'::'+tm#str(time.time())+'::'+str(time.localtime())#tweetid+'::'+userid+'::'+username+'::'+usrescname+'::'+str(time.localtime())
#+'::'+tweet
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