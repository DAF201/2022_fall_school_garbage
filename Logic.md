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

