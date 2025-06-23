<!-- component start: main_prompt -->
# Generate-Chain-withModel Prompt: <<name_of_chain>> (based on <<name_of_model>>)

该prompt的功能是，对Chain_draft进行分析，并按照Model中定义的entity_yaml_of_model的内容，根据GenModelInstanceRule，生成ModelInstance。
用ModelInstance的内容，遵循GenChainRule的规则，按照ChainSchema规定的格式，生成chain_json
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
## ChainSchema
<<component:ChainSchema>>
<<component:GenChainAgenda>>
## Final Output
请根据提供的信息生成结果，并严格按照以下JSON格式返回结果，不要添加任何额外的解释、注释或markdown标记：
format examples:
{
  "rootObject": value is chain_json
}
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
* 顺序先从define_baseset为[primitive]的entity开始
* id：在原entity的id的基础上增加一个可以表达该entity的实体的词，用_分割开
* prototype：原prototype和domain融合而成的一个词，既能继承原prototype所表达的关系，又能体现domain的具体领域
* define_baseset：按照原entity的规定，修改为实例化后的对应的entity的ID，如果原值为promitive，则不变
* define_prompt：定义一种方法，这种方法是表达如何对define_baseset中的entities进行处理，得出该entity的值的
* occur：和原entity一致
* inherits：原entity的id
* value：将define_baseset的值代入define_prompt中，得出的结果
3、分析实例化完成后的ModelInstance，再根据chain_draft的内容，找出这些entity中，所有需要和thinkpoint交互的，形成actual_entity。可以通过如下方法，判断entity是否存在和thinkpoint的交互关系：
* chain_draft中显性说明的；
* chain_draft中提出的要解决的问题中，解答问题明显需要的；
* define_prompt中明显缺乏输入变量，无法直接得出结果的；
### 重构ModelInstance中的actual_entity
* 将ThinkPoint加入entity的define_baseset
* 根据chain_draft的内容和新的define_baseset，重新构建entity的define_prompt
* 构建prompt的一些示例：
 * 将thinkpoint中符合baseset条件的内容筛选出，构建成列表，作为entity的value
 * 将thinkpoint和原baseset以某种形式进行结合，综合形成一个新的内容，作为entity的value
 * thinkpoint是待加工内容，baseset是加工方法，加工结果存入entity的value

### 将ModelInstance生成更易读的agenda
<<component:GenChainAgenda>>


<!-- component end: GenModelInstanceRule -->

<!-- component start: GenChainAgenda -->
## GenChainAgenda
通过理解ModelInstance中的内容，理解这个思路的目标和适用范围，并按下文形成一个介绍：
通过对您构思的理解，我们会帮您创建一个解决这类问题的思路，并展现在画布中，您可以在这个基本思路的基础之上，进行进一步的修改。
思路名称： <<name_of_chain>> 
思路领域：ModelInstance中的domain
思路所采用的模型：<<name_of_model>>，并介绍一下这个模型的特点
思路能处理的问题类型：根据chain_draft的描述和ModelInstance，推测这个思路能解决哪些类型的问题
思考输入内容：请根据chain_draft的描述和ModelInstance,推测运行这个思路（思考）时期待的用户输入
构建这个思路的关键实体为：ModelInstance中baseset为[primitive]的entity；
关键实体介绍：根据关键实体的define_prompt，介绍关键实体的生成函数
关键实体的默认值：baseset为[primitive]的entity的value
处理思考输入的实体：actual_entity中的所有entity
处理思考输入的实体的介绍：根据处理思考输入的实体的define_prompt，介绍它们的生成函数
过渡实体：并未被列入actual_entity中的其它entity
过渡实体的介绍：根据过渡实体的define_prompt，介绍过渡实体的生成函数

这些内容将会在画布中创建成思路，实体会创建成变量，define_prompt会作为步骤的prompt，这些内容可以在画布中再次进行修改。
如果您对这些内容不满意，也可以对chain_draft的描述进行修改，这些内容将会按照您的要求重新生成。
对描述的修改可以继续细化您的需求，也可以直接指定思路的内容。
如：请将axis_x中的define_prompt改为"The X-axis representing opposing conceptual vectors."

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
运用合适的思维模式（思路）进行思考，是一个将抽象的Model和具体要解决的问题相结合，经过逐步的具象化，形成一个具体的关于这个问题的entity组，并将这些entity里面的value，组合成一个合适的答案的过程。整个过程可以理解为一个main函数的执行过程，而思路就是这个main函数中的函数体部分，构建思路就是构建其中的函数体。其中entity的值，则是这个main函数在执行过程中需要调用的常量和变量，而赋值的过程则是entity函数。main函数的返回值就是这次思考的最终结果，思考时的背景信息被称作ThinkPoint，是main函数执行的输入参数。
构建思路的过程是这样的：
1、根据Model的框架设计，实现所有的entity函数，这个具体实现的entity函数库，被称为ModelInstance
2、选择在思路中需要使用的entity，设计这些entity的value是如何通过对thinkpoint的计算来最终实现问题答案的。（设计main函数的函数体）
3、构建返回值，也就是针对计算后的entity的value，选择合适的显示方案。

<!-- component end: HowtoMakeChain -->
<!-- component start: GenChainRule -->

#### Step 1：理解所有的entity，并根据Model建立变量

* 将ModelInstance中的所有entity都生成为变量，
* 变量的命名方法：varName=entityID
* 所有变量必须依次记录进 `TotalvarList`（即变量清单）。
* 根据该entity的baseset确定该变量的依赖关系，依赖关系的示例如下：
    ```json
    dependencies = {
      "X": ["ThinkPoint"],
      "Y": ["X"],
      "Z": ["X", "Y"]
    }
    ```
* 用户输入的变量命名为 `ThinkPoint`。

#### step 3:生成步骤
* 为每一个entity所生成的变量建立一个步骤，这个变量就是这个步骤的输出变量，步骤会根据变量的依赖关系（输入变量），为变量赋值，赋值的方式是这个变量对应的entity的prompt所定义的，而这个prompt就会被定义为步骤的prompt。在Prompt中，所有的变量引用都会用{{}}括起。
* 首先创建类型为初始节点的步骤，这个步骤的输出变量为ThinkPoint
* 从define_baseset=primitive的entities开始，完成所有的步骤建立
* 根据该步骤的输出变量之间的依赖关系，建立步骤之间的前后序关系
* 每一步的 Prompt 指令应参考这样的形式进行改写：“通过{{输入变量1}}和{{输入变量2}}的XXX分析/综合等行为（按entity中的prompt的指引），生成{{输出变量}}“
* 每个变量生成完毕后写入 `varList`。
* 最后一个步骤，其类型应该为10，且应该形成modeVarMap中对变量的映射，映射方式应参考模型中的描述，只选最必需的变量映射，无需将所有变量映射进去，modelVarMap中的ModelVarName，请根据ModelInstance所继承的Model中的entity的ID来确定。


#### Step 4：以符合schema的 JSON 输出结果**

* 输出为一个整体思路级 JSON 对象，字段必须按照ChainSchema的定义，所有变量的值来自于前面的赋值过程。

  * 依赖关系不作为 JSON 内容输出。
  * 检查所有 step 中的 `preID` 和 `nextID`，如果出现不一致的情况，请参照依赖关系重新调整，确保 step 的顺序描述的一致性。
* 最后做一次格式检查，要求输出的结果严格符合json的格式要求。

<!-- component end: GenChainRule -->
<!-- component start: ChainSchema -->
## ChainSchema
<<chain_schema>>
<!-- component end: ChainSchema -->