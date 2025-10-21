from flask import Flask, jsonify, request, render_template, redirect, url_for
from blockchain import Blockchain
from collections import Counter

app = Flask(__name__)
blockchain = Blockchain()

# --- Home Page (Voting Form) ---
@app.route('/')
def home():
    return render_template('index.html')

# --- Submit Vote ---
@app.route('/vote', methods=['POST'])
def vote():
    voter_id = request.form.get('voter_id')
    candidate = request.form.get('candidate')

    if not voter_id or not candidate:
        return "Please fill all fields", 400

    blockchain.add_vote(voter_id, candidate)
    blockchain.create_block(blockchain.last_block['hash'])
    return redirect(url_for('leaderboard'))

# --- Leaderboard Page ---
@app.route('/leaderboard')
def leaderboard():
    all_votes = []
    for block in blockchain.chain:
        for vote in block['votes']:
            all_votes.append(vote['candidate'])

    counts = Counter(all_votes)
    return render_template('leaderboard.html', results=counts)

# --- API to view full chain ---
@app.route('/chain')
def get_chain():
    return jsonify(blockchain.chain)

if __name__ == '__main__':
    app.run(debug=True)
