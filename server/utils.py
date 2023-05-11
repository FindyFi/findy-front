import os
import asyncio
import re
import hashlib


async def match_path_regex(regex_list, path):
    for regex in regex_list:
        match = re.match(regex, path)
        if match:
            return True
    return False


def env_bool(param: str, defval=None) -> bool:
    val = os.getenv(param, defval)
    return bool(val and val != "0" and val.lower() != "false")


def is_int(val):
    return isinstance(val, int) or (isinstance(val, str) and val.isdigit())

def get_jwt_secret():
    return os.getenv('JWT_SECRET')

async def run_thread(fn, *args):
    return await asyncio.get_event_loop().run_in_executor(None, fn, *args)

def hash_password(password):
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()

    # Convert the password to bytes and hash it
    sha256.update(password.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_password = sha256.hexdigest()

    return hashed_password