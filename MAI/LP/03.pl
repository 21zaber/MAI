%------Inside------%
depth([Fin|T], Fin, [Fin|T]).
depth(TMP, Fin, Way):- 
    prolong(TMP, NWay),
    depth(NWay, Fin, Way).

search_depth(ST, Fin):- 
    depth([ST], Fin, Way),
    write("Depth answer"), nl,
    show_answer(Way).

%------Wide------%
wide([[Fin | T] | _], Fin, [Fin | T]).
wide([TMP | X], Fin, Way):- 
    findall(Y, prolong(TMP, Y), Wayz),
    append(X, Wayz, NWay),
    wide(NWay, Fin, Way).

search_wide(ST, Fin):- 
    wide([[ST]], Fin, Way),
    write("Wide answer"), nl,
    show_answer(Way).

%------Iter------%
calci(1).
calci(N):-
    calci(M), 
    N is M + 1.

id([Fin | T], Fin, [Fin | T], N, Num):- 
    Nam is Num - N, 
    write("Iteration answer on depth:"),
    write(Nam).
id(TMP, Fin, Way, N, Num):- 
    N > 0,
    prolong(TMP, NWay),
    N1 is N - 1,
    id(NWay, Fin, Way, N1, Num).

search_iter(ST, Fin):- 
    calci(Depth), Depth > 20, !,
    id([ST], Fin, Way, Depth, Depth), nl,
    show_answer(Way).

prolong([TMP | T], [N, TMP | T]):- 
    move(TMP, N),
    not(member(N, [TMP | T])).
show_answer([_]).
show_answer([X, Y | T]):- 
    show_answer([Y | T]),
    write(X), nl.

move(X, Y):-    
    append(Z, [w  , '_' | T], X), 
    append(Z, ['_', w   | T], Y).
move(X, Y):- 
    append(Z, ['_', b   | T], X),
    append(Z, [b  , '_' | T], Y).
move(X, Y):- 
    append(Z, [w  , w, '_' | T], X),
    append(Z, ['_', w, w   | T], Y).
move(X, Y):- 
    append(Z, ['_', b, b   | T], X),
    append(Z, [b  , b, '_' | T], Y).
move(X, Y):- 
    append(Z, [w  , b, '_' | T], X),
    append(Z, ['_', b, w   | T], Y).
move(X, Y):- 
    append(Z, ['_', w, b   | T], X),
    append(Z, [b  , w, '_' | T], Y).

?- nl.
?- search_depth([w,w,w,'_',b,b,b,b], [b,b,b,b,'_',w,w,w]), nl.
?- search_wide([w,w,w,'_',b,b,b,b], [b,b,b,b,'_',w,w,w]),  nl.
?- search_iter([w,w,w,'_',b,b,b,b], [b,b,b,b,'_',w,w,w]),  nl.
