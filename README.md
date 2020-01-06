# QuineTwt

QuineTwt is a Twitter Quine, a program that tweets itself. Here's the code for it:

```
#@quinetwt
import twitter as T;x='chr(35)+"@quinetwt"+chr(10)+"import twitter as T;x="+chr(39)+x+chr(39)+";T.Api("+chr(42)+").PostUpdate("+x+")"';T.Api(*).PostUpdate(chr(35)+"@quinetwt"+chr(10)+"import twitter as T;x="+chr(39)+x+chr(39)+";T.Api("+chr(42)+").PostUpdate("+x+")")
```

If you run it, it'll tweet to your account. To get it to work you'll need to replace the * with your developer access tokens. Don't worry, these won't get tweeted.

If you know python this should all be straightforward, otherwise follow the instructions below.

## Instructions

To execute the quine you'll need to have a Twitter developer account. If you don't already have one, you can create one by going to developer.twitter.com and filling out the (unfortunately now quite lengthy but otherwise straightforward) application form.

Once you have an account, select _Apps_ followed by _Create an app_. There you'll be able to fill out yet more formage, after all of which you'll end up with your Consumer API keys and your access tokens. When you're filling out the form be sure to give the quine write access.

Now replace the * in the `quine.py` file with your keys, separated by commas, in this order: `consumer_key, consumer_secret, access_token_key, access_token_secret`. The end result will look something like this, but with your own much longer keys:

```
...T.Api('Y6F675','78HF4F','8UFGE4','12F4A0')...
```

Save the file and now you're ready to execute it.

It's easiest to execute it in a virtual environment. Here's a brief overview of how I'd go about doing that:

```
# Set up your virtual environment
mkdir venv
cd venv
virtualenv .
source ./bin/activate
pip install python-twitter

# Execute your quine
python ../quine.py

# Deactivate and delete the virtual environment
deactivate
cd ..
rm -rf venv
```

## The quine_reply bot

This listens for mentions of the quine reproducing itself and posts a reply whenver it does. To run the code you'll need another set of twitter access keys/tokens. Add them to a file called `quine_reply.config` in json format like this:

```
{
	"api_key": "",
	"api_secret_key": "",
	"access_token": "",
	"access_token_secret": ""
}
```

The code will run, check for mentions and then quick, so it can be run periodically as a cron job. It will create two other files: `quine_reply.log` and `quine_reply.cache`. Hopefully the former is self explanatory. The latter keeps track of the last mention it dealt with, so that it doesn't post replies to the same mention multiple times.

## More info

The QuineTwt info page: http://www.flypig.co.uk?to=quinetwt

The @QuineTwt reply_bot: https://twitter.com/quinetwt

