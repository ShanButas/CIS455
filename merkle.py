import hashlib
import os

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

def merkle_tree(files):
    hashes = [hash_file(f) for f in files]

    while len(hashes) > 1:
        temp = []
        for i in range(0, len(hashes), 2):
            if i+1 < len(hashes):
                combined = hashes[i] + hashes[i+1]
            else:
                combined = hashes[i] + hashes[i]
            temp.append(hashlib.sha1(combined.encode()).hexdigest())
        hashes = temp

    return hashes[0]

folder = "files"
files = [os.path.join(folder, f) for f in os.listdir(folder)]

print("Top Hash:", merkle_tree(files))
