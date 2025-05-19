from flask import Flask, request, jsonify, render_template
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/search')
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": 'Query parameter "query" is required'})

    try:
        flipkart_url = f"https://www.flipkart.com/search?q={query}"
        urlclient = urlopen(flipkart_url)
        flipkart_page = urlclient.read()
        flipkart_html = bs(flipkart_page, 'html.parser')

        bigbox = flipkart_html.findAll("div", {"class": "cPHDOP col-12-12"})
        if len(bigbox) <= 3:
            return jsonify({'error': 'No product listings found'}), 404

        del bigbox[0:3]
        product_link = "https://www.flipkart.com" + bigbox[1].div.div.div.a["href"]

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        product_req = requests.get(product_link, headers=headers)
        product_html = bs(product_req.text, 'html.parser')
        comment_box = product_html.find_all("div", {"class": "_8-rIO3"})

        if not comment_box or len(comment_box) < 2:
            return jsonify({'error': 'No reviews found'}), 404

        review_section = comment_box[1]  # Usually this section contains actual user reviews

        names = [i.text for i in review_section.find_all("p", {"class": "_2NsDsF AwS1CA"})]
        ratings = [i.text for i in review_section.find_all("div", {"class": "XQDdHH"})]
        reviews = [i.text for i in review_section.find_all("p", {"class": "z9E0IG"})]

        return render_template(
            'results.html',
            query=query,
            product_link=product_link,
            names=names,
            ratings=ratings,
            reviews=reviews,
            zip=zip
        )

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
