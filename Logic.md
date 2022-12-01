# chapter 1

## Propositions

proposition is a claim that can only be true or false

## propositional variables

propositional variables is a symbol that denote a case. For example, p denotes ground is wet

Each propositional variable has a truth value T or F

Proposition can be <b> Atomic </b> or <b> Compound </b>

Atomic: Cannot be splited down

Compound: Can be splited down

## Logical Operators

Belows are Connectives:

Negation ¬

Conjunction ∧

Disjunction ∨

XOR ⊕

Implication →

Biconditional ⇔

## Truth table

A truth table is a enum of all posiable cases and results

Example:

| p   | q   | p ∧ q |
| --- | --- | ----- |
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | F     |
| F   | F   | F     |

This table shows all the posiable cases and result of the proposition p ∧ q

## Negation

Means opposite: 

p = T, then ¬ p = F

## AND

Only be true when both are true, otherwise false

p = T, q = T, p ∧ q = T

p = T, q = F, p ∧ q = F

## OR

Only be false when both are false, otherwise true

p = F, q = F, p ∨ q = F

p = T, q = F, p ∨ q = T

## XOR

Return the result of "p and q have different truth value". Negation of Biconditional(⇔)

p = T, q = F, p ⊕ q = T

p = T, q = T, p ⊕ q = F

## Biconditional

Return the result of "p and q have same truth value". Negation of XOR(⊕). Also known as iff (if and only if)

p = F, q = F, p ⇔ q = T

p = T, q = F, p ⇔ q = F

## Implication

Only return false when case 1 is true, case 2 is false. Also known as <b> if ...  then ...</b>

p = T, q = T, p → q = T

p = T, q = F, p → q = F

p = F, q = T, p → q = T

p = F, q = F, p → q = T

> ### Vacuous Truth
> when the case 1 is false, no matter what is the truth value of case 2, the output is true, because we cannot make any conclusion when case 1 is false, so we assume the claim is true

## Converse, Contrapositive, and Inverse

From p → q we can form new conditional statements

q → p is the converse of p → q

¬ p → ¬ q is the inverse of p → q

¬ q → ¬ p is the contrapositive of p → q

## Precedence of Logical Operators

| Operator | Precedence |
| -------- | ---------- |
| ¬        | 1          |
| ∧        | 2          |
| ∨        | 3          |
| →        | 4          |
| ⇔        | 5          |

## translate to english

Unless means if ... not ...
>–Unless I work hard, I will fail the exam
>
> If I do not work hard then I will fail the exam

## Tautologies, Contradictions, and Contingencies

Tautologies: something always true, example p ∨ ¬ p

Contradictions: something always false, example p ∧ ¬ p

Contingency: something neither Tautologies or Contradictions, example p ⇔ q

## Logical Equivalences

Means the propositions have the exactly same results, denote by ≡
| Law                 | proposition                                                       |
| ------------------- | ----------------------------------------------------------------- |
| Identity Laws       | p ∧ T ≡ p, p ∨ F ≡ p                                              |
| Domination Laws     | p ∨ T ≡ T, p ∧ F ≡ F                                              |
| Idempotent laws     | p ∧ p ≡ p, p ∨ p ≡ p                                              |
| Double Negation Law | ¬(¬ p) ≡ p                                                        |
| Negation Laws       | p ∨ ¬ p ≡ T, p ∧ ¬ p ≡ F                                          |
| Commutative Laws    | p ∨ q ≡ q ∨ p, p ∧ q ≡ q ∧ p                                      |
| Associative         | (p ∧ q) ∧ r ≡ p ∧ (q ∧ r), (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)              |
| Distributive Laws   | (p ∧ q) ∨ r ≡ (p ∨ r) ∧ (q ∨ r) , (p ∨ q) ∧ r ≡ (p ∧ r) ∨ (q ∧ r) |
| Absorption Laws     | p ∨ (p ∧ q) ≡ p, p ∧ (p ∨ q) ≡ p                                  |
| De Morgan's Laws    | ¬(p ∨ q) ≡ ¬ p ∧ ¬ q , ¬(p ∧ q) ≡ ¬ p ∨ ¬ q                       |
| Nameless            | p → q ≡ ¬ p ∨ q                                                   |
| Nameless            | p ⇔ q ≡ (p → q) ∧ (q → p)                                         |

## Propositional Satisfiability

A compound proposition is satisfiable if there exist at least one set of variables that can make its truth value of this proposition True.

It is unsatisfiable if there does not exist any set of variables that can make its truth value True.

A compound proposition is unsatisfiable if and only if its negation is a tautology

## Arguments

An argument is a sequence of statements (premises) that end with a conclusion

(balabala...then balabala, so balabala)

an argument is valid if and only if it is impossible for all the premises to be true and the conclusion to be false

(it is vaild, so it cannot have something like all premises are True but the conclusion is False, conclusion must be True)

However, we cannot say all premises are True if the conclusion is True

An argument which is not valid is called a fallacy

## Test for Argument Validity

> P1: If John eats peanuts, he falls sick
>
> P2: John did not eat peanuts
>
>---
>
> ∴ John did not fall sick

Does ((p → q) ∧ ¬ p) → ¬ q?

| p   | q   | ((p → q) ∧ ¬ p) | ¬ q |
| --- | --- | --------------- | --- |
| F   | T   | T               | F   |

premises is True ((p → q) ∧ ¬ p), but conclusion is False (¬ q), so this is a fallacy

## Argument Forms

> P1: If John eats peanuts, he falls sick
>
> P2: John did not fall sick
>
>---
>
> ∴ John did not eats peanuts

> P1: If you work hard, you will get a good raise
>
> P2: You did not get a good raise
>
>---
>
> ∴ You did not work hard

Even those two arguements are different, the have the same form which is ((p → q) ∧ ¬ q) → ¬ p

When two arguements have the same arguement form, they:

1. Have the same symbolic representation
2. Belong to the same “family” of arguments

## Important Rules of Inference

| Rules of Inference                         | Tautology                     | Name                   |
| ------------------------------------------ | ----------------------------- | ---------------------- |
| p <br> p → q <br>-------<br> ∴ q           | (p ∧ (p → q)) → q             | Modus ponens           |
| ¬ q <br> p → q <br>-------<br> ∴ ¬ p       | (¬ q ∧ (p → q)) → ¬ p         | Modus tollens          |
| p → q <br> q → r <br>-------<br> ∴ r       | ((p → q) ∧ (q → r)) → (p → r) | Hypothetical Syllogism |
| p ∨ q <br> ¬ p <br>-------<br> ∴ q         | (¬ p ∧ (p ∨ q)) → q           | Disjunctive Syllogism  |
| p <br>-------<br> ∴ p ∨ q                  | p → (p ∨ q)                   | Addition               |
| p ∧ q <br>-------<br> ∴ p                  | (p ∨ q) → p                   | Simplification         |
| p <br> q <br>-------<br> ∴ p ∧ q           | ((p) ∧ (q)) → p ∧ q           | Conjunction            |
| p ∨ q <br> ¬ p ∨ r <br>-------<br> ∴ q ∨ r | ((¬ p ∨ r) ∧ (p ∨ q)) → q ∨ r | Resolution             |

## Comparing the Tautologies for Logical Equivalences and Rules of Inference

> ### Logical Equivalences
> 
> Logical_Expression1 ⇔ Logical_Expresion2 is a tautology

> ### Rules of Inference
> 
> Conjunction_of_premises → Conclusion is a tautology

## Fallacies

1. Fallacy of affirming the conclusion
<br> p → q <br> q <br>-------<br> ∴ p <br> cannot get premises from conclusion

2. Fallacy of denying the hypothesis
<br> p → q <br> ¬ p <br>-------<br> ∴¬ q <br> Vacuous truth

## Predicate Logic

Propositional calculus is inadequate to deal with arguments that deal with all cases, or with some case out of many cases

In such instances, instead of looking at propositions as a whole, we need to understand their inner structure by
>- breaking propositions up into parts {predicates and variables}
>
>- analyzing quantifiers like "all" or "some"

## What is Predicate Logic

1. Include both relationship (and, not, or...) and quantity (one, at least one, all...)

2. Studies the logical form INSIDE atomic propositions

3. Also known as predicate calculus and first-order logic

## Predicate

Describe the properties of an object or the relationship between objects

EX: In the proposition “17 is a prime number”, “is a prime number” is the predicate

## Propositional Function

A proposition contains one or more predicates but does not focus on specific object

EX: 
> Proposition: James is a student at Bedford College
> 
> Predicate: is a student at
>
> Predicate variables: x, y
>
> Propositional Function: x is a student at y {represented as P(x, y)}

Propositional Function does not have truth value by it own

propositional function becomes a proposition when it is filled with variables

The set of all possible values is called the Domain, which denoted by U

The statement P(x) is said to be the value of the propositional function P at x <br>(P(x) is only one case out of all possible results)

## Compound Expressions

Connectives from propositional logic carry over to predicate logic

Expressions with variables are not propositions and therefore do not have truth values. For example: <br> P(x) → P(y)

When used with quantifiers (at least one, all), these expressions (propositional functions) become propositions

Propositional functions can have multiple variables

## Quantifiers

The "degree" of "Being True" of a propositional function over a range of elements (from the pertinent domain)

There are two types of them: 

1. Universal Quantifier, “For all,”, ∀
2. Existential Quantifier, “There exists,”, ∃

## Uniqueness Quantifier

∃! x P(x) means that P(x) is true for one and only one x in the universe of discourse

"There is a unique x such that..."

## Trailing Quantifiers

Additional information at the end of the sentense

Example: ∀ x ∈ R , x <sup> 2 </sup> ≥ 0(x is a real number and x <sup> 2 </sup> is not 0)

this will include all real number but 0

## Bound and Free Variables

when an variable has something to do with the quantifier, we say it is bound, otherwise, we say it is free

Example: ∃ x(x + y = 1), in this case, x in bound and y is free

## quantifer, propositional function, and proposition

Quantifiers provide an alternate way to convert propositional functions to propositions

Example: Let P(x) be the propositional function “x + 1 > x”. Then ∀ x P(x) is a proposition

## ways to make propositional function a proposition

In general, all the variables that occur in a propositional function must be bound or set equal to a particular value to turn it into a proposition

- universal quantifiers

- existential quantifiers

- value assignments

## Properties of Quantifiers

The truth value of ∀ x P(x) and ∃ x P(x) depend on both the propositional function P(x) and on the domain U

If the domain is empty, for any propositional function:

- ∀ xP(x) is true

- ∃ xP(x) is false

## Truth Set

A truth set is a set contains all values of x that make the proposition true

Example, P(x): "x is a factor of 8", Domain: all positive integers

Then the truth set of P(x) is {1,2,4,8}

## Quantifiers Over Finite Domains

∀ xP(x) ≡ P(x1) ∧ P(x2) ∧ P(x3) ∧ … ∧ P(xn)

Conjunction of propositions

∃ xP(x) ≡ P(x1) ∨ P(x2) ∨ P(x3) ∨ … ∨ P(xn)

Disjunction of propositions

## Quantifiers with Restricted Domains

Sometimes it is not feasible to enumerate the domain of a quantifier. Then we use the excluding method to exclude those we don't want out

In such instances, an abbreviated notation is often used

- a condition a variable must satisfy is included after the quantifier

- Such quantifiers are called restricted quantifiers

Example:

(∀ x)<sub> x < 0</sub> (x <sup> 2 </sup> > 0)

means for all x such that x smaller than 0, we have x to the power of 2 is greater than 0

## Precedence of Quantifiers

The ∀ and ∃ have higher precedence than any logical operator

which means ∀ x P(x) ∨ Q(x) means (∀ x P(x)) ∨ Q(x) instead of ∀ x (P(x) ∨ Q(x))

## Equivalences in Predicate Logic

have the save value for every possible result

cover every domain

Example: 

∀ x ¬¬ S(x) ≡ ∀ x S(x)

∀ x(P(x) ∧ Q(x)) ≡ ∀ x P(x) ∧ ∀ x Q(x)

Assume ∀ x(P(x) ∧ Q(x)) is True, then P(x) ∧ Q(x) is true for every value of x in domain, so P(x) and Q(x) are True for every value in domain

Assume ∀ x P(x) ∧ ∀ x Q(x) is True, then P(x) and Q(x) are True for every value of x in domain

So they are equivalent

## Some equivalences and not equivalences

1. ∀ x ¬¬ S(x) ≡ ∀ x S(x)

2. ¬∀ x P(x) ≡ ∃ x ¬ P(x)

3. ¬∃ x P(x) ≡ ∀ x ¬ P(x)

4. ∀ x(P(x) ∧ Q(x)) ≡ ∀ x P(x) ∧ ∀ x Q(x)

5. ∃ x(P(x) ∨ Q(x)) ≡ ∃ xP(x) ∨ ∃ xQ(x)

6. ∀ x(P(x) ∨ Q(x)) ¬≡ ∀ xP(x) ∨ ∀ xQ(x)

7. ∃ x(P(x) ∧ Q(x)) ¬≡ ∃ xP(x) ∧ ∃ xQ(x)

The Universal quantifier cannot be distributed over disjunction, and the existential quantifier cannot be distributed over conjunction

## De Morgan’s Laws for Quantifiers

| Negation  | Equivalent Statement | When Is Negation True?         | When Is False                 |
| --------- | -------------------- | ------------------------------ | ----------------------------- |
| ¬∃ x P(x) | ∀ x ¬ P(x)           | For every x, P(x) is false     | There is x which P(x) is true |
| ¬∀ x P(x) | ∃ x ¬ P(x)           | There is x which P(x) is false | P(x) is true for every x      |

## Restricted Quantifiers

Unrestricted quantifiers apply to the entire domain of discourse

A restricted quantifier has the same semantics as an unrestricted quantifier except that the variables in the domain must satisfy a certain condition in order for the quantification to apply

(Which means we only focus on the values in the domain which satisfies the restriction)

Example: 

(∀ x)<sub> x < 0</sub> (x <sup> 2 </sup> > 0)

for every x in real numbers, if x is smaller than 0, then we have x to the power of 2 is larger than 0

## Restricted quantifer -> Unrestricted quantifer

Sometimes we need to express a restricted quantifier as an unrestricted quantifier

∃ x <sub> P(x)</sub> Q(x) ≡ ∃ x (P(x) ∧ Q(x))

∀ x <sub> P(x)</sub> Q(x) ≡ ∀ x (P(x) → Q(x))

## Nested Quantifiers

In nested quantifiers one quantifier is within the scope of another quantifier

Example: Every real number has an inverse

∀ x ∃ y(x + y = 0)

## Order of Quantifiers

The order of the nested quantifiers is important, unless all the quantifiers are universal quantifiers or all are existential quantifiers

## Quantifications of Two Variables

| Statement                         | When True?                                                     | When False?                                          |
| --------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------- |
| ∀ x ∀ yP(x, y)<br> ∀ y ∀ xP(x, y) | P(x, y) is true for every pair of x and y                      | when any pair of x, y make P(x, y) false             |
| ∀ x ∃ yP(x, y)                    | For every x, there is an y such that P(x, y) is true           | when there is a x for every y P(x, y) is false       |
| ∃ x ∀ yP(x, y)                    | There is at least one x such that for every y, P(x, y) is true | for every x, there is a y such that P(x, y) is false |
| ∃ x ∃ yP(x, y)<br> ∃ y ∃ xP(x, y) | There is a pair of x and y such that                           | for every pair of x and y, P(x, y) is false          |

## Two Surprising Results

if ∃ y ∀ xP(x, y) is true, then ∀ x ∃ yP(x, y) must be also true

if ∀ x ∃ yP(x, y) is true, it is not necessay for ∃ y ∀ xP(x, y) to be true

## Additional Rules of Inference for Quantified Statements

| Rule of Inference                                                     | Name                       |
| --------------------------------------------------------------------- | -------------------------- |
| ∀ xP(x)<br>------<br> ∴ P(c)                                          | Universal instantiation    |
| P(c) for an arbitrary of c <br>-------------------------<br> ∴∀ xP(x) | Universal generalization   |
| ∃ xP(x)<br>-------------------------<br> ∴ P(c) for some element c    | Existential instantaion    |
| P(c) for some element c <br>-------------------------<br> ∴∃ xP(x)    | Existential generalization |

x: Unspecified member of the domain

c: Specific member of the domain

## Using Rules of Inference

"All men has two legs", "John is a man", shows John has two legs

let M(x) represents "x is a man", and L(x) represents "x has two legs"

premises: ∀ x(M(x) → L(x)), M(John)

∀ x(M(x) → L(x))<br>----------------<br> ∴ M(John) → L(John)

M(John) → L(John)<br> M(John)<br>--------------------<br> ∴ L(John)

## Universal Modus Ponens

Combines UI and Modus Ponens

∀ x(P(x) → Q(x))<br> P(c)<br>-----------------<br> ∴ Q(c)

## Universal Modus Tollens

∀ x(P(x) → Q(x))<br> ¬ Q(c)<br>-----------------<br> ∴¬ P(c)

## Proofs of Mathematical Statements

A proof is a valid argument that establishes the truth of a statement

A theorem is a statement that can be shown to be true using:

- definitions

- other theorems

- axioms (statements which are given as true, also known as postulates)

- rules of inference

A lemma is a ‘helping theorem’ or a result which is needed to prove a theorem

A corollary is a result which follows directly from a theorem.
Less important theorems are sometimes called propositions

A conjecture is a statement that is being proposed to be true. Once a proof of a conjecture is found, it becomes a theorem. It may turn out to be false

## Direct Proof

A direct proof shows that a conditional statement p → q is true by showing that if p is true, then q must also be true

We assume that p is true and use axioms, definitions, and previously proven theorems, together with rules of inference, to show that q must also be true

Example:

Proof the square of a odd number is also an odd number

any odd number : 2n+1

(2n + 1)<sup> 2 </sup> = 4n <sup> 2 </sup> + 4n + 1 = 2 * (n <sup> 2 </sup> + 2n) + 1

let r = (n <sup> 2 </sup> + 2n), therefore (2n + 1)<sup> 2 </sup> = 2r + 1, and because of 2r is an even number, so 2r + 1 is an odd number

## Proof By Contraposition

Sometimes it is easier to prove theorems using proof by contraposition

- the conditional statement p → q is proved by showing that its contrapositive, ¬ q → ¬ p is true

Example: Prove that if n is an integer and 3n + 2 is odd, then n is odd

let n = 2k for some integer k

the 3n + 2 = 6k + 2 = 2(3k + 1)

let j = 3k + 1 for some integer j

so 3n + 2 = 6k + 2 = 2j

so 3n + 2 is even

Since we have shown ¬ q → ¬ p , p → q must hold as well. We have proved by contraposition that if 3n + 2 is odd, then n is odd

## Vacuous & Trivial Proofs

- p → q ≡ ¬ p ∨ q

- A proof that makes use of the fact that p → q must be true when p is false is called a vacuous proof

- A proof that makes use of the fact that p → q must be true when q is true is called a trivial proof

- These proofs are never treated as complete proofs but they are used in conjunction with other proof techniques (like proof by cases and mathematical induction) to establish that special cases of a theorem are not in violation of the generalized theorem

## Proof by Contradiction

We make a opposite proof of if p is true, then q is false for p → q. Clearly, therefore, the assumption that if p is true then q is false is wrong. In other words, if p is true then q must be true

Example: 

Prove that if you pick 22 days from the calendar, at least 4 must fall on the same day of the week

Assume that no more than 3 of the 22 days fall on the same day of the week. Because there are 7 days of the week, we could only have picked 21 days. This contradicts the assumption that we have picked 22 days

## Background Information
- Fundamental theorem of arithmetic (also called the unique factorization theorem)

> Every number is a prime or a unique product of primes

## Theorems that are Biconditional Statements

To prove a theorem that is a biconditional statement, that is, a statement of the form p ⇔ q, we show that p → q and q → p are both true

Example:

Prove the theorem: “If n is an integer, then n is odd if and only if n <sup> 2 </sup> is odd.”

Solution: 

We have already shown (previous slides) that both p → q and q → p. Therefore we can conclude p ⇔ q

## Proof By Counterexample

Statements of the form ∀ xP(x) can be proved to be false by providing a counterexample ∃ x(¬ P(x))

Example: Show that the statement “Every positive integer is the sum of the squares of two integers” is false

The number 3 can be represented as the sum of two numbers in one of two ways (order being immaterial)

3 = 0 + 3 = 0 <sup> 2 </sup> + 3

3 = 1 + 2 = 1 <sup> 2 </sup> + 2

In neither case can be number 3 be represented as a sum of two squares.
Therefore we have proved by counterexample that “Every positive integer is the sum of the squares of two integers” is false

## Mistakes in proofs

- performing a disallowed mathematical operation (divide by 0)

- given p → q is true and q is true implying the conclusion that p is true(q can be True when p is False)

- given p → q is true and p is false implying the conclusion that q is false(q is true)

- basing one or more steps of the proof on the truth of the statement being proved, or a statement equivalent to it (begging the question or circular reasoning)

## What is wrong with this

“Proof” that 1 = 2

1. a = b
2. a <sup> 2 </sup> = a * b
3. a <sup> 2 </sup> - b <sup> 2 </sup> = a * b - b <sup> 2 </sup>
4. (a - b)(a + b) = b(a - b)
5. a + b = b
6. 2b = b
7. 2 = 1

Solution: step 5, divide both side by (a - b), (a - b) = 0, it is dividing both side by 0 which is undefined

## If direct methods of proof do not work

- We may need a clever use of a proof by contraposition

- Or a proof by contradiction

## Proof by Exhaustion

Used in situations where theorems can be proved by examining a relatively small number of examples

(list all cases and proof they are true)

Example: 

> Prove that (n + 1)3 ≥ 3n if n is a positive integer with n ≤ 4
>
>----
>
> solution:
>
> Case n = 1: (1 + 1)3 = 23 = 8, which is ≥ 31 i.e. 3
>
> Case n = 2: (2 + 1)3 = 33 = 27, which is ≥ 32 i.e. 9
>
> Case n = 3: (3 + 1)3 = 43 = 64, which is ≥ 33 i.e. 27
>
> Case n = 4: (4 + 1)3 = 53 = 125, which is ≥ 34 i.e. 81

## Proof by Cases

Used in situations where: 

1. it is imposibile to list all the cases
2. need to consider different cases in different ways separately

To prove a conditional statement of the form

Example: 

>(p1 ∨ p2 ∨ p3 ... ∨ pn) → q
>
>(p1 ∨ p2 ∨ p3 ... ∨ pn) → q ≡ ¬(p1 ∨ p2 ∨ p3 ... ∨ pn) ∨ q
>
> ¬(p1 ∨ p2 ∨ p3 ... ∨ pn) ∨ q ≡ (¬ p1 ∧ ¬ p2 ∧ ¬ p2 ∧ ¬ p3 ... ∧ ¬ pn) ∨ q
>
>(¬ p1 ∧ ¬ p2 ∧ ¬ p2 ∧ ¬ p3 ... ∧ ¬ pn) ∨ q ≡ (¬ p1 ∨ q) ∧ (¬ p2 ∨ q) ∧ (¬ p3 ∨ q) ... ∧ (¬ pn ∨ q)
>
>(¬ p1 ∨ q) ∧ (¬ p2 ∨ q) ∧ (¬ p3 ∨ q) ... ∧ (¬ pn ∨ q) ≡ (p1 → q) ∧ (p2 → q) ∧ (p3 → q) ... ∧ (pn → q)

Use the tautology

(p1 ∨ p2 ∨ p3 ... ∨ pn) → q ⇔ (p1 → q) ∧ (p2 → q) ∧ (p3 → q) ... ∧ (pn → q)

Each of the implications p <sub> n </sub> → q is a case

----

Example:

> Prove that Prove that if n is an integer, then n <sup> 2 </sup> ≥ n
>
> Case 1 : n = 0, then n <sup> 2 </sup> = 0, which n <sup> 2 </sup> >= n
>
> Case 2 : n <= 1, then n<sup> 2 </sup> >= n or n <sup> 2 </sup> = n = 1
>
> Case 3: n >= 1, then n <sup> 2 </sup> > n
>
> Since the inequality n <sup> 2 </sup> ≥ n holds in all three cases, we can conclude that if n is an integer, then n <sup> 2 </sup> ≥ n

## Without Loss of Generality

The phrase “Without Loss of Generality” (WLOG) is used in proofs with cases to assert that by proving one case of a theorem, no additional argument is required to prove other specified cases

( Standary english: This is a common sense so I dont want to prove it)

## Existence Proofs

A proof of a proposition of the form ∃ xP(x) is called an existence proof

there are two form of proof for existence proof

- Constructive: Finding an element a, which P(a) is True

- Nonconstructive: Proof there is ∃ xP(a) is True without finding an element. For example, using proof by contradiction to shows that not all P(a) are False

Example 1: 

> Show that there is a positive integer that can be written as the sum of cubes of positive integers in two different ways
>
> 1729 = 10 <sup> 3 </sup> + 9 <sup> 3 </sup> = 12 <sup> 3 </sup> + 1 <sup> 3 </sup>

Example 2:

> Show that there exist irrational numbers x and y such that xy is rational
>
> We know that √ 2 is irrational. Let us consider the number √ 2 <sup> √ 2 </sup>. There are two possibilities to consider
>
>> Possibility 1: √ 2 <sup> √ 2 </sup> is rational
>>
>>- In this case x = y = √ 2 and x <sup> y </sup> is rational
>
>> Possibility 2: √ 2 <sup> √ 2 </sup> is irrational
>>
>>- In this case let x = √ 2 <sup> √ 2 </sup> and y = √ 2. Therefore x <sup> y </sup> = (√ 2 <sup> √ 2 </sup>)<sup> √ 2 </sup> = (√ 2)<sup> 2 </sup> = 2, a rational number
>
> This is an example of Nonconstructive proof, we don't know the property of the √ 2 <sup> √ 2 </sup>, but but we have proved that one of them does has the desired property

## Uniqueness Proofs

Some theorems asset the existence of a unique element with a particular property, ∃! x P(x). The two parts of a uniqueness proof are

- Existence: x exist such that P(x) satisfies the properties
- Uniqueness: if y != x, then P(y) != P(x)

Example: 

> Shows that if a, b are real numbers, and a != 0, there exits an real number r such that ar + b = 0
> 
> Solution:
> ___
>
> ar + b = 0 <br> ar = -b <br> r = $-\frac{b}{a}$
>
> ___
>
> Existance:
> 
> the real number r has a solution because ar + b = -b + b = 0, there for r = $-\frac{b}{a}$
> 
> Uniqueness: 
> 
> Suppose that s is a real number such that as + b = 0
> 
> as + b = ar + b
> 
> as = ar
> 
> s = r
> 
> therfore, r is unique
> 
> QED

## Proof Strategies for proving p → q

> Choose a method
> 
>> 1.First try a direct method of proof
>>
>> 2.If this does not work, try an indirect method (e.g., try to prove the contrapositive)
>
> For whichever method you are trying, choose a strategy
>> 1.First try forward reasoning. Start with the axioms and known theorems and construct a sequence of steps that end in the conclusion. Start with p and prove q, or start with ¬ q and prove ¬ p
>>
>> 2.If this doesn’t work, try backward reasoning

## Backward Reasoning

1. we assume the conclusion is correct, then we try to get conditions from it 
2. use the conditions to get backward, until we reach the start point
3. Start reversing, follow the opposite direction and make the forward proof

(we need to proof the reliability of those conditions before moves on)

Example: 

> Question:
>
> Prove that for any two distinct positive real numbers x and y, their arithmetic mean [i.e. (x + y)∕ 2] is greater than their geometric mean [i.e. √(xy)]
>
> Solution:
>
>> We start by using backward reasoning to establish the starting point of our proof
>
> Let us assume the conclusion is true
>> 1. (x + y)∕ 2 > √(xy)
>> 2. ((x + y)<sup> 2 </sup>) ∕ 4 > xy (squr both sides)
>> 3. (x + y)<sup> 2 </sup> > 4xy
>> 4. x <sup> 2 </sup> + 2xy + y <sup> 2 </sup> > 4xy
>> 5. x <sup> 2 </sup> - 2xy + y <sup> 2 </sup> > 0
>> 6. (x - y)<sup> 2 </sup> > 0
>
> Now that we have our secondary conclusion, let us see if we can prove it.
>
> (x - y)<sup> 2 </sup> > 0 <sup> 2 </sup> is true because x != y, so x - y != 0, and for any non-zero number, the square of it is always positive
> 
> Now we move to our formal proof
> 
> (x − y)<sup> 2 </sup> > 0
>
> x <sup> 2 </sup> − 2xy + y <sup> 2 </sup> > 0
>
> x <sup> 2 </sup> + 2xy + y <sup> 2 </sup> > 4xy
>
> (x + y)<sup> 2 </sup> > 4xy
>
> (x + y)<sup> 2 </sup> ∕ 4 > xy
>
> (x + y) ∕ 2 > √(xy)

## The Role of Open Problems

___

Unsolved problems have motivated much work in mathematics. Fermat’s Last Theorem was conjectured more than 300 years ago. It has only recently been finally solved

Fermat’s Last Theorem: The equation x <sup> n </sup> + y <sup> n </sup> = z <sup> n </sup>
has no solutions in integers x, y, and z, with xyz ≠ 0 whenever n is an integer with n > 2

A proof was found by Andrew Wiles in the 1990s

___

3N + 1 problem: 

...

___

## Additional Proof Methods

Time permitting, we will see many other proof methods:

- Mathematical induction, which is a useful method for proving statements of the form ∀ n P(n), where the domain consists of all positive integers

- Structural induction, which can be used to prove such results about recursively defined sets

- Cantor diagonalization is used to prove results about the size of infinite sets

- Combinatorial proofs use counting arguments

# chapter 2

## set

A set is an unordered collection of objects

The objects in a set are called the elements, or members of the set. A set is said to contain its elements

The notation a ∈ A denotes that a is an element of the set A
If a is not a member of A, write a ∉ A

By convention, sets are denoted using uppercase letters while lowercase letters are used to denote elements of sets

elements in a set are unique

(just like Python dictionary with only keys)

## Describing a Set

### <b> Roster Method </b>

---

S = {a, b, c, d}

(order does not matter)

Each distinct object is either a member or not; listing more than once does not change the set

S = {a, b, c, d} = {a, b, c, b, c, d}

Elipses (…) may be used to describe a set without listing all of the members when the pattern is clear

S = {a, b, c, d, ……, z }

(iterator)

---

## Some Important Sets

| name | meaning                      | Set                    |
| ---- | ---------------------------- | ---------------------- |
| N    | natural numbers              | {0,1,2,3…}             |
| Z    | integers                     | {…,-3,-2,-1,0,1,2,3,…} |
| Z ⁺  | positive integers            | {1,2,3,…}              |
| R    | set of real numbers          |                        |
| R+   | set of positive real numbers |                        |
| C    | set of complex numbers       |                        |
| Q    | set of rational numbers      |                        |

## Set-Builder Notation

Specify the property or properties that all members must satisfy
The general form of this notation is {x ∣ x has property P} and is read “the set of all x such that x has property P”

S = {x | x is a positive integer less than 100}

A predicate may be used: S = {x | P(x)}

Positive rational numbers: Q+ = {x ∈ R | x = p/q, for some positive integers p, q}

(just like python list generator: [x for x in range(0,100000)] if Prime(x))

## Interval Notation

"[" and "]" means including boundary, "(" and ")" means excluding boundary

closed interval [a, b]

open interval (a, b)

[a, b] = {x | a <= x <= b}

(a, b) = {x | a < x < b}

## Universal Set, Empty Set and Singleton Set

The universal set U is the set containing everything currently under consideration

The empty set (aka null set) is the set with no elements. Symbolized ∅, but {} also used

A set with one element is called a singleton set

## Venn Diagrams

In Venn diagrams the universal set U is represented by a rectangle

Inside the Venn Diagram for U, circles or other geometrical figures are used to represent sets

Sometimes points are used to represent the particular elements of the set

![](https://vt-vtwa-assets.varsitytutors.com/vt-vtwa/uploads/problem_question_image/image/2063/Venn.gif)

## Some things to remember

Sets can be elements of sets: {{1,2,3}, a, {b, c}}, {N, Z, Q, R}

Let A = { {a}, {b}, {a, b}}, In this case {a} ∈ A, but a ∉ A

The empty set is different from a set containing the empty set

An empty set is a subset of any set

## Set Equality

Two sets are equal if and only if they have the same elements (order don't matter)

Therefore if A and B are sets, then A and B are equal if and only if ∀ x(x ∈ A ⇔ x ∈ B)

---

Remember:
- order is immaterial
- multiplicity is ignored

---

## Subsets

The set A is a subset of B, if and only if every element of A is also an element of B

The notation A ⊆ B is used to indicate that A is a subset of the set
B

A ⊆ B holds if and only if ∀ x(x ∈ A → x ∈ B) is true

1. Because x ∈ ∅ is always false, ∅ ⊆ S , for every set S
2. Because x ∈ S → x ∈ S, S ⊆ S, for every set S

“Every nonempty set S is guaranteed to have at least two
subsets, the empty set and the set S itself”

(super class)

## Supersets

If set A is a subset of set B, then set B is a superset of set A

The notation B ⊇ A is used to indicate that B is a superset of the set A

A ⊆ B and B ⊇ A are equivalent statements

(sub class)

## Showing a Set is or is not a Subset of Another Set

Showing that A is a Subset of B: To show that A ⊆ B, show that if x belongs to A, then x also belongs to B

Showing that A is not a Subset of B: To show that A is not a subset of B, A ⊈ B, find an element x ∈ A with x ∉ B. (Such an x is a counterexample to the claim that x ∈ A implies x ∈ B)

(To show not a subset, just proof existance for x ∈ A and x ∉ B)

## Another look at Equality of Sets

∀ x(x ∈ A ⇔ x ∈ B) is equal to ∀ x [(x ∈ A → x ∈ B) ∧ (x ∈ B → x ∈ A )] or (A ⊆ B) and (B ⊆ A)

## Proper Subsets

If A ⊆ B, but A ≠ B, then we say A is a proper subset of B, denoted by A ⊂ B

If A ⊂ B, then:

> ∀ x(x ∈ A → x ∈ B) ∧ ∃ x(x ∈ B ∧ x ∉ A) must be True

## Set Cardinality

the size of the set (ignore the duplicate elements)

The cardinality of a finite set A, denoted by |A|

1. |ø| = 0
2. Let S be the letters of the English alphabet. Then |S| = 26
3. |{1, 2, 3}| = 3
4. |{ø}| = 1
5. The set of integers is infinite

## Power Sets

The set of all subsets of a set A, denoted P(A), is called the power set of A

If A = {a, b} then P(A) = {ø, {a}, {b}, {a, b}}

> Q) What is the power set of ø?
>
> A) P(ø) = {ø}

> Q) What is the power set of {ø}?
>
> A) P({ø}) = {ø, {ø}}

## Tuples

Because sets are unordered, a different structure is needed to represent ordered collections. This is provided by ordered n-tuples

The ordered n-tuple (a <sub> 1 </sub>, a <sub> 2 </sub>,…, a <sub> n </sub>) is the ordered collection that has a1 as its first element and a2 as its second element and so on until an as its last element

Two n-tuples are equal if and only if their corresponding elements are equal

2-tuples are called ordered pairs

The ordered pairs (a, b) and (c, d) are equal if and only if a = c and b = d

Order does matter

## Cartesian Product

The Cartesian Product of two sets A and B, denoted by A × B is the set of ordered pairs (a, b) where a ∈ A and b ∈ B

A * B = {(a, b) | a ∈ A ∧ b ∈ B}

> Example: 
>
> A = {a, b} and B = {1, 2, 3}
>
> A × B = {(a, 1), (a, 2), (a, 3), (b, 1), (b, 2), (b, 3)}

---

> ### relation
>
> A subset R of the Cartesian product A × B is called a relation from the set A to the set B
>
> A relation from a set A to itself is called a relation on A
>
> A * ø = ø for any set A
---

We use the notation A <sup> 2 </sup> to denote A × A

Similarly A <sup> 3 </sup> = A × A × A and so on...

## Truth Sets of Quantifiers

Given a predicate P and a domain D, we define the truth set of P to be the set of elements in D for which P(x) is true

The truth set of P(x) is denoted by {x ∈ D | P(x)}

## Boolean Algebra

Propositional calculus and set theory are both instances of an algebraic system called a Boolean Algebra

As always there must be a universal set U. All sets are assumed to be subsets of U

## Set Operations

methodes you can apply on sets to get new set

Most commonly used set theory operations are:
- Union
- Intersection
- Difference
- Complementation
- Symmetric Difference

## Union

Let A and B be sets. The union of the sets A and B, denoted by A ∪ B, is the set

A ∪ B = {x | x ∈ A ∨ x ∈ B}

Set of all unique elements from A and B

## Intersection

The intersection of sets A and B, denoted by A ∩ B, is

A ∩ B = {x | x ∈ A ∧ x ∈ B }

Set of all unique elements in both A and B

## Difference

The difference of A and B, denoted by A – B, is the set containing the elements of A that are not in B

A - B = {x | x ∈ A ∧ x ∉ B }

Set of all unique element that only in A

## Complement

If A is a set, then the complement of the A (with respect to U), denoted by $\overline{A}$ is the set U - A

which means A + $\overline{A}$ = U, or Those elements in the universal set U but not in A

$\overline{A}$ = {x | x ∈ U | x ∉ A}

## Another Interpretation of Set Difference

A - B = {x | x ∈ A ∧ x ∉ B} = A ∩ $\overline{B}$

## The Cardinality of the Union of Two Sets

|A ∪ B| = |A| + |B| − |A ∩ B|

## Symmetric Difference

The symmetric difference of A and B, denoted by A ⊕ B is the set (A - B) ∪ (B - A)

The set of all unique elements from A or B (in A or in B, not both)

Symmetric Difference is different from Complement of Intersection

## Set Identities

---

Identity laws

- A ∪ ø = A
- A ∩ U = A

Domination laws

- A ∪ U = U
- A ∩ ø = ø

Idempotent laws

- A ∪ A = A
- A ∩ A = A

Complementation law

- The completement of $\overline{A}$ is A (markdown cannot display double overline)

---

Commutative laws

A ∪ B = B ∪ A

A ∩ B = B ∩ A

Associative laws

A ∪ (B ∪ C) = (A ∪ B) ∪ C

A ∩ (B ∩ C) = (A ∩ B) ∩ C

Distributive laws

A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

De Morgan’s laws

$\overline{A ∪ B}$ = $\overline{A}$ ∩ $\overline{B}$

$\overline{A ∩ B}$ = $\overline{A}$ ∪ $\overline{B}$

Absorption laws

A ∪ (A ∩ B) = A 

A ∩ (A ∪ B) = A 

Complement laws

A ∪ $\overline{A}$ = U

A ∩ $\overline{A}$ = ø

---

## Proving Set Identities

Venn diagrams “proofs” are considered informal

Different ways to formally prove set identities:

1. prove both sets are subset of the other
2. Use set builder notation and propositional logic to transform one side of the identity to the other
3. Membership Tables: Verify that elements in the same combination of sets always either belong or do not belong to the same side of the identity. Use 1 to indicate it is in the set and a 0 to indicate that it is not

## Membership Table

similar with truth table, proof by giving all posible values

1 indicate the element belong to the table, 0 indeciate not

| A   | B   | A ∩ B | A ∪ B |
| --- | --- | ----- | ----- |
| 1   | 1   | 1     | 1     |
| 1   | 0   | 0     | 1     |
| 0   | 1   | 0     | 1     |
| 0   | 0   | 0     | 0     |

## Generalized Unions and Intersections

Let A <sub> 1 </sub>, A <sub> 2 </sub> ,…, A <sub> n </sub> be an indexed collection of sets.

<sup> <sup> <sup> n </sup> </sup> </sup> ∪ <sub> <sub> <sub> i = 1 </sub> </sub> </sub> A <sub> i </sub> = A <sub> 1 </sub> ∪ A <sub> 2 </sub> ∪ ... A <sub> n </sub>

<sup> <sup> <sup> n </sup> </sup> </sup> ∩ <sub> <sub> <sub> i = 1 </sub> </sub> </sub> A <sub> i </sub> = A <sub> 1 </sub> ∩ A <sub> 2 </sub> ∩ ... A <sub> n </sub>

These are well defined, since union and intersection are
associative.

For i = 1,2,…, let A <sub> i </sub> = {i, i + 1, i + 2, …}. Then,

<sup> <sup> <sup> n </sup> </sup> </sup> ∪ <sub> <sub> <sub> i = 1 </sub> </sub> </sub> A <sub> i </sub> = A <sub> 1 </sub>

<sup> <sup> <sup> n </sup> </sup> </sup> ∩ <sub> <sub> <sub> i = 1 </sub> </sub> </sub> A <sub> i </sub> = A <sub> n </sub>

## Multisets

A multiset (short for multiple-membership set) is an unordered collection of elements where an element can occur as a member more than once

(a set with some duplicated elements)

Multisets use a similar notation as sets but for each element we also list its multiplicity i.e. the number of times it occurs

e.g. {4 . a, 1 . b, 3 . c} (there are 4 a, 1 b and 3 c in this set)

The cardinality of a multiset is defined to be the sum of the multiplicities of its elements

(sum of the all elements, inclluding duplicated)

## Multiset Operations

- The union of the multisets P and Q (P ∪ Q) is the multiset in which the multiplicity of an element is the maximum of its multiplicities in P and Q

- The intersection of P and Q (P ∩ Q) is the multiset in which the multiplicity of an element is the minimum of its multiplicities in P and Q

- The difference of P and Q (P − Q) is the multiset in which the multiplicity of an element is the multiplicity of the element in P less its multiplicity in Q unless this difference is negative, in which case the multiplicity is 0

- The sum of P and Q (P + Q) is the multiset in which the multiplicity of an element is the sum of multiplicities in P and Q

> Example: 
>
> Suppose that P and Q are the multisets {4 ⋅ a, 1 ⋅ b, 3 ⋅ c} and {3 ⋅ a, 4 ⋅ b, 2 ⋅ d}, respectively. Find P ∪ Q, P ∩ Q, P − Q, and P + Q.
>
> P ∪ Q = {max(4, 3) ⋅ a, max(1, 4) ⋅ b, max(3, 0) ⋅ c, max(0, 2) ⋅ d} = {4 ⋅ a, 4 ⋅ b, 3 ⋅ c, 2 ⋅ d}
>
> P ∩ Q = {min(4, 3) ⋅ a, min(1, 4) ⋅ b, min(3, 0) ⋅ c, min(0, 2) ⋅ d} = {3 ⋅ a, 1 ⋅ b, 0 ⋅ c, 0 ⋅ d} = {3 ⋅ a, 1 ⋅ b}
>
> P − Q = {max(4 − 3, 0) ⋅ a, max(1 − 4, 0) ⋅ b, max(3 − 0, 0) ⋅ c, max(0 − 2, 0) ⋅ d} = {1 ⋅ a, 0 ⋅ b, 3 ⋅ c, 0 ⋅ d} = {1 ⋅ a, 3 ⋅ c}
> 
> P + Q = {(4 + 3) ⋅ a, (1 + 4) ⋅ b, (3 + 0) ⋅ c, (0 + 2) ⋅ d} = {7 ⋅ a, 5 ⋅ b, 3 ⋅ c, 2 ⋅ d}

## Functions

Let A and B be nonempty sets. A function f from A to B, denoted f: A → B is an assignment of each element of A to exactly one element of B. We write f(a) = b if b is the unique element of B assigned by the function f to the element a of A

Functions are sometimes called mappings or transformations

A function f: A → B can also be defined as a subset of
A × B (a relation). This subset is restricted to be a relation
where no two elements of the relation have the same
first element

Specifically, a function f from A to B contains one, and
only one ordered pair (a, b) for every element a ∈ A

(function is an one to one mapping relationship)

Given a function f: A → B:

- We say f maps A to B or f is a mapping from A to B
- A is called the domain of f
- B is called the codomain of f
- If f(a) = b,
  - then b is called the image of a under f
  - a is called the preimage of b
- The range of f is the set of all images of points in A under f. We denote it by f(A)

<img src = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Domain%2C_Range%2C_Codomain.svg" style="background-color:#FFFFFF">

Two functions are equal when they have the same domain, the same codomain and map each element of the domain to the same element of the codomain

## Domain, Codomain and Range

domain: what may comes in 

codomain: what may comes out

range: what actually comes out

## Representing Functions

Functions may be specified in different ways

1. An explicit statement of the assignment. Students
and grades example
2. A formula f(x) = x + 1
3. A computer program

## image

image of a is b means f(a) = b, where b is image and a is pre-image

income is image, outcome is pre-image

## Question on Functions and Sets

if S is a subset of A, s belongs to S, B is codomain of A, then F(s) is a subset of B

because s must fall in A, so F(x) must fall in B

## Increasing and Decreasing Functions

> ---
> 
> increasing function: increasing if 
>
> ∀ x <sub> 1 </sub> ∀ x <sub> 2 </sub>(x <sub> 1 </sub> < x<sub> 2 </sub> → f (x <sub> 1 </sub>) ≤ f (x <sub> 2 </sub>))
> 
> this may have somewhere horizontal
> 
> ---
>
> strictly increasing function: increasing if 
> ∀ x <sub> 1 </sub> ∀ x <sub> 2 </sub>(x <sub> 1 </sub> < x<sub> 2 </sub> → f (x <sub> 1 </sub>) < f (x<sub> 2 </sub>))
> 
> no horizontal line, if x <sub> 1 </sub> > x <sub> 2 </sub>, then f(x <sub> 1 </sub>) is always larger than f(x <sub> 2 </sub>)
>
> ---
> decreasing function and strictly decreasing function are the reverse

## Injection

Injection is also called one-to-one, which means for each value in domain will always has it unique image in range. (if f(a)== f(b), then a == b)

## Surjection

Surjections means a function's codomain is equal to it's range, it is also called onto

## Bijection

A function that is both Injection and Surjection

## showing function is injection or surjection

Example:

Suppose that f : A → B

injective: show that if f(x)== f(y), then x == y

surjective: show that for any x in codomin, there is a y in domain such that f(y)== x

> f(x) = 4x - 1 show one-to-one and onto

> one-to-one:
>
> 4a - 1 = 4b - 1
>
> 4a = 4b
>
> a = b

> onto:
>
> assume there is a y such that y = 4x - 1
>
> y - 1 = 4x
>
> x = (y - 1) / 4
>
> There exist a function to project y to x, so it is surjective

> book example:
>
> Solution: 
>
> Part 1 (scratch work) 
>
> Let us pick an arbitrary number y ∈ R in the codomain  If such a number exists, 
>
> 2x - 3 =   y   2x = y + 3   x = (y + 3)/2 
>
> Part 2 (actual solution)  Let y ∈ R be an arbitrary element from the codomain 
>
> Let  x = (y + 3)/2 
>
> f(x) = 2((y + 3)/2)-3 = y + 3 -3 = y  An arbitrary element from the codomain has a preimage in the domain  ∴ f(x) = 2x -3, from R to R, is surjective
>

## Inverse function

All inverse functions are bijective

Let function be f, then the inverse function of it is f <sup>-1 </sup>

f(x) = y iff f <sup>-1 </sup>(y) = x

inverse function is the projection from image to pre-image

All bijective functions are inversible

## Composition

let f from B to C, g from A to B, then the composition of f with g denote as f ∘ g is the function form A to C defined by f ∘ g = f(g(x))

the inner function will be calculated first

## Floor and Cell function

Floor function return the largest integer that less than or equal to x

Celling function return the smallest integer that larger than or equal to x

> ⌊ 4.5 ⌋ = 4, ⌊-4.5 ⌋ = -5
>
> ⌈ 4.5 ⌉ = 5, ⌈-4.5 ⌉ = -4

## properties of flooring and celling functions

> n is a integer, and x is a real number
>
> 1. ⌊ x ⌋ = n iff n <= x < n + 1
> 2. ⌈ x ⌉ = n iff n - 1 < x <= n
> 3. ⌊ x ⌋ = n iff x - 1 < n <= x
> 4. ⌈ x ⌉ = n iff x <= n < x + 1
> 5. x - 1 < ⌊ x ⌋ <= x <= ⌈ x ⌉ < x + 1
> 6. ⌊ -x ⌋ = -⌈ x ⌉
> 7. ⌈ -x ⌉ = -⌊ x ⌋
> 8. ⌊ x + n ⌋ = ⌊ x ⌋ + n
> 9. ⌈ x + n ⌉ = ⌈ x ⌉ + n

## Proving properties of functions

prove if x is a real number, then ⌊ 2x ⌋ = ⌊ x ⌋ + ⌊ x + 1/2 ⌋ 

let x = n + ε, where n is an integer and 0 ≤ ε < 1. 

case 1: ε < 1/2

> ⌊ 2x ⌋ = ⌊ 2n + 2 ε ⌋ = 2n since ε < 1/2
>
> ⌊ x ⌋ + ⌊ x + 1/2 ⌋ = ⌊ n + ε ⌋ + ⌊ n + ε + 1/2 ⌋ = n + n since ε < 1/2 and correspondingly ε + 1/2 < 1
>

case 2: ε >= 1/2

> ⌊ 2x ⌋ = ⌊ 2n + 2 ε ⌋ = 2n + 1 since ε >= 1/2
>
> ⌊ x ⌋ + ⌊ x + 1/2 ⌋ = ⌊ n + ε ⌋ + ⌊ n + ε + 1/2 ⌋ = n + (n + 1) since ε > 1/2 and correspondingly ε + 1/2 > 1

## Factorial function

f: N → Z+ , denoted by f(n) = n! is the 
product of the first n positive integers when n is a 
nonnegative integer. 

f(n) = 1 * 2 * 3 ... * n

f(0) = 0! = 1

f(1) = 1! = 1

## Partial function

A partial function from A → B is a assignment of each element in subset of A to B, which means not every element in domain is used.

for example, f: Z → R, f(x) = $\sqrt{x}$ is a partial function beacause f(x) is undefined when x is negative

## Sequences and Summations

Sequaences are ordered lists of elements

> Example:
>
> 1,2,3,5,8...
>
> 1,3,9,27,81...

The notion of position is important in sequences.  
It is the index at which a certain value appears in 
the sequence

## Formal defination of sequences

A sequence is a function from a subset of the integers (usually {1,2,3...} or {0,1,2,3...})to a set S

The notation a <sub> n </sub> is used to denote the image of the integer n. 

## Types of sequences

> ### Geometric Progression:
>
> A geometric progression is a sequence of the form a, ar, ar <sup> 2 </sup>, ..., ar <sup> n </sup>, ...
>
> where the initial term a and the common ratio r are real numbers

> ### Arithmetic Progression
>
> A arithmetic progression is a sequence ofform a, a + d, a + 2d , ..., a + nd, ...
>
> where the initial term a and the common difference d are real numbers

## Summations

Sume of the term a <sub> m </sub>, a <sub> m+1 </sub>, ... , a <sub> n </sub>, 

> Notation: $\sum_{i=m}^{n} a_i$
>
>(starting from a <sub> m </sub> stop at a <sub> n </sub>)

## Geometric Series

> Sum of terms of germetric progressions:
>
> $\sum_{j = 0} ^ {n} ar^j$ = $\frac{ar ^ {n + 1} - a}{r - 1}$ when r ≠ 1
>
> $\sum_{j = 0} ^ {n} ar^j$ = ${(n + 1) a}$ when r = 1

## Some Useful Summation formulae

| Sum                                       | Closed Form                             |
| ----------------------------------------- | --------------------------------------- |
| $\sum_{j = 0} ^ {n} ar^j$ (r ≠ 1)         | $\frac{ar ^ {n + 1} - a}{r - 1}$, r ≠ 1 |
| $\sum_{j=0}^{n} j$                        | $\frac{n(n+1)}{2}$                      |
| $\sum_{j=0}^{n} j^2$                      | $\frac{n(n+1)(n+2)}{6}$                 |
| $\sum_{j=0}^{n} j^2$                      | $\frac{n^2(n+1)^2}{4}$                  |
| $\sum_{j=0}^{\infty} x^j$, $\|x\|<1$      | $\frac{1}{1-x}$                         |
| $\sum_{j=0}^{\infty} jx^{j-1}$, $\|x\|<1$ | $\frac{1}{(1-x)^2}$                     |

# chapter 3

## Problems and Algorithms

We then solve the general problem by specifying 
the steps of a procedure that takes a valid input 
and produces the desired output. This 
procedure is called an algorithm. 

Definition: 
> An algorithm is a finite set of precise instructions for 
performing a computation or for solving a problem. 

Human understable words:
> The steps of a general question to get desired out put from any vaild input