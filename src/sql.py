from peewee import Model, SqliteDatabase, IntegerField, CharField, TextField

# Initialize SQLite database using Peewee
db = SqliteDatabase('conversation_history.db')


class Conversation(Model):
    user_id = IntegerField()
    channel_id = IntegerField()
    user_name = CharField(max_length=100)
    message_id = IntegerField()
    role = CharField(max_length=100)
    message_content = TextField()

    class Meta:
        database = db
        indexes = (
            (('user_id', 'channel_id'), False),
        )


def create_tables():
    db.connect()
    db.create_tables([Conversation], safe=True)


