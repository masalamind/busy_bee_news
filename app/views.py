from flask import render_template
from newsapi import NewsApiClient
from app import app

@app.route("/")
@app.route("/home")
def home():
    newsapi = NewsApiClient(api_key='4c9546d6e1fb4b03a2ff8273c06023ac')
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(6):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(news, desc, img)
    return render_template('home.html', context = mylist)


if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/al-jazeera")
# @app.route("/aljazeera")
# def aljazeera():
#     newsapi = NewsApiClient(api_key='4c9546d6e1fb4b03a2ff8273c06023ac')
#     topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')
#
#     articles = topheadlines['articles']
#
#     desc = []
#     news = []
#     img = []
#
#     for i in range(len(articles)):
#         myarticles = [articles[i]]
#         news.append(myarticles["title"])
#         desc.append(myarticles["description"])
#         img.append(myarticles["urlToImage"])
#
#     mylist = zip(news, desc, img)
#     return render_template('aljazeera.html', context= mylist)