from flask import Flask, request, render_template
from main import get_article, get_links, get_links_urls, get_single_url

appy= Flask(__name__)

@appy.route('/', methods=['GET', 'POST'])
def appyhome():
    if request.method == 'POST':
        name = request.form['article']
        name_url = get_single_url(name)
        mush = sorted(get_links(get_article(name)))
        mush_urls = get_links_urls(mush)
        return render_template('wikimushdisplay.html', name=name, name_url=name_url, mush=mush, mush_urls=mush_urls)
    elif request.method == "GET":
        return render_template('postiiiing.html') 

if __name__ == '__main__':
    appy.run(debug=True)