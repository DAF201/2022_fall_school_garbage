# chapter 1

## Propositions

proposition is a claim that can only be true or false

## propositional variables

propositional variables is a symbol that denote a case. For example, p denotes ground is wet.

Each propositional variable has a truth value T or F

Proposition can be <b>Atomic</b> or <b>Compound</b>

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

This table shows all the posiable cases and result of the proposition p∧q

## Negation

Means opposite: 

p = T, then ¬p = F

## AND

Only be true when both are true, otherwise false.

p = T, q = T, p ∧ q = T

p = T, q = F, p ∧ q = F

## OR

Only be false when both are false, otherwise true.

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

Only return false when case 1 is true, case 2 is false. Also known as <b>if ...  then ...</b>

p = T, q = T, p → q = T

p = T, q = F, p → q = F

p = F, q = T, p → q = T

p = F, q = F, p → q = T

> ### Vacuous Truth
> when the case 1 is false, no matter what is the truth value of case 2, the output is true, because we cannot make any conclusion when case 1 is false, so we assume the claim is true.

## Converse, Contrapositive, and Inverse

From p → q we can form new conditional statements .

q → p is the converse of p → q

¬p → ¬q is the inverse of p → q

¬q → ¬p is the contrapositive of p → q

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
>If I do not work hard then I will fail the exam

## Tautologies, Contradictions, and Contingencies

Tautologies: something always true, example p ∨ ¬p

Contradictions: something always false, example p ∧ ¬p

Contingency: something neither Tautologies or Contradictions, example p ⇔ q

## Logical Equivalences

Means the propositions have the exactly same results, denote by ≡
| Law                 | proposition                                                       |
| ------------------- | ----------------------------------------------------------------- |
| Identity Laws       | p ∧ T ≡ p, p ∨ F ≡ p                                              |
| Domination Laws     | p ∨ T ≡ T, p ∧ F ≡ F                                              |
| Idempotent laws     | p ∧ p ≡ p, p ∨ p ≡ p                                              |
| Double Negation Law | ¬(¬p) ≡ p                                                         |
| Negation Laws       | p ∨ ¬p ≡ T, p ∧ ¬p ≡ F                                            |
| Commutative Laws    | p ∨ q ≡ q ∨ p, p ∧ q ≡ q ∧ p                                      |
| Associative         | (p ∧ q) ∧ r ≡ p ∧ (q ∧ r), (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)              |
| Distributive Laws   | (p ∧ q) ∨ r ≡ (p ∨ r) ∧ (q ∨ r) , (p ∨ q) ∧ r ≡ (p ∧ r) ∨ (q ∧ r) |
| Absorption Laws     | p ∨ (p ∧ q) ≡ p, p ∧ (p ∨ q) ≡ p                                  |
| De Morgan's Laws    | ¬(p ∨ q) ≡ ¬p ∧ ¬q , ¬(p ∧ q) ≡ ¬p ∨ ¬q                           |
| Nameless            | p → q ≡ ¬p ∨ q                                                    |
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

>P1: If John eats peanuts, he falls sick
>
>P2: John did not eat peanuts
>
>---
>
>∴ John did not fall sick

Does ((p → q) ∧ ¬p) → ¬q?

| p   | q   | ((p → q) ∧ ¬p) | ¬q  |
| --- | --- | -------------- | --- |
| F   | T   | T              | F   |

premises is True ((p → q) ∧ ¬p), but conclusion is False (¬q), so this is a fallacy

## Argument Forms

>P1: If John eats peanuts, he falls sick
>
>P2: John did not fall sick
>
>---
>
>∴ John did not eats peanuts

>P1: If you work hard, you will get a good raise
>
>P2: You did not get a good raise
>
>---
>
>∴ You did not work hard

Even those two arguements are different, the have the same form which is ((p → q) ∧ ¬q) → ¬p

When two arguements have the same arguement form, they:

1. Have the same symbolic representation
2. Belong to the same “family” of arguments

## Important Rules of Inference

| Rules of Inference                     | Tautology                     | Name                   |
| -------------------------------------- | ----------------------------- | ---------------------- |
| p<br>p → q<br>-------<br>∴ q           | (p ∧ (p → q)) → q             | Modus ponens           |
| ¬q<br>p → q<br>-------<br>∴ ¬p         | (¬q ∧ (p → q)) → ¬p           | Modus tollens          |
| p → q<br>q → r<br>-------<br>∴ r       | ((p → q) ∧ (q → r)) → (p → r) | Hypothetical Syllogism |
| p ∨ q<br>¬p<br>-------<br>∴ q          | (¬p ∧ (p ∨ q)) → q            | Disjunctive Syllogism  |
| p<br>-------<br>∴ p ∨ q                | p → (p ∨ q)                   | Addition               |
| p ∧ q<br>-------<br>∴ p                | (p ∨ q) → p                   | Simplification         |
| p<br>q<br>-------<br>∴ p ∧ q           | ((p) ∧ (q)) → p ∧ q           | Conjunction            |
| p ∨ q <br>¬p ∨ r<br>-------<br>∴ q ∨ r | ((¬p ∨ r) ∧ (p ∨ q)) → q ∨ r  | Resolution             |

## Comparing the Tautologies for Logical Equivalences and Rules of Inference

> ### Logical Equivalences
> 
> Logical_Expression1 ⇔ Logical_Expresion2 is a tautology

> ### Rules of Inference
> 
> Conjunction_of_premises → Conclusion is a tautology

## Fallacies

1. Fallacy of affirming the conclusion
<br>p → q<br>q<br>-------<br>∴p<br>cannot get premises from conclusion

2. Fallacy of denying the hypothesis
<br>p → q<br>¬p<br>-------<br>∴¬q<br>Vacuous truth

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

Expressions with variables are not propositions and therefore do not have truth values. For example: <br>P(x) → P(y)

When used with quantifiers (at least one, all), these expressions (propositional functions) become propositions

Propositional functions can have multiple variables

## Quantifiers

The "degree" of "Being True" of a propositional function over a range of elements (from the pertinent domain)

There are two types of them: 

1. Universal Quantifier, “For all,”, ∀
2. Existential Quantifier, “There exists,”, ∃

## Uniqueness Quantifier

∃!x P(x) means that P(x) is true for one and only one x in the universe of discourse

"There is a unique x such that..."

## Trailing Quantifiers

Additional information at the end of the sentense

Example: ∀x ∈ R , x<sup>2</sup> ≥ 0(x is a real number and x<sup>2</sup> is not 0)

this will include all real number but 0

## Bound and Free Variables

when an variable has something to do with the quantifier, we say it is bound, otherwise, we say it is free.

Example: ∃x(x + y = 1), in this case, x in bound and y is free

## quantifer, propositional function, and proposition

Quantifiers provide an alternate way to convert propositional functions to propositions

Example: Let P(x) be the propositional function “x + 1 > x”. Then ∀x P(x) is a proposition

## ways to make propositional function a proposition

In general, all the variables that occur in a propositional function must be bound or set equal to a particular value to turn it into a proposition

- universal quantifiers

- existential quantifiers

- value assignments

## Properties of Quantifiers

The truth value of x P(x) and  x P(x) depend on both the propositional function P(x) and on the domain U

If the domain is empty, for any propositional function:

- ∀xP(x) is true

- ∃xP(x) is false

## Truth Set

A truth set is a set contains all values of x that make the proposition true.

Example, P(x):"x is a factor of 8", Domain:all positive integers

Then the truth set of P(x) is {1,2,4,8}

## Quantifiers Over Finite Domains

∀xP(x) ≡ P(x1) ∧ P(x2) ∧ P(x3) ∧ … ∧ P(xn)

Conjunction of propositions

∃xP(x) ≡ P(x1) ∨ P(x2) ∨ P(x3) ∨ … ∨ P(xn)

Disjunction of propositions

## Quantifiers with Restricted Domains

Sometimes it is not feasible to enumerate the domain of a quantifier. Then we use the excluding method to exclude those we don't want out.

In such instances, an abbreviated notation is often used

- a condition a variable must satisfy is included after the quantifier

- Such quantifiers are called restricted quantifiers

Example:

(∀x)<sub>x < 0</sub> (x<sup>2</sup> > 0)

means for all x such that x smaller than 0, we have x to the power of 2 is greater than 0

## Precedence of Quantifiers

The ∀ and ∃ have higher precedence than any logical operator.

which means ∀x P(x) ∨ Q(x) means (∀x P(x)) ∨ Q(x) instead of ∀x (P(x) ∨ Q(x))

## Equivalences in Predicate Logic

have the save value for every possible result.

cover every domain

Example: 

∀x ¬¬S(x) ≡ ∀x S(x)

∀x(P(x) ∧ Q(x)) ≡ ∀x P(x) ∧ ∀x Q(x)

Assume ∀x(P(x) ∧ Q(x)) is True, then P(x) ∧ Q(x) is true for every value of x in domain, so P(x) and Q(x) are True for every value in domain

Assume ∀x P(x) ∧ ∀x Q(x) is True, then P(x) and Q(x) are True for every value of x in domain

So they are equivalent

## Some equivalences and not equivalences

1. ∀x ¬¬S(x) ≡ ∀x S(x)

2. ¬∀x P(x) ≡ ∃x ¬P(x)

3. ¬∃x P(x) ≡ ∀x ¬P(x)

4. ∀x(P(x) ∧ Q(x)) ≡ ∀x P(x) ∧ ∀x Q(x)

5. ∃x(P(x) ∨ Q(x)) ≡ ∃xP(x) ∨ ∃xQ(x)

6. ∀x(P(x) ∨ Q(x)) ¬≡ ∀xP(x) ∨ ∀xQ(x)

7. ∃x(P(x) ∧ Q(x)) ¬≡ ∃xP(x) ∧ ∃xQ(x)

The Universal quantifier cannot be distributed over disjunction, and the existential quantifier cannot be distributed over conjunction

## De Morgan’s Laws for Quantifiers

| Negation | Equivalent Statement | When Is Negation True?         | When Is False                 |
| -------- | -------------------- | ------------------------------ | ----------------------------- |
| ¬∃x P(x) | ∀x ¬P(x)             | For every x, P(x) is false     | There is x which P(x) is true |
| ¬∀x P(x) | ∃x ¬P(x)             | There is x which P(x) is false | P(x) is true for every x      |

## Restricted Quantifiers

Unrestricted quantifiers apply to the entire domain of discourse

A restricted quantifier has the same semantics as an unrestricted quantifier except that the variables in the domain must satisfy a certain condition in order for the quantification to apply

(Which means we only focus on the values in the domain which satisfies the restriction)

Example: 

(∀x)<sub>x < 0</sub> (x<sup>2</sup> > 0)

for every x in real numbers, if x is smaller than 0, then we have x to the power of 2 is larger than 0.

## Restricted quantifer -> Unrestricted quantifer

Sometimes we need to express a restricted quantifier as an unrestricted quantifier

∃x <sub>P(x)</sub> Q(x) ≡ ∃x (P(x) ∧ Q(x))

∀x <sub>P(x)</sub> Q(x) ≡ ∀x (P(x) → Q(x))

## Nested Quantifiers

In nested quantifiers one quantifier is within the scope of another quantifier

Example: Every real number has an inverse

∀x∃y(x + y = 0)

## Order of Quantifiers

The order of the nested quantifiers is important, unless all the quantifiers are universal quantifiers or all are existential quantifiers

## Quantifications of Two Variables

| Statement                | When True?                                                    | When False?                                         |
| ------------------------ | ------------------------------------------------------------- | --------------------------------------------------- |
| ∀x∀yP(x,y)<br>∀y∀xP(x,y) | P(x,y) is true for every pair of x and y                      | when any pair of x, y make P(x,y) false             |
| ∀x∃yP(x,y)               | For every x, there is an y such that P(x,y) is true           | when there is a x for every y P(x,y) is false       |
| ∃x∀yP(x,y)               | There is at least one x such that for every y, P(x,y) is true | for every x, there is a y such that P(x,y) is false |
| ∃x∃yP(x,y)<br>∃y∃xP(x,y) | There is a pair of x and y such that                          | for every pair of x and y, P(x,y) is false          |

## Two Surprising Results

if ∃y∀xP(x,y) is true, then ∀x∃yP(x,y) must be also true

if ∀x∃yP(x,y) is true, it is not necessay for ∃y∀xP(x,y) to be true

## Additional Rules of Inference for Quantified Statements

| Rule of Inference                                                  | Name                       |
| ------------------------------------------------------------------ | -------------------------- |
| ∀xP(x)<br>------<br>∴P(c)                                          | Universal instantiation    |
| P(c) for an arbitary of c <br>-------------------------<br>∴∀xP(x) | Universal generalization   |
| ∃xP<br>-------------------------<br>∴P(c) for some element c       | Existential instantaion    |
| P(c) for some element c<br>-------------------------<br>∴∃xP       | Existential generalization |

x: Unspecified member of the domain

c: Specific member of the domain

## Using Rules of Inference

"All men has two legs", "John is a man", shows John has two legs

let M(x) represents "x is a man", and L(x) represents "x has two legs"

premises: ∀x(M(x) → L(x)), M(John)

∀x(M(x) → L(x))<br>----------------<br>∴M(John) → L(John)

M(John) → L(John)<br>M(John)<br>--------------------<br>∴L(John)

## Universal Modus Ponens

Combines UI and Modus Ponens

∀x(P(x) → Q(x))<br>P(c)<br>-----------------<br>∴Q(c)

## Universal Modus Tollens

∀x(P(x) → Q(x))<br>¬Q(c)<br>-----------------<br>∴¬P(c)

## Proofs of Mathematical Statements

A proof is a valid argument that establishes the truth of a statement.

A theorem is a statement that can be shown to be true using:

- definitions

- other theorems

- axioms (statements which are given as true, also known as postulates)

- rules of inference

A lemma is a ‘helping theorem’ or a result which is needed to prove a theorem.

A corollary is a result which follows directly from a theorem.
Less important theorems are sometimes called propositions

A conjecture is a statement that is being proposed to be true. Once a proof of a conjecture is found, it becomes a theorem. It may turn out to be false.

## Direct Proof

A direct proof shows that a conditional statement p → q is true by showing that if p is true, then q must also be true

We assume that p is true and use axioms, definitions, and previously proven theorems, together with rules of inference, to show that q must also be true.

Example:

Proof the square of a odd number is also an odd number

any odd number : 2n+1

(2n + 1)<sup>2</sup> = 4n<sup>2</sup> + 4n + 1 = 2 * (n<sup>2</sup> + 2n) + 1

let r = (n<sup>2</sup> + 2n), therefore (2n + 1)<sup>2</sup> = 2r + 1, and because of 2r is an even number, so 2r + 1 is an odd number.

## Proof By Contraposition

Sometimes it is easier to prove theorems using proof by contraposition

- the conditional statement p → q is proved by showing that its contrapositive, ¬q → ¬p is true

Example: Prove that if n is an integer and 3n + 2 is odd, then n is odd.

let n = 2k for some integer k

the 3n + 2 = 6k + 2 = 2(3k + 1)

let j = 3k + 1 for some integer j

so 3n + 2 = 6k + 2 = 2j

so 3n + 2 is even

Since we have shown ¬q → ¬p , p → q must hold as well. We have proved by contraposition that if 3n + 2 is odd, then n is odd

## Vacuous & Trivial Proofs

- p → q ≡ ¬p ∨ q

- A proof that makes use of the fact that p → q must be true when p is false is called a vacuous proof

- A proof that makes use of the fact that p → q must be true when q is true is called a trivial proof

- These proofs are never treated as complete proofs but they are used in conjunction with other proof techniques (like proof by cases and mathematical induction) to establish that special cases of a theorem are not in violation of the generalized theorem

## Proof by Contradiction

We make a opposite proof of if p is true, then q is false for p → q. Clearly, therefore, the assumption that if p is true then q is false is wrong. In other words, if p is true then q must be true.

Example: 

Prove that if you pick 22 days from the calendar, at least 4 must fall on the same day of the week.

Assume that no more than 3 of the 22 days fall on the same day of the week. Because there are 7 days of the week, we could only have picked 21 days. This contradicts the assumption that we have picked 22 days.

## Background Information
- Fundamental theorem of arithmetic (also called the unique factorization theorem)

> Every number is a prime or a unique product of primes

## Theorems that are Biconditional Statements

To prove a theorem that is a biconditional statement, that is, a statement of the form p ⇔ q, we show that p → q and q → p are both true.

Example:

Prove the theorem: “If n is an integer, then n is odd if and only if n2 is odd.”

Solution: 

We have already shown (previous slides) that both p → q and q → p. Therefore we can conclude p ⇔ q.

## Proof By Counterexample

Statements of the form ∀xP(x) can be proved to be false by providing a counterexample ∃x(¬P(x))

Example: Show that the statement “Every positive integer is the sum of the squares of two integers” is false.

The number 3 can be represented as the sum of two numbers in one of two ways (order being immaterial)

3 = 0 + 3 = 0<sup>2</sup> + 3

3 = 1 + 2 = 1<sup>2</sup> + 2

In neither case can be number 3 be represented as a sum of two squares.
Therefore we have proved by counterexample that “Every positive integer is the sum of the squares of two integers” is false.

## Mistakes in proofs

- performing a disallowed mathematical operation (divide by 0)

- given p → q is true and q is true implying the conclusion that p is true(q can be True when p is False)

- given p → q is true and p is false implying the conclusion that q is false(q is true)

- basing one or more steps of the proof on the truth of the statement being proved, or a statement equivalent to it (begging the question or circular reasoning)

## What is wrong with this

“Proof” that 1 = 2

1. a = b
2. a<sup>2</sup> = a * b
3. a<sup>2</sup> - b<sup>2</sup> = a * b - b<sup>2</sup>
4. (a - b)(a + b) = b(a - b)
5. a + b = b
6. 2b = b
7. 2 = 1

Solution: step 5, divide both side by (a - b), (a - b) = 0, it is dividing both side by 0 which is undefined

## If direct methods of proof do not work

- We may need a clever use of a proof by contraposition.

- Or a proof by contradiction.

## Proof by Exhaustion

Used in situations where theorems can be proved by examining a relatively small number of examples

(list all cases and proof they are true)

Example: 

> Prove that (n + 1)3 ≥ 3n if n is a positive integer with n ≤ 4.
>
>----
>
>solution:
>
>Case n = 1: (1 + 1)3 = 23 = 8, which is ≥ 31 i.e. 3
>
>Case n = 2: (2 + 1)3 = 33 = 27, which is ≥ 32 i.e. 9
>
>Case n = 3: (3 + 1)3 = 43 = 64, which is ≥ 33 i.e. 27
>
>Case n = 4: (4 + 1)3 = 53 = 125, which is ≥ 34 i.e. 81

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
>¬(p1 ∨ p2 ∨ p3 ... ∨ pn) ∨ q ≡ (¬p1 ∧ ¬p2 ∧ ¬p2 ∧ ¬p3 ... ∧ ¬pn) ∨ q
>
>(¬p1 ∧ ¬p2 ∧ ¬p2 ∧ ¬p3 ... ∧ ¬pn) ∨ q ≡ (¬p1 ∨ q) ∧ (¬p2 ∨ q) ∧ (¬p3 ∨ q) ... ∧ (¬pn ∨ q)
>
>(¬p1 ∨ q) ∧ (¬p2 ∨ q) ∧ (¬p3 ∨ q) ... ∧ (¬pn ∨ q) ≡ (p1 → q) ∧ (p2 → q) ∧ (p3 → q) ... ∧ (pn → q)

Use the tautology

(p1 ∨ p2 ∨ p3 ... ∨ pn) → q ⇔ (p1 → q) ∧ (p2 → q) ∧ (p3 → q) ... ∧ (pn → q)

Each of the implications p<sub>n</sub> → q is a case.

----

Example:

>Prove that Prove that if n is an integer, then n<sup>2</sup> ≥ n.
>
>Case 1 : n = 0, then n<sup>2</sup> = 0, which n<sup>2</sup> >= n
>
>Case 2 : n <= 1, then n<sup>2</sup> >= n or n <sup>2</sup> = n = 1
>
>Case 3: n >= 1, then n<sup>2</sup> > n
>
>Since the inequality n<sup>2</sup> ≥ n holds in all three cases, we can conclude that if n is an integer, then n<sup>2</sup> ≥ n.

## Without Loss of Generality

The phrase “Without Loss of Generality” (WLOG) is used in proofs with cases to assert that by proving one case of a theorem, no additional argument is required to prove other specified cases

( Standary english: this case can represent any other cases, so I dont need to prove other cases )

