father(ahmed,wali).
father(ahmed,moin).
father(wali,raza).
father(wali,saad).
father(wali,sazzad).
father(moin,salman).
father(moin,sultan).
sibling(wali,moin).
sibling(moin,wali).
sibling(raza,saad).
sibling(saad,raza).
sibling(raza,sazzad).
sibling(sazzad,raza).
sibling(saad,sazzad).
sibling(sazzad,saad).
sibling(salman,sultan).
sibling(sultan,salman).
grandfather(X,Y) :-
father(X,Z) , father(Z,Y).
uncle(A,B) :-
father(X,A) , father(X,Y) , father(Y,B) , sibling( A,Y).
cousin(X,Y) :-
father(M,X) , father(N,Y) , sibling(M,N).