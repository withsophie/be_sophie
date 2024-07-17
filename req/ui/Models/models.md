# RDF Model Requirements Specification

## Term sheet

- RDF Model: data exchange formats, Class Layer and Thought Layer
  - Flow Graph:       Node      Edge        Model
  - Class Graph:     Entity   Predicate     Class Translate Model 
  - Thought Graph:   Thought  Relation      Thought Translate Model
  
## Class Graph Translate (from Flow Node and Entity Translate to CG)

- think step    -> Class Graph an Edge(named step name)
- text entity   -> Class Graph a Node(named entity name)
- list entity   -> Class Graph a Node(named entity name)
- dict entity   -> Class Graph a Node(entity named), some Nodes(named entity-key), some Edges(named has_property)
- Entity Color: unique color in one CG

## Class Translate Model (CGM Definition)

- CGM Atom Codes
  - Add Predicate: entity.key <-pred-> entity.key
  - Del Predicate: -pred
  - Merge Predicate: #pred1+pred2 (Don't delete pred1 or pred2)
  - Add Entity: TODO
  - Del Entity: TODO
- CGM Actions
  - Delete Entity: del entity, merge predicates 
  - Add Predicate: add predicate
  - Del Predicate: del predicate

## Thought Grapph Translate (from CG + CGM Translate to TG)

- Merge Class Translate Model
  - exec every CGM on CG, trnaslate to TGM
  - for every TGM translate to TG
- Thought Graph Translate
  - text entity        -> Thought Graph Node(named text value, entity color)
  - list entity line   -> Thought Graph Node(named single text value, entity color)
  - dict entity line   -> Thought Graph Node(entity named #ln), Edges(named keyname), Nodes(named value)
  - predicate          -> Thought Graph Edges(named predicate name)