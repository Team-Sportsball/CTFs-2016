from hashlib import md5
import re
import sys

# clean_hash(md5(md5($str) . "SALT"));

salt = "SALT"
hash_regex = re.compile(r"^0e[0-9]+$")

with open(sys.argv[1], "rb") as ofile:
    for line in ofile:
        guess = line.rstrip('\n').rstrip('\r')
        final_result = md5(md5(guess).hexdigest() + salt).hexdigest()
        if hash_regex.match(final_result):
            print "%s results in  %s" % (guess, final_result)
