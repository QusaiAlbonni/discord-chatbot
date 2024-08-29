# Simple Discord Bot using Gemini and Peewee
<hr/><br/> 

#### No premium price needed conversations are stored locally on an SQLite database <br>

### Features:
- Locally stored Channel histories on an SQLite database.
- Uses peewee ORM for easily extensible DB.

### Usage example:
- first get your discord application configured and get the key for the bot
- generate a google AI key (note that the free tier only works in the USA)
- make sure you have python installed
```sh
python --version
# on linux
python3 -version
```
- run the following to ensure you have all dependencies
```sh
pip install -r requirements.txt
```
and run the main.py file and chat with your bot!

### Important Note:
storing users data without their consent is generally prohibited by discord,<br/>
so make sure you add a consent or terms of use agreement before storing any data <br/>
you also need to adhere to local data protection laws.