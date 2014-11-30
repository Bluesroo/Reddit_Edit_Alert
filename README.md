Reddit_Edit_Alert
=================

Reddit_Edit_Alert is a bot that alerts users of [Reddit](http://www.reddit.com) in the event that a comment that they had replied
to in the past has since been edited.

However, Reddit does not have an API call for edits as they are made, so instead I had to scrape incoming comments and
check that their parent comment had been edited. Because of this, if a comment hasn't had any responses since being
edited, thenthe bot will miss it. Unfortunately, short of back-scanning the thousands and thousands of comments that
come in daily, I'm not sure there is a better way of doing this. And even if you decided to backscan comments, it would
be almost impossible to do it in a reasonable amount of time due to Reddit's API call [rate limit](http://www.github.com/reddit/reddit/wiki/API#rules). Unless Reddit develops
an incoming edit API call, I'm not sure there will ever be a perfect system for this.

This is a bot written in Python using [PRAW (Python Reddit API Wrapper)](http://www.praw.readthedocs.org).
