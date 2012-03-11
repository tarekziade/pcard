from bottle import route, run, request, response
from pcard.gen import create_card, SYMBOLS


_INDEX = """\
<h1>PCard</h1>
<p>Beware that anyone can sniff your secret when you post the form.
You should consider generating the card from your computer.</p>
<form action="/card" method="POST">
     <input type="password" name="key"/>
     <input type="submit">
</form>
<p>How to generate the card on your computer:</p>
<pre>
$ pip install pcard
$ pcard
</pre>
"""

_CSS =  """
<style type="text/css">

td {
 text-align: center;
 vertical-align: middle;
 padding: 1px;
 margin: 0px;
}

div.card {
 background-color: #ECF1EF;
 -moz-border-radius: 15px;
 border-radius: 15px;
 padding: 10px;
 text-align: center;
 vertical-align: middle;
 width: 90mm;
 height: 45mm;
 margin-top: 20px;
}

table {
 border-collapse: collapse;
 font-size: 3mm;
}

pre {
 text-align: left;
 -moz-border-radius: 15px;
 border-radius: 15px;
 padding: 10px;
 background-color: white;
}
</style>
"""

HOW = """\
<p>How to generate this card again:</p>
<pre>
$ pip install pcard
$ pcard
</pre>
Or visit: http://pcard.ziade.org
"""

_COLORS = ['#98F5FF', '#BF3EFF', '#EE3B3B', '#76EE00', 'white',
           '#FFC0CB', '#FF8C00', '#EAEAEA',
           '#98F5FF', '#BF3EFF', '#EE3B3B', '#76EE00', 'white',
     '#98F5FF', '#BF3EFF', '#EE3B3B', '#76EE00', 'white',
           ]


@route('/')
def home():
    response.content_type = 'text/html; charset=utf8'
    return _INDEX


@route('/card', method='POST')
def get_card():
    response.content_type = 'text/html; charset=utf8'
    key = request.forms.key
    __, lines = create_card(key)
    res = [_CSS + '<div class="card"><table><tr><td></td>']

    for symbol in SYMBOLS.split():
        symbol = symbol.strip()
        res.append('<td>%s</td>' % symbol)

    res.append('</tr>')
    for index, line in enumerate(lines):
        res.append('<tr style="background-color:%s">' % _COLORS[index])
        res.append('<td>%d.</td>' % index)
        values = line.split()
        for value in values:
            value = value.strip()
            res.append('<td>%s</td>' % value)

        res.append('</tr>')

    res.append('<tr></tr></table></div>')
    res.append('<div class="card"><h4>PCard</h4>%s</div>' % HOW)
    return '\n'.join(res)


if __name__ == '__main__':
    run(host='localhost', port=8080)
