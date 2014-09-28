"""
A script that scans incoming comments of Reddit for edited comments. It then responds to the children,
alerting them of the edit.
"""

import praw

username = "user"
password = "pass"
body = "This is just an alert that a comment that you previously responded to has been edited.\n\n" \
       "^(This [bot](https://github.com/Bluesroo/Reddit_Edit_Alert) was made by /u/Bluesroo." \
       " Message him with any problems you have.)"


class CommentChecker(object):

    """ A comment from the Reddit comment stream. """

    def __init__(self, comment):
        self.comment = comment
        self.parent = comment

    def set_parent(self, r):
        """ Finds the parent to the current comment.

        :returns: Bool, whether is was successful in finding a parent.

        """

        url = self.comment.permalink
        parent_id = self.comment.parent_id.partition('_')
        if parent_id[0] == 't3':
            self.parent = None
            return False
        submission = r.get_submission(url + parent_id[2])
        self.parent = submission.comments[0]
        return True

    def child_before_edit(self, child):
        """
        :returns: Bool, whether a child comment was posted before or after the parent was edited.
        """
        if self.parent.edited > child.created:
            return True
        return False

    def alert_children(self):
        """ Alerts each of the child comments of an edited parent.

        """
        children = self.parent.replies
        for child in children:
            try:
                if self.child_before_edit(child):
                    if child.author != username:
                        if child.author != self.parent.author:
                            child.reply(body)
            except AttributeError:
                children = child.comments


def main():
    """ Main entry point for the program

    """
    r = praw.Reddit("Edit alert bot by /u/Bluesroo")
    print("Logging in...")
    r.login(username, password)
    checked_list = []
    edited_list = []

    print("\nGetting more comments...\n")
    comments = praw.helpers.comment_stream(r, 'all', limit=5)
    for comment in comments:
        if comment.id not in checked_list and not comment.is_root:
            responder = CommentChecker(comment)
            if responder.set_parent(r) and responder.parent.name not in edited_list:
                if responder.parent.edited:
                    responder.alert_children()
                edited_list.append(responder.parent.id)
        checked_list.append(comment.id)

if __name__ == "__main__":
    main()