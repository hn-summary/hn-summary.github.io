I want to change my habit of browsing HN all the time, but still don't want to miss important news or events. So, I decided to create this simple static site with summaries and aggregations of all the most popular Stories, Ask HN, Show HN and other categorized posts (News, Dev Blogs, Scientific Publications, etc).

### Where does the data come from?

I built [a quick wrapper around Algolia's API](https://github.com/santiagobasulto/python-hacker-news) and I use it to dump a huge CSV of all the HN posts every week. The source dataset is [hosted on Kaggle](https://www.kaggle.com/santiagobasulto/all-hacker-news-posts-stories-askshow-hn-polls).

### Custom groups of posts

I've grouped posts from specific domains in a very arbitrary way. You can check (and collaborate) the groups in `domain_groups.json`. Open an issue if you consider one domain should be added/moved.

### Building and dev

I haven't done much to document this properly. I'm using Jupyter Notebooks for the build process (something that I'll probably need to change to automate it weekly). The only requirements are `pandas`, `jinja2` and the datasource mentioned above.
