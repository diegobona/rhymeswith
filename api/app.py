
from flask import Flask, request, jsonify,send_from_directory,render_template
from Phyme import Phyme

app = Flask(__name__)
ph = Phyme()


@app.route('/')
def home():
    #return send_from_directory('static', 'index.html')
    return render_template('index.html')



@app.route('api/rhymes', methods=['POST'])
def get_rhymes():
    data=request.json
    print(data)
    word=data['word']
    # word = request.json.get('word')
    rhymes = ph.get_perfect_rhymes(word)
    return jsonify(rhymes)

@app.route('/api/rhymes_family', methods=['POST'])
def get_rhymes_family():
    data=request.json
    print(data)
    word=data['word']
    rhymes = ph.get_family_rhymes(word)
    return jsonify(rhymes)

@app.route('/api/rhymes_partner', methods=['POST'])
def get_rhymes_partner():
    data=request.json
    print(data)
    word=data['word']
    rhymes = ph.get_partner_rhymes(word)
    return jsonify(rhymes)

@app.route('/api/rhymes_additive', methods=['POST'])
def get_rhymes_additive():
    data=request.json
    print(data)
    word=data['word']
    rhymes = ph.get_additive_rhymes(word)
    return jsonify(rhymes)

@app.route('/api/rhymes_subtractive', methods=['POST'])
def get_rhymes_subtractive():
    data=request.json
    print(data)
    word=data['word']
    rhymes = ph.get_subtractive_rhymes(word)
    return jsonify(rhymes)

@app.route('/api/rhymes_substitution', methods=['POST'])
def get_rhymes_substitution():
    data=request.json
    print(data)
    word=data['word']
    rhymes = ph.get_substitution_rhymes(word)
    return jsonify(rhymes)

@app.route('/api/rhymes_assonance', methods=['POST'])
def get_rhymes_assonance():
    data=request.json
    print(data)
    word=data['word']
    rhymes = ph.get_assonance_rhymes(word)
    return jsonify(rhymes)

@app.route('/api/rhymes_consonant', methods=['POST'])
def get_rhymes_consonant():
    data=request.json
    print(data)
    word=data['word']
    rhymes = ph.get_consonant_rhymes(word)
    return jsonify(rhymes)


@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/lyricRhyme.html')
def lyricRhyme():
    return render_template('lyricRhyme.html')

@app.route('/aiLyrics.html')
def aiLyrics():
    return render_template('aiLyrics.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#必须放到最后，否则post请求报404：
if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True)