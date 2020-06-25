#!/usr/local/bin/python3

user_owns = 4
root_owns = 3
challenge_owns = 28


def ownership(root, user, challenge):
    return 100 * (root + user / 2 + challenge / 10) / (20 + (20 / 2) + (62 / 10))


for users in range(user_owns, 20):
    for roots in range(root_owns, users):
        for challenges in range(challenge_owns, 42):  # until Lvl50
            if 50 < ownership(roots, users, challenges) < 50.5:
                print('TO-DO: Roots: %i | Users: %i | Challenges: %i' % (roots - root_owns, users - user_owns, challenges - challenge_owns))
print('Ownership: %s' % str(round(100 * ownership(root_owns, user_owns, challenge_owns) / 50, 2)) + '% until Pro Hacker')
