<!-- component start: main_prompt -->
# Generate-Chain-withModel Prompt: <<name_of_chain>> (based on <<name_of_model>>)

该prompt的功能是根据用户所选择的<<Model>>，对<<Chain_draft>>进行分析，并按照GenModelInstanceRule中的规则，生成<<ModelInstance>>。
用<<ModelInstance>>的内容，遵循GenChainRule的规则，按照Datadic的格式，生成<<chain_json>>
用<<chain_json>>，按照GenChainAgenda的规则，生成<<Chain_Agenda>>


<<component:GenModelInstanceRule>>

<<component:GenChainRule>>

<<component:Datadic>>

<<component:GenChainAgenda>>
<!-- component end: main_prompt -->

<!-- component start: GenModelInstanceRule -->
## GenModelInstanceRule
根据<<Chain_draft>>的内容生成ModelInstance的内容：
1、判断其涉及的领域，生成ref_domain，这个领域应具备一定的抽象性；
2、根据<Chain_draft>>来确定思路的类型<<chain_type>>：分类、排序、决策、组合
* 分类（Categorize）：思考的目标是对对象或信息进行归类，以识别特征或结构。
* 排序（Prioritize）：思考的目标是对事物按某种标准进行排序，强调“先后、重要性、优劣”等
* 决策（Evaluate）：思考的目标是通过权衡，得出最合适的结论
* 组合（Synthesize）：思考的目标是通过组合不同维度的元素，形成新的内容
3、根据entity/relation的prototype确定其是否需要在step的prompt的执行后，生成输出值，将其LLM_output属性设置为true/false；
* G1:if prototype=quadrant then LLM_output=true

4、根据ref_domain，根据<<Model>>所设定的prototype的元素，并参考<<Model>>中的define_prompt，为其生成符合<<Chain_draft>>需要的define_prompt，并依据define_prompt，为define_baseset为[primitive]的entity生成能表达其含义的ID。
5、按照define_baseset的定义，结合<<Model>>中对应的define_prompt的定义，为后续的entities生成符合<<Chain_draft>>需要的define_prompt，并依据define_prompt，依次生成其余的entities的ID，
6、根据prototype和对应的baseset，依照<<Model>>中对应的define_prompt的定义，为其生成符合<<Chain_draft>>需要的define_prompt，并根据define_prompt生成relation的ID
7、ModelInstance中的entity和relations的id生成请将<<Model>>的id拼在生成的id后面，以:分隔。
<!-- component end: GenModelInstanceRule -->

<!-- component start: GenChainAgenda -->
## GenChainAgenda
用<<chain_json>>中的内容，帮我生成<<Chain_Agenda>>，<<Chain_Agenda>>的目的是为了让人快速了解该<<chain_json>>的内容，<<Chain_Agenda>>的内容包括：
1. <<chain_json>>的name；
2.根据对应的define_prompt解释baseset为[primitive]的entity的含义；
3.依照baseset的顺序，根据对应的define_prompt解释其他entity的含义；
4.根据对应的define_prompt解释relation的含义。
    Example: |
      1. chain_json的name是{{Chain_json.name}}，它是一个{{Chain_json.visual}}模型。
      2. axis_x表示{{Chain_json.axis_x.define_prompt}}，axis_y表示{{Chain_json.axis_y.define_prompt}}。
      3. quadrant_I表示{{Chain_json.quadrant_I.define_prompt}}，quadrant_II表示{{Chain_json.quadrant_II.define_prompt}}，quadrant_III表示{{Chain_json.quadrant_III.define_prompt}}，quadrant_IV表示{{Chain_json.quadrant_IV.define_prompt}}。
      4. x_flip表示{{Chain_json.x_flip.define_prompt}}，y_flip表示{{Chain_json.y_flip.define_prompt}}，diagonal_reverse表示{{Chain_json.diagonal_reverse.define_prompt}}，diagonal_swap表示{{Chain_json.diagonal_swap.define_prompt}}。
<!-- component end: GenChainAgenda -->

<!-- component start: GenChainRule -->
## GenChainRule

### Step 1：通过<<ModelInstance>>，理解所选择的 Model和思路期待解决的问题

* 通过<<ModelInstance>>的ref_domain确定这个思路的问题域
* trainName是<<name_of_chain>>，modelId使用<<Model>>的ID



### Step 2：理解所有的entity和relation，并根据Model建立变量

* 
* 将所有<<ModelInstance>>中的entity和relation都生成为变量，
* 变量的命名方法：varName=entity/relationsID
* 根据对应的define_prompt，和prototype类型，生成varDesc的内容，例子是：social_axis:binary_orthogonal是一个axis维度，它的含义是美国民主党在社会自由与保守之间的立场；pro_intervention:binary_orthogonal是一个vector，它的含义是倾向政府干预的经济政策方向；
quadrant_I:binary_orthogonal是一个quadrant，它的含义是第一象限：经济上支持政府干预，社会上倾向进步
* 所有变量必须依次记录进 `varList`（即变量清单）。
* 用户提供的第一个变量固定命名为 `ThinkPoint`。

### step 3:生成步骤

* 为每一个LLM_output=true的entity和relation建立一个步骤（step）
* 根据<<chain_type>>和define_prompt来创造stepPrompt，stepPrompt的目标是：将Thinkpoint的内容，根据define_prompt所设定的条件，按照<<chain_type>>的思考目标，进行对应的处理
* stepPrompt的例子是：我希望对{{thinkpoint}}（美国民主党的政策）进行chain_type（分类）处理，当前的步骤需要处理的是define_prompt（第一象限：经济上支持政府干预，社会上倾向进步）,请将符合条件的值存进{{quadrant_I:binary_orthogonal}}

### Step 4：理清变量生成的因果顺序

* 以 `ThinkPoint` 为起点，构建变量之间的生成链。
* 所有变量必须有清晰的前置依赖关系（除 `ThinkPoint`）。
* 构成整个“思路”的路径（step-by-step chain），这个路径体现为变量间的依赖关系。

  * 依赖关系的示例如下：
    ```json
    dependencies = {
      "X": ["ThinkPoint"],
      "Y": ["X"],
      "Z": ["X", "Y"]
    }
    ```

### Step 5：构建分步逻辑链

* 将整个 Prompt 拆解为多个步骤（step）。
* 根据依赖关系来构建步骤和步骤之间的关系。
* 每一步能使用多个输入变量，只能生成一个输出变量，输入变量和输出变量在 prompt 里面的使用需要符合格式规定，用 `{{}}` 扩起来。
* 每一步的 Prompt 指令应根据输入/输出逻辑改写。
* 每一步必须产出一个明确的结果，且这个结果需要赋值给输出变量，这个赋值动作需要在步骤的 prompt 写出来。
* 每个变量生成完毕后写入 `varList`。
* step中的最后一个步骤，其类型应该为10，且应该形成modeVarMap中对变量的映射，映射方式应参考模型中的描述，只选最必需的变量映射，无需将所有变量映射进去，modeVarMap中的ModeVarName，请根据变量名称中的:后面的Modelid定义。

**Step 6：去除格式相关的规约**

* 只保留内容相关的生成规则。
* 每一步只描述思维转换、生成机制。

**Step 7：以符合数据字典的 JSON 输出结果**

* 输出为一个整体思路级 JSON 对象，字段必须参考数据字典，只为必填字段赋值。

  * 依赖关系不作为 JSON 内容输出。
  * 检查所有 step 中的 `preID` 和 `nextID`，如果出现不一致的情况，请参照依赖关系重新调整，确保 step 的顺序描述的一致性。


<!-- component end: GenChainRule -->


<!-- component start: Datadic -->
## Datadic

### 根对象 (Root Object)

| 字段名称       | 数据类型           | 描述                                    | 默认值          | 说明                                                                                                          | 例子                                   |
| -------------- | ------------------ | --------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| id             | String             | 思路ID                                  | 未指定          | 唯一标识一个思路。                                                                                            | "思路ID"                               |
| trainName      | String             | 思路名                                  | 未指定          | 根据 prompt 的作用，设计一个简短易记的名称。                                                                  | "内容总结助手"                         |
| trainDesc      | String             | 思路描述                                | 未指定          | 根据 prompt 的作用，描述其具体功能和应用场景。                                                                | "此思路用于快速总结长文本的主要内容。" |
| welcomeMessage | String             | 思路欢迎语                              | 未指定          | 主要向用户表达，希望他们输入的内容或如何开始使用该思路。                                                      | "请输入您想总结的文本内容："           |
| summary        | String             | 思路总结                                | 未指定          | 对整个思路的功能或成果的总结性描述。                                                                          |                                        |
| modelId        | String             | 模式ID                                  | 未指定          | 如果该思路是基于某个特定模式创建的，则记录模式的ID。                                                          | "模式ID"                               |
| stepList       | Array `<Object>` | 思路过程中的步骤列表。                  | `[]` (空数组) | 定义了思路执行的具体步骤和逻辑。详细信息请参见下方的**步骤对象 (Step Object)** 部分。                   |                                        |
| varList        | Array `<Object>` | 实体变量列表 - 步骤使用到的变量。       | `[]` (空数组) | 存储在思路执行过程中，步骤间传递和使用的变量。详细信息请参见下方的**变量对象 (Variable Object)** 部分。 |                                        |
| totalVarList   | Array `<Object>` | 实体变量列表 - 当前思路定义的全量变量。 | `[]` (空数组) | 包含此思路中定义的所有变量的完整列表。详细信息请参见下方的**变量对象 (Variable Object)** 部分。         |                                        |
| termList       | Array `<Object>` | 术语列表 - 当前思路使用到的术语。       | `[]` (空数组) | 定义在当前思路的 prompt 或步骤中明确使用的术语。详细信息请参见下方的**术语对象 (Term Object)** 部分。   |                                        |
| totalTermList  | Array `<Object>` | 术语列表 - 当前思路定义的全量术语。     | `[]` (空数组) | 包含此思路中定义的所有术语的完整列表。详细信息请参见下方的**术语对象 (Term Object)** 部分。             |                                        |

### 步骤对象 (Step Object) (位于 `stepList` 内)

| 字段名称              | 数据类型           | 描述                                 | 默认值              | 说明                                                                                                                                                                          | 例子                                      |
| --------------------- | ------------------ | ------------------------------------ | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| id                    | String             | 步骤ID                               | 未指定              | 唯一标识一个步骤。                                                                                                                                                            | "步骤ID"                                  |
| preId                 | String             | 前步骤ID,分隔多个                    | 空字符串或 `null` | 指向当前步骤的前一个或多个步骤的ID，用逗号分隔。                                                                                                                              | "stepId_A,stepId_B"                       |
| nextId                | String             | 后步骤ID,分隔多个                    | 空字符串或 `null` | 指向当前步骤的后一个或多个步骤的ID，用逗号分隔。                                                                                                                              | "stepId_C,stepId_D"                       |
| trainId               | String             | 思路标识                             | 未指定              | 所属思路的ID。                                                                                                                                                                | "思路ID"                                  |
| stepType              | String/Number      | 步骤类型                             | 未指定              | 1-普通步骤, 2-总结, 3-取图步骤, 4-归纳步骤, 5-摘要步骤, 6-归属, 7-搜索步骤, 8-工具步骤, 9-起始节点, 10-结束节点, 11-知识库步骤, 12-if-else步骤。                              | `1` (普通步骤)                          |
| stepName              | String             | 步骤名称                             | 未指定              | 当前步骤的名称。                                                                                                                                                              | "提取关键信息"                            |
| stepDesc              | String             | 步骤描述                             | 未指定              | 对当前步骤功能的详细描述。                                                                                                                                                    | "此步骤用于从输入文本中提取关键信息点。"  |
| stepInVars            | String/Array       | 输入变量数组                         | `[]`              | 步骤执行所需的输入变量名称列表。文档中描述为数组，示例中为字符串，应以实际JSON为准。                                                                                          | `["inputText"]`                         |
| stepOutVars           | Array `<String>` | 输出变量数组                         | `[]`              | 步骤执行后产生的输出变量名称列表。                                                                                                                                            | `["keyInfo"]`                           |
| stepTerms             | Array `<String>` | 步骤用到的术语数组                   | `[]`              | 此步骤的 prompt 或逻辑中用到的特定术语列表。                                                                                                                                  | `["核心观点", "主要论据"]`              |
| stepPrompt            | String             | 步骤prompt                           | 未指定              | 用于指导大模型生成内容的具体提示文本。                                                                                                                                        | "请总结以下文本的主要观点：{{inputText}}" |
| cases                 | Array `<Object>` | 条件列表 (if-else步骤类型的条件列表) | `[]`              | 仅当 `stepType` 为 12 (if-else步骤) 时适用。详细信息请参见下方的 **Case 对象 (Case Object)** 部分。                                                                   |                                           |
| modelVarMap           | Array `<Object>` | 变量映射关系 (END类型的结点)         | 未指定              | 仅当 `stepType` 为 10 (结束节点) 时适用。定义了思路的输出变量如何映射到模式变量。详细信息请参见下方的 **模式变量映射对象 (Mode Variable Map Object)** 部分。          |                                           |
| trainModelGraphPrompt | String             | 使用模式的graphprompt                | 未指定              | 仅当 `stepType` 为 10 (结束节点) 时适用。如果步骤使用了模式中的 graphprompt，在此处记录。                                                                                   |                                           |
| generationPrompts     | Array `<Object>` | 多种graphprompt                      | `[]`              | 仅当 `stepType` 为 10 (结束节点) 时适用。如果一个步骤内有多种生成方式或 prompt 变体，在此定义。详细信息请参见下方的**生成提示对象 (Generation Prompt Object)** 部分。 |                                           |

### Case 对象 (Case Object) (位于步骤对象的 `cases` 数组内, 当 `stepType` 为 12 时)

| 字段名称        | 数据类型          | 描述                   | 默认值 | 说明                                                                                                   | 例子                                          |
| --------------- | ----------------- | ---------------------- | ------ | ------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| nextId          | String            | 指向步骤ID             | 未指定 | 当前条件分支满足后，流程应跳转到的下一个步骤的ID。                                                     | "stepId_TrueBranch"                           |
| logicalOperator | String            | 逻辑类型               | "and"  | 定义多个条件之间的逻辑关系。                                                                           | "and", "or"                                   |
| id              | String            | if-else case的唯一ID。 | 未指定 | 当前 case（条件分支）的唯一标识符。                                                                    | "ifElse_688adffe-4d8d-4d16-8f20-20f2880f2587" |
| conditions      | Array`<Object>` | 条件                   | `[]` | 定义了当前 case 的一个或多个具体条件。详细信息请参见下方的**条件对象 (Condition Object)** 部分。 |                                               |
| caseType        | String/Number     | Case 类型。            | 未指定 | 标识当前 case 是 "if", "else_if" 还是 "else"。                                                         | `0` (if), `1` (else_if), `2` (else)     |

### 条件对象 (Condition Object) (位于Case对象的 `conditions` 数组内)

| 字段名称           | 数据类型 | 描述           | 默认值   | 说明                             | 例子             |
| ------------------ | -------- | -------------- | -------- | -------------------------------- | ---------------- |
| varType            | String   | 变量类型。     | 未指定   | 条件判断中涉及的变量的类型。     | "1"              |
| varName            | String   | 变量名称。     | 未指定   | 条件判断中涉及的变量的名称。     | "ThinkPoint"     |
| comparisonOperator | String   | 比较操作符。   | 未指定   | 用于比较变量值与目标值的操作符。 | "contains", "==" |
| value              | String   | 用于比较的值。 | 空字符串 | 与变量值进行比较的目标值。       | "keyword"        |

### 模式变量映射对象 (Mode Variable Map Object) (位于步骤对象的 `modeVarMap` 数组内, 当 `stepType` 为 10 时)

| 字段名称     | 数据类型 | 描述         | 默认值 | 说明                                                 | 例子            |
| ------------ | -------- | ------------ | ------ | ---------------------------------------------------- | --------------- |
| varName      | String   | 实体变量名   | 未指定 | 当前思路中定义的实体变量的名称。                     | "总结结果"      |
| modelVarId   | Number   | 模式变量ID   | 未指定 | 对应模式中定义的变量的ID，需要使用真实的模式变量ID。 | "123"           |
| modelVarName | String   | 模式变量名称 | 未指定 | 对应模式中定义的变量的名称。                         | "模式输出变量1" |
| varId        | Number   | 实体变量ID   | `[]` | 当前思路中定义的实体变量的ID。                       | "123"           |

### 生成提示对象 (Generation Prompt Object) (位于步骤对象的 `generationPrompts` 数组内)

| 字段名称       | 数据类型 | 描述                 | 默认值 | 说明                                 | 例子                                          |
| -------------- | -------- | -------------------- | ------ | ------------------------------------ | --------------------------------------------- |
| VarId          | Number   | 唯一ID。             | 未指定 | 当前生成提示配置的唯一标识。         | `123`                                       |
| trainId        | Number   | 思路标识。           | 未指定 | 所属思路的ID。                       | `417`                                       |
| stepId         | String   | 步骤ID。             | 未指定 | 所属步骤的ID。                       | "1919683135748886528"                         |
| generationType | String   | 生成类型。           | 未指定 | 指定生成内容的类型或格式。           | "Chat", "SVG", "RDF"                          |
| stepInVars     | Array    | 此提示的输入变量。   | `[]` | 此特定生成提示所使用的输入变量列表。 | `["sourceText"]`                            |
| stepTerms      | Array    | 此提示中使用的术语。 | `[]` | 此特定生成提示中使用的术语列表。     | `["AI", "机器学习"]`                        |
| stepPrompt     | String   | 提示文本。           | 未指定 | 用于指导模型生成内容的具体提示文本。 | "请根据以下内容生成一张SVG图：{{sourceText}}" |

### 变量对象 (Variable Object) (位于 `varList` 和 `totalVarList` 内)

| 字段名称     | 数据类型    | 描述                    | 默认值   | 说明                                                          | 例子                                                         |
| ------------ | ----------- | ----------------------- | -------- | ------------------------------------------------------------- | ------------------------------------------------------------ |
| id           | Number      | 唯一ID。                | 未指定   | 变量的唯一标识符。                                            | `15104`                                                    |
| trainId      | Number      | 思路标识                | 未指定   | 所属思路的ID。                                                | `417`                                                      |
| parentId     | Null/String | 父ID。                  | `null` | 如果变量具有层级关系，则记录其父变量的ID。                    |                                                              |
| stepId       | String      | 与此变量关联的步骤ID。  | 未指定   | 标识此变量主要在哪个步骤中被定义或使用。                      | "1909528709373546496"                                        |
| varType      | Number      | 变量类型。              | 未指定   | 标识变量的数据类型或用途分类。                                | `1`                                                        |
| varLevel     | Number      | 变量级别。              | `0`    | 变量在层级结构中的级别。                                      | `0` (顶层), `1` (子层)                                   |
| varName      | String      | 变量名称。              | 未指定   | 变量的正式名称，在prompt中通常用 `{{varName}}` 的形式引用。 | "ThinkPoint", "inputText"                                    |
| varDesc      | String      | 变量描述。              | 未指定   | 对变量用途、内容或格式的详细说明。                            | "Anything you wish to think about using a chain of thought." |
| varFormat    | String      | 变量格式。              | 空字符串 | 描述变量内容的具体格式，例如日期格式、JSON结构等。            | "YYYY-MM-DD"                                                 |
| defaultValue | Null/String | 默认值。                | `null` | 变量的初始值或在未提供输入时的默认值。                        |                                                              |
| childs       | Null/Array  | 子变量 (用于层级数据)。 | `null` | 如果变量包含子变量，则在此处列出。                            | `[{"varName": "subPoint1", ...}]`                          |

### 术语对象 (Term Object) (位于 `termList` 和 `totalTermList` 内)

| 字段名称    | 数据类型 | 描述       | 默认值   | 说明                         | 例子             |
| ----------- | -------- | ---------- | -------- | ---------------------------- | ---------------- |
| id          | Number   | 唯一ID。   | 未指定   | 术语的唯一标识符。           | `767`          |
| trainId     | Number   | 思路标识。 | 未指定   | 所属思路的ID。               | `417`          |
| name        | String   | 术语名称。 | 未指定   | 术语的具体名称。             | "terrrrrr", "AI" |
| description | String   | 术语描述。 | 空字符串 | 对术语含义或用法的详细说明。 | "人工智能的简称" |

<!-- component end: Datadic -->