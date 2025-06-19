<!-- component start: main_prompt -->
# Generate-Chain-withModel Prompt: <<name_of_chain>> (based on <<name_of_model>>)

该prompt的功能是，对Chain_draft进行分析，并按照Model中定义的entity_yaml_of_model的内容，根据GenModelInstanceRule，生成ModelInstance。
用ModelInstance的内容，遵循GenChainRule的规则，按照Datadic的格式，生成chain_json
用ModelInstance的内容，按照GenChainAgenda的规则，生成Chain_Agenda，并将生成的内容存进chain_json的summary中。

<<name_of_model>>
## chain_draft
<<component:Chain_draft>>
## ModelSchema
<<component:ModelSchema>>
## entity_yaml_of_model
<<component:entity_yaml_of_model>>
## GenModelInstanceRule
<<component:GenModelInstanceRule>>
## GenChainRule
<<component:GenChainRule>>
## Datadic
```json
<<component:Datadic>>
```
<<component:GenChainAgenda>>

<!-- component end: main_prompt -->
<!-- component start: Chain_draft -->
``` txt
<<chain_draft>>
```
<!-- component end: Chain_draft -->
<!-- component start: entity_yaml_of_model -->
``` json
<<entity_yaml_of_model>>
```
<!-- component end: entity_yaml_of_model -->
<!-- component start: GenModelInstanceRule -->
<<component:HowtoMakeChain>>
### 根据<<Chain_draft>>的内容对entity_yaml_of_model的内容进行实例化，生成ModelInstance的内容：
1、判断其涉及的领域，生成domain，这个领域应具备一定的抽象性；
2、深入理解<Chain_draft>>中的内容，并根据如下规则，实例化entity_yaml_of_model中的entites,为这些属性赋值
* id：在原entity的id的基础上增加一个可以表达该entity的实体的词，用_分割开
* prototype：原prototype和domain融合而成的一个词，既能继承原prototype所表达的关系，又能体现domain的具体领域
* define_baseset：按照原entity的规定，修改为实例化后的对应的entity的ID，如果原值为promitive，则不变
* define_prompt：定义一种方法，这种方法是表达如何对define_baseset中的entities进行处理，得出该entity的值的
* occur：和原entity一致
* inherits：原entity的id
* value：将define_baseset的值代入define_prompt中，得出的结果
3、分析实例化完成后的ModelInstance，再根据chain_draft的内容，找出
* G1:if prototype=quadrant then LLM_output=true
### 将ModelInstance生成更易读的agenda
<<component:GenChainAgenda>>
4、根据ref_domain，根据<<Model>>所设定的prototype的元素，并参考<<Model>>中的define_prompt，为其生成符合<<Chain_draft>>需要的define_prompt，并依据define_prompt，为define_baseset为[primitive]的entity生成能表达其含义的ID。
5、按照define_baseset的定义，结合<<Model>>中对应的define_prompt的定义，为后续的entities生成符合<<Chain_draft>>需要的define_prompt，并依据define_prompt，依次生成其余的entities的ID，
6、根据prototype和对应的baseset，依照<<Model>>中对应的define_prompt的定义，为其生成符合<<Chain_draft>>需要的define_prompt，并根据define_prompt生成relation的ID
7、ModelInstance中的entity和relations的id生成请将<<Model>>的id拼在生成的id后面，以:分隔。

1、思路作者希望解决某一个领域的一类问题，他对这类问题的描述就是chain_draft，请根据他的需求，推测这个领域是什么，生成ref_domain，这个领域应是具备一定的抽象性的，并理解想解决的这类问题是什么，据此生成chain_object；
2、假设作者是个对深度思考有着非常独特见解的人，他会用<<name_of_model>>和chain_object的现实问题建立映射的方式进行思考。他的映射方法是：找到这些现实问题中的一些关键元素，映射成Model中的entities。
3、理解模型中的entity：通过各个entities的prototype，理解各个entity之间的结构关系。这个结构关系和要创建的思路的待解决问题的内容的结构有相似性。
4、创建思路的顺序是：先映射chain_object中最关键的元素为define_baseset=primitive的，因为其他的元素都是基于这几个primitive元素生成的。映射的具体方法就是生成这些元素的define_prompt。这些元素的define_prompt的内容是：解释这些元素在chain_object这个解题过程中的含义和价值。
5、其余entities的define_prompt内容，是用来定义这些元素的，而这个定义的构成是：描述这个元素是怎样通过它的baseset父元素生成或推导出来的，且生成出来的结果是符合prototype的特征的，理解prototype需要结合继承的model的ref_domain来综合理解，相同的prototype的entities应该有相同的特征。
6、其他的内容，按照原model中的内容继承，结构要符合model的结构
7、inherits=<<name_of_model>>
<!-- component end: GenModelInstanceRule -->

<!-- component start: GenChainAgenda -->
## GenChainAgenda
通过理解ModelInstance中的内容，理解这个思路的目标和适用范围，并按下文形成一个介绍：
通过对您构思的理解，我们会帮您创建一个解决这类问题的思路，并展现在画布中，您可以在这个基本思路的基础之上，进行进一步的修改。
思路名称： <<name_of_chain>> 
思路领域：ModelInstance中的ref_domain
思路所采用的模型：<<name_of_model>>，并介绍一下这个模型的特点
构建这个思路的关键因素为：ModelInstance中baseset为[primitive]的entity；
关键因素介绍：根据关键因素的define_prompt，介绍关键因素
其他因素介绍：根据其他的entities和relations的define_prompt,介绍其他因素

<!-- component end: GenChainAgenda -->
<!-- component start: ModelSchema -->
 "model": {
      "id": "base_model",
      "name": "Base Model",
      "domain": "geometry",
      "description": "Base structure for all models.",
      "inherits": null,
      "entities": [
        {
          "id": "base_entity",
          "name": "base_entity",
          "prototype": "point",
          "define_baseset": [],
          "define_prompt": "",
          "occur": 1,
          "Value": "",
          "inherits": null
        }
      ]
    }
<!-- component end: ModelSchema -->
<!-- component start: ModelSchemaRule -->
Model是所有思路（chain）的父类，Base Model会用来作为所有Model的基础，而使用这些Model所创建的ModelInstance则是这些Model在某个领域的实例化的结果。
Model各字段的意义和用途：
domain：代表问题所属的领域，会作为实例化时的关键参数参与到实例化的过程中
inherits：代表其继承的父对象，继承者属于被继承的一次具象化的过程
entities：代表思路中的各种实体，实例化的过程就是实体被逐渐具体化的过程,在Model中可以有多个entities
entities.id:这个entity的ID，用作引用时的索引
entities.name:entity的名称，会表达entity的含义
entities.prototype:entity的类型，类型是一个父entity的prototype在ref_doamin这个领域的一个具体表达
entities.define_baseset:形成entity的value的输入参数的定义，如果=primitive，则代表entity为常量，具体的值由define_prompt来决定
entities.define_prompt:用来描述如何使用define_baseset的value来生成该entity的value
entities.occur:Occurrence constraint: 1 (exactly one), n (exactly n), n+ (at least n), n* (up to n, optional).
entities.value:entity的value
entities.inherits:代表这个entity的父entity，其来自其父model所对应的entity

<!-- component end: ModelSchemaRule -->


<!-- component start: HowtoMakeChain -->
运用合适的思维模式（思路）进行思考，是一个将抽象的Model和具体要解决的问题相结合，经过逐步的具象化，形成一个具体的关于这个问题的entity组，并将这些entity里面的value，组合成一个合适的答案的过程。整个过程可以理解为一个函数的执行过程，而思路就是这个函数中的函数体部分，构建思路就是构建其中的函数体。其中entity，则是这个函数体在执行过程中需要调用的常量和变量。整个函数的返回值就是这次思考的最终结果，思考时的背景信息被称作ThinkPoint，是这个函数执行的输入参数。
构建思路的过程是这样的：
1、根据Model的框架，将思路设计者的设计需求变成一个更为具体的ModelInstance
2、将ModelInstance的内容，按照特定的格式，将所有的entity映射成变量，将为entity具体赋值的过程映射成步骤
3、选择合适的显示方案和对应方案中需要展现的变量

<!-- component end: HowtoMakeChain -->
<!-- component start: GenChainRule -->


### Step 1：通过ModelInstance，理解所选择的 Model和思路期待解决的问题

* 通过ModelInstance的ref_domain确定这个思路的问题域
* trainName是<<name_of_chain>>，modelId使用Model的ID
* 根据chain_draft的内容，推测思路的思考目标


#### Step 2：理解所有的entity，并根据Model建立变量

* 将ModelInstance中的所有entity都生成为变量，
* 变量的命名方法：varName=entityID
* 所有变量必须依次记录进 `varList`（即变量清单）。
* 用户提供的第一个变量固定命名为 `ThinkPoint`。
* 根据ModelInstance的define_baseset的关联关系，找出各个变量的依赖关系
* 依赖关系的示例如下：
    ```json
    dependencies = {
      "X": ["ThinkPoint"],
      "Y": ["X"],
      "Z": ["X", "Y"]
    }
    ```

### step 3:生成步骤

* 从define_baseset=primitive的entities和relations开始建立步骤
* 根据define_prompt来创造stepPrompt，stepPrompt的目标是：使用当前的entity对应的变量创造它的依赖变量，将所有拥有依赖变量的变量所对应的步骤都创建完成；
* 所有没有被依赖的变量，被称为终点变量，终点变量所对应的stepPrompt的目标是：将Thinkpoint的内容，根据define_prompt所设定的条件，按照推测出的思考目标，进行对应的处理。这种stepPrompt的例子是：
```prompt
我希望对{{thinkpoint}}（美国民主党的政策）进行{{思考目标}}（分类处理），当前的步骤需要处理的是从{{ThinkPoint}}中找出define_prompt（第一象限：经济上支持政府干预，社会上倾向进步）的内容,请将符合条件的值存进{{quadrant_I:binary_orthogonal}}
```


### Step 4：理清变量生成的因果顺序

* 以 `ThinkPoint` 为起点，构建变量之间的生成链。
* 所有变量必须有清晰的前置依赖关系（除 `ThinkPoint`和define_baseset=primitive的变量）。
* 构成整个“思路”的路径（step-by-step chain），这个路径体现为变量间的依赖关系。


### Step 5：构建分步逻辑链

* 根据依赖关系来构建步骤和步骤之间的关系。
* 每一步能使用多个输入变量，只能生成一个输出变量，输入变量和输出变量在 prompt 里面的使用需要符合格式规定，用 `{{}}` 扩起来。
* 每一步的 Prompt 指令应根据输入/输出逻辑改写。
* 每一步必须产出一个明确的结果，且这个结果需要赋值给输出变量，这个赋值动作需要在步骤的 prompt 写出来。
* 每个变量生成完毕后写入 `varList`。
* step中的最后一个步骤，其类型应该为10，且应该形成modeVarMap中对变量的映射，映射方式应参考模型中的描述，只选最必需的变量映射，无需将所有变量映射进去，modeVarMap中的ModeVarName，请根据变量名称中的:后面的Modelid定义。


### Step 6：以符合数据字典的 JSON 输出结果**

* 输出为一个整体思路级 JSON 对象，字段必须参考Datadic，只为必填字段赋值。

  * 依赖关系不作为 JSON 内容输出。
  * 检查所有 step 中的 `preID` 和 `nextID`，如果出现不一致的情况，请参照依赖关系重新调整，确保 step 的顺序描述的一致性。
* 最后做一次格式检查，要求输出的结果严格符合json的格式要求。

### Final Output  
请根据提供的信息生成结果，并严格按照以下JSON格式返回结果，不要添加任何额外的解释、注释或markdown标记：
 - format examples:
     {
         "rootObject": value is  chain_json
     }

<!-- component end: GenChainRule -->


<!-- component start: Datadic -->

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "termList": {
      "type": "array",
      "items": {}
    },
    "totalTermList": {
      "type": "array",
      "items": {}
    },
    "totalVarList": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "trainId": { "type": "string" },
          "varType": { "type": "integer" },
          "varName": { "type": "string" },
          "varLevel": { "type": "integer" },
          "varDesc": { "type": "string" },
          "varFormat": { "type": ["string", "null"] },
          "defaultValue": { "type": ["string", "null"] },
          "stepId": { "type": ["string", "null"] },
          "id": { "type": "integer" },
          "childs": { "type": ["array", "null"], "items": {} },
          "parentId": { "type": ["integer", "null"] }
        },
        "required": ["trainId", "varType", "varName", "varLevel", "varDesc", "stepId", "id"]
      }
    },
    "modelId": { "type": ["string", "integer"] },
    "varList": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "trainId": { "type": "string" },
          "varType": { "type": "integer" },
          "varName": { "type": "string" },
          "varLevel": { "type": "integer" },
          "varDesc": { "type": "string" },
          "varFormat": { "type": ["string", "null"] },
          "defaultValue": { "type": ["string", "null"] },
          "stepId": { "type": ["string", "null"] },
          "id": { "type": "integer" },
          "childs": { "type": ["array", "null"], "items": {} },
          "parentId": { "type": ["integer", "null"] }
        },
        "required": ["trainId", "varType", "varName", "varLevel", "varDesc", "stepId", "id"]
      }
    },
    "trainName": { "type": "string" },
    "welcomeMessage": { "type": "string" },
    "trainDesc": { "type": "string" },
    "id": { "type": "string" },
    "stepList": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "trainId": { "type": "string" },
          "preId": { "type": ["string", "null"] },
          "stepType": { "type": "integer" },
          "stepDesc": { "type": "string" },
          "cases": { "type": "array" },
          "stepInVars": { "type": "array", "items": { "type": "string" } },
          "modelVarMap": { "type": "array" },
          "stepOutVars": { "type": "array", "items": { "type": "string" } },
          "nextId": { "type": ["string", "null"] },
          "stepTerms": { "type": "array" },
          "trainModelGraphPrompt": { "type": ["string", "null"] },
          "stepName": { "type": "string" },
          "generationPrompts": { "type": "array" },
          "id": { "type": "string" },
          "stepPrompt": { "type": "string" }
        },
        "required": ["trainId", "stepType", "stepDesc", "stepInVars", "stepOutVars", "id", "stepPrompt"]
      }
    }
  },
  "required": [
    "termList",
    "totalTermList",
    "totalVarList",
    "modelId",
    "varList",
    "trainName",
    "welcomeMessage",
    "trainDesc",
    "id",
    "stepList"
  ]
<!-- component end: Datadic