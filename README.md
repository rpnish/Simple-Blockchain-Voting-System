

# Blockchain Voting System

A simple, hands-on blockchain-based voting system built with **Python** and **Flask**. Cast votes through a web interface, and watch them securely stored in a local blockchain with a live leaderboard. Perfect for learning blockchain fundamentals!

---

## Features

- Cast votes via a clean web form.
- Votes are stored in blocks linked together with hashes (blockchain simulation).
- Live leaderboard shows vote counts for each candidate.
- Demonstrates blockchain concepts like **immutability**, **hashing**, and **block linking**.
- Lightweight, runs locally, no external blockchain network required.


---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/blockchain-voting-system.git
cd blockchain-voting-system
````

2. **Install dependencies**

```bash
python -m pip install flask
```

*(hashlib and json are built-in, no need to install.)*

---

## Usage

1. Run the Flask app:

```bash
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000
```

3. **Cast a vote** by entering a voter ID and selecting a candidate.
4. **View the leaderboard** to see current vote counts.

---

## Folder Structure

```
blockchain_voting/
│
├── app.py              # Flask app with routes
├── blockchain.py       # Blockchain logic (blocks, hashing, chain)
├── templates/          # HTML templates for the web interface
│   ├── index.html      # Voting form
│   └── leaderboard.html # Vote results
└── README.md           # This file
```

---

## How It Works

* Each vote is stored as a transaction in a **block**.
* Each block contains:

  * `index` → position in the chain
  * `timestamp` → time of creation
  * `votes` → list of votes in the block
  * `previous_hash` → links block to the previous one
  * `hash` → unique SHA-256 hash of the block
* Blocks are **linked** to create a chain, demonstrating **immutability**.

---

## Future Improvements

* Prevent double voting using voter ID verification.
* Add a chart-based leaderboard (Chart.js).
* Persist votes to a file or database.
* Upgrade to a **real blockchain** using Ethereum smart contracts.

---

## License

This project is **open source** and free to use. Feel free to experiment, learn, and share!


