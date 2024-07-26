# RDF Model Requirements Specification

## Term sheet

- Data Architecture:     Class Layer   Thought Layer  Model Layer
  - FG/Flow Graph:       Node          Edge           MG/Model Graph
  - CG/Class Graph:      Entity        Predicate      CMG/Class Model Graph
  - TG/Thought Graph:    Thought       Relation       => RDF Export
- Processtion: Edit-Time           Run-Time
  - Canvas     Flow - 
  - End-Node        -> CG -> MG -
  - Tbl                         -> TG
  
## Flow => CG/Class Graph

- Flow               -> CG
- think step node    -> an Edge(named step name)
- text entity        -> a Node(named entity name)
- list entity        -> a Node(named entity name)
- TODO: 4th node
- dict entity        -> a Node(named entity name), 
-                       some Nodes(named entity-key-name), 
-                       some Edges(named has_property)
- Entity Color: unique entity color in a Class Graph
- All nodes in CG are either value or value list. 
- Dict node is a value-combinated list(should be a brother node of all key nodes)
- Every end-node may has a different CG
- TODO: Think step node can have multiple in flow? 

## CG/Class Graph => MG/Class Model Graph

- MG Diff Codes: Diff ops ordered-list on CG
  - Add Predicate: entity_from.key, new_pred, entity_to.key
  - Del Predicate: old_pred
  - Merge Predicate: pred1, pred2 (named pred1 + pred2, Don't delete pred1 or pred2)
  - Add Entity: TODO
  - Del Entity: TODO
  - Ref Entity: TODO
- MG Diff Actions
  - Delete Entity: del entity, merge predicates 
  - Add Predicate: add predicate
  - Del Predicate: del predicate
- Predictable Nodes Pair(pred can store index relastion for acceleration TG generation)
  - value node <-> value node
  - list node <-> value node
  - reasonable list node -> list node
  - dict key1 node <-> dict key2 node

## MG/Model Graph Define (Tree MG & Knowledge MG)

- A chain can define multiple MGs with same MG type.
- Knowledge MG Diff is a empty list. the CG is same with MG.
- MG Diff list is a codes ordered list. 
- Every end-node must define all of MG which the chain declared.
- Define MG Diff List in every End-Node.
- A new diff in a end-node also appears in other end-nodes, but is disabled by default.
- Every MG type has an Edit-time Checker vs Run-time Checker
- Layout
  - CG of a end-node
  - MG action
  - MG Diff Codes List(enable | code)
  - MG of a end-node
  
## Tbl => TG/Thought Graph

- Entity Instancizations: Tbl -> TG
  - text entity        -> Node(named text value, entity color)
  - list entity line   -> Node(named single text value, entity color)
  - dict entity line   -> Node(entity named #ln), Edges(named keyname), Nodes(named value)
  - dict-key line
  - predicate          -> Thought Graph Edges(named predicate name)
- After executing flow, choosing the CG and MG Diff by the end-node and merging the MG
- Every Predicate in MG has a pair of index nodes ref-to Tbl's column.
- Every Entity in MG ref-to a Tbl's column.
- Traversal MG to generater TG
  - TODO: Dict Root Node?
