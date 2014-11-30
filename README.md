Reddit_Edit_Alert
=================

Reddit_Edit_Alert is a bot that alerts users of [Reddit](reddit.com) in the event that a comment that they had replied
to in the past has since been edited.

However, Reddit does not have an API call for edits as they are made, so instead I had to scrape incoming comments and
check that their parent comment had been edited. Because of this, if a comment hasn't had any responses after being
edited, then the bot will miss it. Unfortunately, short of back-scanning the thousands and thousands of comments that
come in daily, I'm not sure there is a better was of doing this unless Reddit develops an incoming edit API.

This is a bot written in Python using [PRAW (Python Reddit API Wrapper)](praw.readthedocs.org).
