?- style_check(-singleton).
member(E, [E|T]):-
    true.
member(E, [H|T]):-
    member(E, T).

mmember([], L):-
    true.
mmember([H, T], L):-
    member(H, L),
    mmember(T, L).    

eqval([], []):-
    true.
eqval([H1 | T1], [H2 | T2]):-
    H1 == H2,
    eqval(T1, T2).

unique([]).
unique([Head|Tail]):-
    not(member(Head, Tail)), 
    unique(Tail).

student("Dima").
student("German").
student("Oleg").

subject("biology").
subject("history").
subject("chemistry").
subject("mathematics").

g1([O, G, D]):-
    member("history", D),
    not(member("history", O)),
    not(member("history", G)).

g2([O, G, D]):-
    eqval(O, G).

g3([O, G, D]):-
    member("biology", O),
    member("biology", D),
    member("biology", G).

g4([O, G, D]):-
    permutation([O, G, D], [S1, S2, S3]),
    member("biology", S1), member("chemistry", S1), 
    member("biology", S2), member("chemistry", S2), 
    not(member("biology", S3), member("chemistry", S3)). 

o1([O, G, D]):-
    member("mathematics", O),
    member("mathematics", G),
    member("mathematics", D).

o2([O, G, D]):-
    member("history", G).

o3([O, G, D]):-
    permutation(O, [S1, S2, S3]),
    member(S1, D),
    member(S2, D),
    not(member(S3, D)).
    
o4([O, G, D]):-
    member("chemistry", G),
    member("chemistry", D).

d1([O, G, D]):-
    permutation(["history", "mathematics", "chemistry", "biology"], [S, S1, S2, S3]),
    member(S, O), member(S, D), member(S, G), 
    not((member(S1, O), member(S1, D), member(S1, G))), 
    not((member(S2, O), member(S2, D), member(S2, G))), 
    not((member(S3, O), member(S3, D), member(S3, G))). 
    
d2([O, G, D]):-
    member("mathematics", D), 
    not(member("mathematics", O)), 
    not(member("mathematics", G)). 

d3(Solution):-
    permutation(Solution, [S1, S2]),
    not(eqval(S1, S2)).

d4(Solution):-
    not(o4(Solution)).

checko(Solution):-
    (o1(Solution), o2(Solution), not(o3(Solution)), not(o4(Solution)));   
    (o1(Solution), o3(Solution), not(o2(Solution)), not(o4(Solution)));   
    (o1(Solution), o4(Solution), not(o3(Solution)), not(o2(Solution)));   
    (o3(Solution), o4(Solution), not(o1(Solution)), not(o2(Solution)));   
    (o2(Solution), o4(Solution), not(o1(Solution)), not(o3(Solution)));   
    (o3(Solution), o2(Solution), not(o1(Solution)), not(o4(Solution))). 

checkd(Solution):-
    (d1(Solution), d2(Solution), not(d3(Solution)), not(d4(Solution)));   
    (d1(Solution), d3(Solution), not(d2(Solution)), not(d4(Solution)));   
    (d1(Solution), d4(Solution), not(d3(Solution)), not(d2(Solution)));   
    (d3(Solution), d4(Solution), not(d1(Solution)), not(d2(Solution)));   
    (d2(Solution), d4(Solution), not(d1(Solution)), not(d3(Solution)));   
    (d3(Solution), d2(Solution), not(d1(Solution)), not(d4(Solution))). 

checkg(Solution):-
    (g1(Solution), g2(Solution), not(g3(Solution)), not(g4(Solution)));   
    (g1(Solution), g3(Solution), not(g2(Solution)), not(g4(Solution)));   
    (g1(Solution), g4(Solution), not(g3(Solution)), not(g2(Solution)));   
    (g3(Solution), g4(Solution), not(g1(Solution)), not(g2(Solution)));   
    (g2(Solution), g4(Solution), not(g1(Solution)), not(g3(Solution)));   
    (g3(Solution), g2(Solution), not(g1(Solution)), not(g4(Solution))). 

    

solve(Solution):-
    O = [o1, o2, o3, o4],
    G = [g1, g2, g3, g4],
    D = [d1, d2, d3, d4],
    permutation(["mathematics", "history", "chemitry", "biology"], [O1, O2, O3, _]), 
    permutation(["mathematics", "history", "chemitry", "biology"], [G1, G2, G3, _]), 
    permutation(["mathematics", "history", "chemitry", "biology"], [D1, D2, D3, _]),
    Solution = [[O1, O2, O3], [G1, G2, G3], [D1, D2, D3]],
    checkg(Solution),
    checko(Solution), 
    checkd(Solution),
    nl,
    print('Dima: '), print([D1, D2, D3]), nl,  
    print('Oleg: '), print([O1, O2, O3]), nl,  
    print('German: '), print([G1, G2, G3]), nl,  
    nl.

?- solve(Solution).
