import praw
import time

username = "blah"
password = "blah"
body = "This is just an alert that a comment that you previously responded to has been edited.\n\n" \
       "^(This [bot](https://github.com/Bluesroo/Reddit_Edit_Alert) was made by /u/Bluesroo." \
       " Message him with any problems you have.)"


class CommentChecker(object):
    """ A comment from the Reddit comment stream.
    """

    def __init__(self, comment):
        self.comment = comment
        self.checked_list = []
        self.edited_list = []

    def get_parent(self, r, child):
        url = child.link_url
        parent_id = child.parent_id.partition('_')
        submission = r.get_submission(url + parent_id[2])
        parent = submission.comments[0]
        return parent

    def alert_children(self, parent):
        children = parent.replies
        for child in children:
            if child.author != 'user_battle_bot':
                if child.author != parent.author:
                    child.reply(body)
        return

def main():
    r = praw.Reddit("Edit alert bot by /u/Bluesroo")
    print("Logging in...")
    r.login(username, password)

    while True:
        print("Getting fresh comments...")
        comments = r.get_comments('all')
        for comment in comments:
            checker = CommentChecker(comment)
            print(checker.comment.author)
            if comment.id not in checked_list:
                parent_comment = get_parent(r, comment)
                if parent_comment.name not in edited_list:
                    if parent_comment.edited:
                        print("Alerting children...")
                        alert_children(parent_comment)
                edited_list.append(parent_comment.id)
            checked_list.append(comment.id)
        print("Sleeping...")
        time.sleep(30)

if __name__ == "__main__":
    main()