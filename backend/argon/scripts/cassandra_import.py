from csv import reader
from datetime import datetime
from sys import argv
from uuid import uuid4

from cassandra.cluster import Cluster


if __name__ == '__main__':
    file = argv[1]

    cluster = Cluster()
    session = cluster.connect('development')

    with open(file, encoding='utf8') as f:
        r = reader(f, delimiter='\t')
        for index, row in enumerate(r):
            if len(row) is 4:
                userid, tweetid, tweet, date = row
                userid = int(userid.replace('\ufeff', ''))
                tweetid = int(tweetid.replace('\ufeff', ''))
                date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                session.execute(
                    """
                    INSERT INTO tweets (id, tweet_user_id, tweet_id, tweet_text, timestamp)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (uuid4(), userid, tweetid, tweet, date)
                )
                print(f'Inserted {index} tweets')
