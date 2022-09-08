# CS 2305
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

Example: 1+1≡0(false), 1+1≡2(true)

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
>2. ∧
>
>3. ∨
>
>4. ->
>
>5. <->

the higher precedence, the smaller the scope

# tauologies, contradictions,and contingencies

A tauology is a proposition that is always true

p ∨ -p

A contraction is a proposition that is always false

p ∧ -p

A contingency is a proposition that can be true of false

----

Two compounded propositons p and q are logically equivalent if p <-> q a tautology

we write this as p<->q or p≡q 

----

# De Morgan's law

-(p ∧ q) ≡ -p ∨ -q

-(p ∨ q) ≡ -p ∧ -q

The most important law in logic

it can also be extended

-(p1 ∧ p2 ∧ p3 ...) ≡ -p1 ∨ p2 ∨ p3 ...

-(p1 ∨ p2 ∨ p3 ...) ≡ -p1 ∧ p2 ∧ p3 ...

----

# Key logical equivalent

identity laws: p ∧ T ≡ p, p ∨ F ≡ p

domination laws: p ∨ T ≡ T, p ∧ F ≡ F

idempotent laws: p ∨ p ≡ p, p ∧ p ≡ p

double negation laws: -(-p) ≡ p

negation laws: p ∨ -p ≡ T, p ∧ -p ≡ F

----

commutative laws: p ∨ q ≡ q ∨ p, p ∧ q ≡ q ∧ p

associative laws: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r), (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)

distributive laws: (P ∨ (q ∧ r)) ≡ (p ∨ q) ∧ (p ∨ r), (p ∧ (q ∨ r)) ≡ (p ∧ q) ∨ (p ∨ r)

Absorption laws: p ∨ (p ∧ q) ≡ p, p ∧ (p ∨ q) ≡ p

---
# Shortcoming of truth table

The number of elements in a truth table increase vary fast when the number of varibles increase

elements = 2^n, where n is the number of elements

---

# Alternate approach to establish logical equivalences

simplify logical expression using well known results

it can handle large number of inputs

----

# Propositional satisfiability

A compound proposition is satisfiable if there an assignment of truth values to its variables that make it true, otherwise, it is unsatisfiable

-- a compound proposition has at lease one true in out put, otherwise it is unsatisfiable.

---

# Arguement

An arguement is a sequence of statements that end with a conclusion

A vaild arguement is a conclusion that follows from the fruth of the premises of the arguement

An arguement is vaild if and only if it is impossible for all premises to be true and the conclusions to be false(but not claim that if the conclusion is true then the premises are true as well)

An arguement which is not vaild is called a fallacy

(from this premises, can I make a conclusion bese on premises?)

---

p1:(p) john eats peanuts, (q) he falls sick (p -> q)

p2:(-p) john did not eat peanuts (-p)

conclusion: john did not fall sick (-q)

does ((p -> q) ∧ -p) -> -q ?

> ### everytime the premises is true, the conclusion should also be true, otherwise it is a fallacy

> ### only focus when the premises is true, if the conclusion is true. When the premises is false, no conclusion can be make

# Arguement forms
---
p1:(p) if you work hard, (q) you will get a good raise

p2:(-q) you did not get a good raise

conclusion: (-q) you did not work hard

---

p1:(p) john eats peanuts, (q) he falls sick (p -> q)

p2:(-p) john did not eat peanuts (-p)

conclusion: john did not fall sick (-q)

---

both are ((p -> q) ∧ -p) -> -q even they have different arguements, we says they have the same arguement form

---

# establishing validity of arguement forms

Bruth force approach: 

1. truth table

Rule of inference based apporach: 

1. first establish the validity of some relatively simple arguement form("rule of inference")

2. use rules of inference as building blocks to vaildate more complicated vaild forms

----

# ALL OF THOSE BELOW BASED ON EVERYTHING HAS A TRUTH VALUE OF TRUE

----
# modus ponens

p->q

p

\----

q

(p ^ (p -> q)) -> q

let p be it is snowing

let q be I will study discrete math

if it is snowing, then I will study discrete math

it is snowing

therfore I will study discrete math

----

# modus tollens

p -> q

-q

\----

-p

(-q ^ (p -> q)) -> -q

if it is snowing, I will study discrete math

I will not study discrete math

therefore, it is not snowing

----

# hypothetical syllgoism

# TODO: add corresponding tautology starting here

p -> q

q -> r

\----

p -> r

it snows

i will study discrete math

i will get A

if it is snowing, I will get A

-----

# disjunctive syllgoism

p v q

-P

\----

q

I will study discrete math

I will study english

I will study discrete math or english

I will not sutdy discrete math therefore I will study english

----

# addition

p

\----

p v q

(-p ^ (p v q)) -> q

---- 

# simplification

p ^ q

\----

p

(p ^ q) -> p

----

# conjunction

p

q

\----

p ^ q

# resolution

-p v r

p v q

\----

q ^ r

----
# Fallacies

<b>Those are wrong!</b>

p -> q

q

\----

p

----

p -> q

-p

\----

-q

----

# predicate logic

propositional calculus is inadequate to deal with arugements that with all cases, or with some case out of many cases

in such instances, instead of looking at propositions as a while, we need to understand their inner structure by 

?

TODO: FILL THIS PART

----

# WHAT IS predicate logic

An advanced form of symbolic logic that incorporates not only propositions, and relations between propositions[and, but ...], but also quantifiers[all, some, few...]

TODO: SAME AS ABOVE

----

# predicate
a predicate is a part of a declarative sentense that describe the properties of an object or the relationship between objects

TODO:

----
# propositional function

The generalized form of a proposition, containing one or more prodicates, but not tartgeting any specific subject,is known as propositional function

proposotions: jame is a student at bedford college

predicate: is a student at

predicate variable: x,y

propositional function: x is a student at y

prodicate in a propositional function contains a finited number of varibles and becomes a statement when specific values are subsituted for the variables

The propositional function does not have a truth value of it own

the set of all values that may be substituted in place of the variable in a predicate is known as the domain of the predicate variable

often the domain is denoted by U

<b>the truth value of a propositional function is depenced on the truth value of the predicate variable</b>