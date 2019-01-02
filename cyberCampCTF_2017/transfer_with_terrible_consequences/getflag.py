import hashlib
import string
import itertools

alphabet = string.ascii_lowercase + string.digits
partialHash = "50afXXXXXX6351475e54bf6eb2c96f2b"

print("Generating combinations...")

combinations = ["q" + ''.join(i) + "oq" for i in itertools.product(alphabet, repeat=5)]

combinationsCount = len(combinations)
print("Generated " + str(combinationsCount) + " combinations.")

print("Cracking...")

for i, combination in enumerate(combinations):
    hash = hashlib.new("md4", combination.encode("utf-8")).hexdigest()
    newPartial = hash[0:4] + "XXXXXX" + hash[10:]
    if (i % 1000000 == 0 or i == combinationsCount - 1):
        print("{0:.2f}".format(100 / combinationsCount * i) + "% " + str(i) + ": " + combination + " " + hash + " " + newPartial + " " + partialHash)
    if (newPartial == partialHash):
        print("Combination: " + combination)
        print("Hash: " + hash)
        break
