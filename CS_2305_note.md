# CS 2305
> ## 08 22 2022
> ### what is discrete math?
> logic mathmatic, the opposite of the continus math.

> continus math: focus on the process,phenomena that change a in a cointiuns fashion
>
> Infinity scope, and no hole in the scope
>
> example: real numbers

> discrete math: focus on the process, phenomea that consite of a sequence of individual steps
>
> finited scope, with holes between successive values
>
> example: integer
>
>

>### why study this course?
> Provide the mathematical background needed for more advanced courses in computer science
>
> Concepts learned here will be more useful in many other discplines like advanced mathmatics, philosophy, linnguisting...

> ### what will be learn
> basic concept of mathematic concepts
> 
> Different formal proof strategies
>
> Introduction to various discrete structures
>
> ...

## chapter 1
what is logic?

logic is the study of mormal reasoning

statements in a spoken languates are often ambigous in their meaning but statements in logic have a well defined meaning

logic is useful in any field in which it is important to analyze precise statements

## what is propositional logic (propositional calculus)
a propersition is a declearative sentance(statement) that can only be true or false.

Example: 1+1=0(false), 1+1=2(true)

It have to be decleartive and has to be either true or false, and it has to have an objective standard of measuring.

## formal representation of proposition
propositional variables(or sentential variable) are denoted by letter p,q,r,s

each propositional variable has a truth value of true(denoted as T) or false(denoted as F)

there are two types of proposition: atomic and compound

atomic: cannot be break down anymore

compound: mutiple proposition binded with logic operation

## logical opeartion

Negation

Conjunctin

Disjunction

XOR

Implication

Biconditional

----

those are called connector, because they connect proposition

## Truth table

A table that listed the output of truth value of a compound proposition for each combination of the truth values of its consituent propositions

Enum all the posibilities and outputs

## negation
Negation means not, it invert the input

! p(T) -> False

! p(F) -> True

## conjunction
conjunction means and, it output true only when both inputs are true

p(T) ∧ q(T) -> T

p(F) ∧ q(T) -> F

p(T) ∧ q(F) -> F

p(F) ∧ q(F) -> F

----
> ## 08 24 2022

Disjunction means or, it output true if any of the input is true

p(T) ∨ q(T) -> T

p(T) ∨ q(F) -> T

p(F) ∨ q(T) -> T

p(F) ∨ q(F) -> F

### English or:

inclusive or: disjunction

exclusion or: xor

# Exclusive or

it means one is true, but not both. it output true if one of the input is true, other case, it output false

p(T) ⊕ q(T) -> F

p(T) ⊕ q(F) -> T

p(F) ⊕ q(T) -> T

p(F) ⊕ q(F) -> F

# Truth table of compound proposition

| p      | q | p |q|
| ----------- | ----------- |---|---|
| p      | q       |||
| Paragraph   | Text        |||

# Equal proposition

Two proposition are equivalent (≡) if the always have the same truth table

-(p ∧ q) ≡ -p ∨ -q

So we say they are logically equivalent 

---

# IF p THEN q

consider: 

p: if it is raining, q: then the ground is wet

1. if it is raining, then ground is wet

2. if the ground is not wet, then it is not raining

you cannot say: it is raining because the ground is wet



|p|q|if p then q|
|---|---|---|
|T|T|T|
|T|F|F|
|F|T|T|
|F|F|T|

if I am not making any clam, it is true

No claim(p is false): vacuously true(q is true automatically)

(If the condition is not satisfied, I assume any conclusion is true)

# p only if q

the ground is not wet only when it is not raining

|p|q|p only if q|
|---|---|---|
|T|T|T|
|T|F|F|
|F|T|T|
|F|F|T|

p only if q is logically equivalent to if p then q

---

# implication/conditional statement

p implies q(p->q)
|p|q|p -> q|
|---|---|---|
|T|T|T|
|T|F|F|
|F|T|T|
|F|F|T|

if I am at home then it is raining

---

If it is raining then the ground is wet

it is raining: hypothsis

the ground is wet: contradiction

---

# Necessary and sufficient

Necessary: the ground is not wet, then it is not raining for sure

Sufficient: the ground is wet, but it may not be raining

There are many ways to make ground wet, they are all suffcient of the ground is wet

But if the ground is not wet, it is necessay it is not raining

( p -> q ) ≡ ( -p ∨ q )

# exercise

p:it is weekend

q: parking lots are full

parking lots are full only it is weekend

q -> p

q is condition and p is conclusion

---

This is different from CS programing, it only describe the relationship between two propositions

# Converse, contrapositive, and inverse

q -> p is the converse of p -> q

-p -> -q is the inverse of p -> q

-q -> -P is the contrapositive of p -> q

it is raining is a sufficient condition for my not going to town

converse: if I am not going to town, then it is raining

inverse: if I am going to town, then it is not raining

contrapositive: if I am going to town, then it is not raining

---

( p -> q ) ≡ ( -q -> -p )

___
# Biconditional/Bi-implication

it means "p if and only if q"

|p|q|p <-> q|
|---|---|---|
|T|T|T|
|T|F|F|
|F|T|F|
|F|F|T|

this is true if both p and q are both true or both false

for example: if I am at home if and only if it is raining

if I am not home if and only if it is not raining

___

(p -> q) ∧ (p -> q) ≡ (p <-> q)

p <-> q is the same as not XOR

# precedence of logic opeartion

>1. \-
>
>2. ^
>
>3. v
>
>4. ->
>
>5. <->

the higher precedence, the smaller the scope

# tauologies, contradictions,and contingencies

A tauology is a proposition that is always true

p V -p

A contraction is a proposition that is always false

p ^ -p

A contingency is a proposition that can be true of false

----

Two compounded propositons p and q are logically equivalent if p<->q a tautology

we write this as p<->q or p=q 

----

# De Morgan's law

-(p ^ q) = -p V -q

-(p V q) = -p ^ -q

The most important law in logic

it can also be extended

-(p1 ^ p2 ^ p3 ...) = -p1 V p2 V p3 ...

-(p1 V p2 V p3 ...) = -p1 ^ p2 ^ p3 ...

----

# Key logical equivalent

identity laws: p ^ T = p, p V F = p

domination laws: p V T = T, p ^ F = F

idempotent laws: p V p = p, p ^ p = p

double negation laws: -(-p) = p

negation laws: p V -p = T, p ^ -p = F