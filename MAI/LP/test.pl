
a(B):- B = 1.

test(A):-
    B = [1, 2, 3],
    C = [2, 1, 3],
    A = permutation(B, C).
