import praw
import time

username = "user"
password = "pass"
body = "This is just an alert that a comment that you previously responded to has been edited.\n\n" \
       "^(This [bot](https://github.com/Bluesroo/Reddit_Edit_Alert) was made by /u/Bluesroo." \
       " Message him with any problems you have.)"


class CommentChecker(object):
    """ A comment from the Reddit comment stream.
    """

    def __init__(self, comment):
        self.comment = comment
        self.parent = comment

    def set_parent(self, r):
        url = self.comment.permalink
        parent_id = self.comment.parent_id.partition('_')
        if parent_id[0] == 't3':
            self.parent = None
            return False
        submission = r.get_submission(url + parent_id[2])
        self.parent = submission.comments[0]
        return True

    def alert_children(self):
        children = self.parent.replies
        for child in children:
            try:
                if child.author != username:
                    if child.author != self.parent.author:
                        print("\tto " + str(child.name))
                        #child.reply(body)
            except AttributeError:
                children = child.comments


def main():
    r = praw.Reddit("Edit alert bot by /u/Bluesroo")
    print("Logging in...")
    r.login(username, password)
    checked_list = []
    edited_list = []

    while True:
        print("\nGetting more comments...\n")
        comments = praw.helpers.comment_stream(r, 'all', limit=500)
        for comment in comments:
            if comment.id not in checked_list:
                responder = CommentChecker(comment)
                if responder.set_parent(r):
                    if responder.parent.name not in edited_list:
                        if responder.parent.edited:
                            print("Responding...")
                            responder.alert_children()
                        edited_list.append(responder.parent.id)
            checked_list.append(comment.id)

if __name__ == "__main__":
    main()