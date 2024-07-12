
# Exploring Ambiguity Reduction in Language with AI
> Alex Sudo @ Jul 2024
Since humans began to communicate through language, ambiguity has shadowed us. As soon as the light of expression starts to shine, the concept projected into the other’s consciousness becomes uncontrollable. Whether the initiator can accurately convey their meaning makes the role of the receiver equally important. However, both parties in the communication process seem indifferent to the attenuation of the signal because they rarely verify the transmission's effectiveness afterward. Thus, the profound insights of our ancestors might merely be ancient ambiguities repurposed by later generations in appropriate contexts.

Despite the lies and poetry created by ambiguity, a dedicated group of engineers tirelessly seeks to eliminate ambiguity in language. From the three-way handshake of TCP/IP to Word Sense Disambiguation (WSD) in large language models (LLMs), efforts are made to reduce the signal-to-noise ratio and enhance transmission efficiency. The pursuit of accurate information expression remains a crucial task in communication.

Setting aside human-to-human communication, human-to-AI communication also requires the elimination of ambiguity. Besides AI's own efforts, humans need to employ engineering techniques to mitigate ambiguities caused by their habitual practices. Before addressing this issue, we must carefully analyze the origins of ambiguity.

### Common types of linguistic ambiguity include:

### 1. Lexical Ambiguity
**Types**
- **Homonymy**: Words with the same form but different meanings, e.g., "bank" can mean a financial institution or the side of a river.
- **Homophony**: Words that sound the same but have different meanings, e.g., "bare" and "bear."
- **Polysemy**: Words with multiple related meanings, e.g., "paper" can mean "material" or "academic article."

**Causes**
- **Language Simplification**: Words tend to simplify in form, leading to homonymy and homophony.
- **Historical Evolution**: Words acquire new meanings over time, creating polysemy.
- **Cultural and Social Influences**: Different cultural and social contexts assign different meanings to the same word.

### 2. Syntactic Ambiguity
**Types**
- **Structural Ambiguity**: A sentence’s structure allows multiple interpretations, e.g., "old professor's student" can mean "the professor is old" or "the student is old."
- **Attachment Ambiguity**: The attachment position of a phrase is unclear, e.g., "She saw the man with glasses" can mean "the man wears glasses" or "she wears glasses."

**Causes**
- **Complex Grammar Rules**: The complexity and variety of grammar rules lead to diverse structural interpretations.
- **Phrase and Sentence Construction**: Ambiguous attachment positions in sentence construction create ambiguity.
- **Lack of Syntactic Markers**: The absence of clear syntactic markers (e.g., punctuation) in spoken and written language leads to ambiguity.

### 3. Semantic Ambiguity
**Types**
- **Category Ambiguity**: The category of a word in a sentence is unclear, e.g., "can" can be a verb ("able to") or a noun ("container").
- **Scope Ambiguity**: The scope of quantifiers or negations is unclear, e.g., "All students did not do homework" can mean "every student did not do homework" or "not a single student did homework."

**Causes**
- **Semantic Polysemy**: Words have multiple semantic interpretations, leading to ambiguity.
- **Complex Sentence Structures**: The scope of quantifiers and negations in complex sentence structures is often vague.
- **Context Dependence**: Semantic interpretation relies on context, and lack of sufficient contextual information easily leads to ambiguity.

### 4. Pragmatic Ambiguity
**Types**
- **Implicature**: The speaker's intent differs from the literal meaning, e.g., "Can you pass the salt?" can mean "Are you able to pass the salt?" or "Please pass the salt."
- **Indirect Speech Acts**: The speaker expresses intentions indirectly, e.g., "I'm thirsty" can mean stating a fact or requesting water.

**Causes**
- **Pragmatic Strategies**: Speakers use indirect speech acts or implications to achieve communicative goals, creating ambiguity.
- **Context Absence**: Pragmatic interpretation depends on context; without it, ambiguity arises.
- **Cultural and Social Backgrounds**: Different cultural and social contexts lead to different understandings of speech acts, causing ambiguity.

### 5. Phonological Ambiguity
**Types**
- **Phonetic Similarity**: Words or phrases sound similar, creating ambiguity, e.g., "night" and "knight."
- **Phonological Overlap**: Overlapping pronunciations in rapid speech create ambiguity, e.g., "ice cream" and "I scream."

**Causes**
- **Phonetic Simplification**: Simplification of speech sounds leads to phonetic similarity and overlap.
- **Phonetic Changes**: Phonetic changes like linking and reduction in rapid speech cause ambiguity.
- **Auditory Misunderstanding**: Misinterpretation or unclear auditory information leads to ambiguity.

These five types of ambiguity are inherent in any sufficiently complex natural language. Even Latin, known for its structured rigor, faces ambiguities that require contextual interpretation due to inflection and polysemy. However, humans have always aspired to invent a language with the certainty of mathematics, devoid of ambiguity. With the advent of computers, numerous programming languages emerged, aiming to precisely express the complexities of the real world, similar to mathematical precision. Engineers succeeded in creating many programming languages that, like mathematics, are precise and can efficiently run on their designed computational devices. However, they soon realized the need to balance flexibility with rigor. Strict syntax and rules often compromise flexibility, reducing the language’s usability and expressiveness. Furthermore, even well-trained programmers, faced with increasingly complex business requirements, began to favor highly flexible and readable high-level languages. Thus, modern programming languages started to resemble natural languages more closely.

With the emergence of large language models, the trend of using natural language prompts to instruct AI in programming has become increasingly popular, potentially overshadowing traditional coders. When humans can truly use AI as both a compiler and runtime to invoke various silicon-based services, will natural language be the end of high-level languages?

In my speculation, linguistic ambiguity will once again emerge as a significant challenge. At that point, people may reminisce about the efforts programming languages made to eliminate ambiguity. Let us anticipate and explore the strategies programming languages have employed:

Programming languages have adopted various mechanisms to eliminate ambiguity and ensure the accuracy and consistency of programs:

1. **Strict Syntax and Semantic Rules**:
    - **Syntax**: Programming languages define strict syntax rules that dictate the structure and form of programs, such as variable declarations, function definitions, and control structures.
    - **Semantics**: The semantic rules of programming languages define the meaning of syntactic structures, ensuring each structure has a clear interpretation during execution, thus eliminating ambiguity.

2. **Type Systems**:
    - **Static Typing**: In statically typed languages (e.g., Java, C++), the compiler checks type consistency during compilation, reducing runtime errors.
    - **Dynamic Typing**: In dynamically typed languages (e.g., Python, JavaScript), type checks occur at runtime, offering flexibility but also reporting errors during execution.

3. **Scope and Namespace**:
    - **Scope**: Scope rules define the visibility of variables and functions within a program, distinguishing between local and global variables to reduce naming conflicts and unintended reuse.
    - **Namespace**: Namespace mechanisms group identifiers, preventing naming conflicts, e.g., Python modules and C++ namespaces.

4. **Modularity and Encapsulation**:
    - **Modularity**: Programming languages support dividing code into modules or packages, allowing independent development and testing, managing complexity, and reducing dependencies.
    - **Encapsulation**: Object-oriented languages (e.g., Java, C++) use classes and objects for encapsulation, hiding internal implementation details and exposing only necessary interfaces.

5. **Code Style Guides and Static Analysis Tools**:
    - **Style Guides**: Programming communities often establish style guides recommending consistent coding styles and conventions to reduce stylistic ambiguities.
    - **Static Analysis Tools**: These tools analyze code before compilation, identifying potential errors and stylistic issues to ensure code quality.

These mechanisms, combined with advanced abstraction techniques like object-oriented and generic programming, software engineering practices like testing and quality management, and design patterns, enable programming languages to express an increasingly complex world. Now, it’s natural language's turn. The path programming languages have taken will help natural language meet the demands of a more complex world.

Therefore, we believe natural language will inevitably need regulations to find a new balance between rigor and flexibility. These regulations, we hope, will be implemented in a manner similar to IDE tools, making natural language "programming" more engineered. This will reduce ambiguities in natural language expression and computational operations, enhancing the certainty of outcomes. This is another aspiration we have for WithSophie.