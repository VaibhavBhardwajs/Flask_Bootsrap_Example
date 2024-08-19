#import
from flask import Flask,render_template,request
import requests
from config import NEWS_API_KEY

#Create a flask app
app=Flask(__name__)


@app.route("/")
def index():
    query=request.args.get("query","latest")
    url=f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    resposnce=requests.get(url)
    news_data=resposnce.json()
    articles=news_data.get('articles',[])

    filterd_articles=[article for article in articles if "removed" not in article['title'].lower() and "Yahoo" not in article["source"]["name"] ]

    return render_template("index.html",articles=filterd_articles,query=query)










if __name__ == "__main__":
    app.run(debug=True)