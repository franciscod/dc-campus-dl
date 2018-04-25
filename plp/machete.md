# Machete
([fuente](https://campus.exactas.uba.ar/course/view.php?id=995&section=13))
---
### [Machete](https://campus.exactas.uba.ar/course/view.php?id=995&section=13)

# Algunas cosas útiles para programar

### Haskell

**Funciones:** foldr, foldl, foldr1, foldl1, map, zipWith, all, any, null,
nub, sort, rem, (++), (!!), head, tail, init, last, length, replicate,
iterate, filter, take, drop, elem, find, isNothing, fromJust, maybe, lookup,
reverse, concat, union, (>>=), span, takeWhile, dropWhile, concatMap, and, or,
sum, max, maximum, min, minimum, (==), (/=), not, ord, chr

Algunas de estas funciones no se encuentran definidas en el preludio, sino en
los módulos List o Maybe. Para usarlas, incluir la(s) línea(s) import
Data.List y/o import Data.Maybe respectivamente en el archivo fuente.

### Prolog

**Predicados:** =, sort, msort, length, nth1, nth0, member, append, last,
between, is_list, list_to_set, is_set, union, intersection, subset, subtract,
select, delete, reverse, atom, number, numlist, sumlist, flatten, help

**Operaciones extra-lógicas:** is, \=, ==, =:=, =\=, >, <, =<, >=, abs, max,
min, gcd, var, nonvar, ground, trace, notrace

**Metapredicados:** bagof, setof, maplist, include, not, forall, assert,
retract, listing

¡Ojo! A excepción del not, el cual está permitido siempre, los metapredicados
no están permitidos para resolver prácticas ni parciales. Sólo son lícitos en
el TP.

### Smalltalk

**Métodos de colecciones:** select:, reject:, collect:, detect:,
detect:ifNone:, inject:into:, fold:, add:, at:, at:put:, do:,
keysAndValuesDo:, keysDo:, valuesAndCountsDo:, withAll:, includes:,
includesKey:

**Clases útiles para metaprogramación:** Object, Message, MessageSend,
Behavior, Class, Metaclass, Method, Context

**Métodos comunes para metaprogramación:** doesNotUnderstand:, compile:,
perform:, respondsTo:, sendTo:, value:, class, species, superclass,
superclass:, isKindOf:,
subclass:instanceVariableNames:classVariableNames:category:, allSubclasses,
allSubclassesDo:, withAllSubclassesDo:, methodDictionary

