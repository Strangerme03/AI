eats(tiger,meat).
eats(cow, vegetables).
eats(human, meat).
eats(human, vegetables).
carnivorous(X) :- eats(X, meat).
omnivorous(X):- eats(X, meat), eats(X, vegetables).
hervivorous(X):- eats(X, vegetables).