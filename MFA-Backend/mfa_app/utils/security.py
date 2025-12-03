'''import hashlib
import secrets
import jwt
import datetime
import random
import string

# A secret key for JWT signing (keep this safe in production!)
SECRET_KEY = "supersecretkey"  


def generate_token(user_id: int) -> str:
    """Generate a JWT token for a user"""
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # expires in 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token: str) -> dict:
    """Decode a JWT token"""
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}


def hash_password(password: str) -> str:
    """Hashes a password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password: str, hashed: str) -> bool:
    """Verifies if a password matches the stored hash"""
    return hash_password(password) == hashed


def generate_grid_challenge(size=6, num_prompts=3):
    """
    Generates a grid-based MFA challenge.
    Returns:
        - challenge_str: string to store in DB (e.g., A1=XY:B2=ZZ)
        - challenge_dict: dict to send only positions to frontend (e.g., {A1: XX, B2: YY})
    """
    rows = [chr(i) for i in range(ord('A'), ord('A') + size)]
    cols = [str(i + 1) for i in range(size)]

    all_positions = [r + c for r in rows for c in cols]
    selected_positions = random.sample(all_positions, num_prompts)

    challenge_dict = {
        pos: ''.join(random.choices(string.ascii_uppercase, k=2))
        for pos in selected_positions
    }

    challenge_str = ":".join([f"{k}={v}" for k, v in challenge_dict.items()])
    return challenge_str, challenge_dict'''
'''import random, string
from werkzeug.security import generate_password_hash, check_password_hash

# existing functions
def hash_password(password):
    return generate_password_hash(password)

def check_password(password, hashed):
    return check_password_hash(hashed, password)

# MFA grid setup
GRID = [
    ["A", "B", "C", "D", "E", "F"],
    ["G", "H", "I", "J", "K", "L"],
    ["M", "N", "O", "P", "Q", "R"],
    ["S", "T", "U", "V", "W", "X"],
    ["Y", "Z", "1", "2", "3", "4"],
    ["5", "6", "7", "8", "9", "0"]
]

def generate_coordinates(n=3):
    rows = list(string.ascii_uppercase[:6])  # A-F
    cols = list(range(1, 7))  # 1-6
    coords = []
    while len(coords) < n:
        coord = f"{random.choice(rows)}{random.choice(cols)}"
        if coord not in coords:
            coords.append(coord)
    return coords

def get_grid_value(coord):
    row_letter = coord[0].upper()
    col_number = int(coord[1]) - 1
    row_index = ord(row_letter) - ord('A')
    return GRID[row_index][col_number]'''

import random, string
from werkzeug.security import generate_password_hash, check_password_hash

# Password hashing
def hash_password(password):
    return generate_password_hash(password)

def check_password(password, hashed):
    return check_password_hash(hashed, password)

# MFA grid setup (6x6)
GRID = [['57', '92', '41', '86', '63', '22'],
 ['15', '44', '77', '81', '99', '36'],
 ['28', '55', '19', '62', '73', '11'],
 ['64', '48', '35', '97', '20', '54'],
 ['32', '10', '91', '68', '82', '40'],
 ['23', '75', '88', '59', '14', '95']]

def generate_coordinates(n=3):
    rows = list(string.ascii_uppercase[:6])  # A-F
    cols = list(range(1, 7))  # 1-6
    coords = []
    while len(coords) < n:
        coord = f"{random.choice(rows)}{random.choice(cols)}"
        if coord not in coords:
            coords.append(coord)
    return coords

def get_grid_value(coord):
    row_letter = coord[0].upper()
    col_number = int(coord[1]) - 1
    row_index = ord(row_letter) - ord('A')
    return GRID[row_index][col_number]
