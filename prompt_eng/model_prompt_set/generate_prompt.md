<!-- component start: main_prompt -->
# Generate-Chain-withModel Prompt
## 综述
这是一个通过预先设计好的思路模型，来辅助用户生成思路的prompt。在这个生成的过程中，需要用到的概念和定义请参考目录和构成。

## 目录和构成
### 思路构思（chain_draft）：用户创建思路的构思文本
<<component:Chain_draft>>
### 模型定义 （entity_of_model）：创建思路时，参考Model的实体定义，描述了思路中涉及的各种实体及其属性
<<component:entity_of_model>>
### 思路概述 （chain_agenda)
<<component:GenChainAgenda>>
### 模型实例生成规则(GenModelInstance)：生成思路模型实例的方法
<<component:GenModelInstanceRule>>
### 思路生成规则(GenChain)：思路生成的规则
<<component:GenChainRule>>
### 思路格式规约 ：思路的JSON格式规范
<<component:ChainSchema>>
### 思路文件（chain_json）
思路文件是一个严格符合思路格式规约schema的json文件。

## 生成步骤
生成思路的具体步骤是：
1、用户为该思路命名为： <<name_of_chain>> 
2、用户选择合适的模型定义：<<name_of_model>>
3、用户输入自己对这个思路的思路构思
4、深入理解用户的思路构思，套用模型定义，将思路构思中的内容形成模型实例（ModelInstance），具体的套用方法需要遵循模型实例生成规则
5、将模型实例根据思路概述的方法，形成思路概述（chain_agenda）
<<component:Fatal_Output02>>
<!-- component end: main_prompt -->

<!-- component start: Fatal_Output01 -->
6、将模型实例按照思路格式规约的要求，将思路概述（chain_agenda）放入思路文件（chain_json）的summary字段中，然后生成整个思路文件。
7、请将思路文件（chain_json）严格按照以下JSON格式返回结果，不要添加任何额外的解释、注释或markdown标记：
format examples:
{
  "rootObject": value is chain_json
}
<!-- component end: Fatal_Output01 -->

<!-- component start: Fatal_Output02 -->
6、将思路概述（chain_agenda）和模型实例（ModelInstance）严格按照以下JSON格式返回结果，不要添加任何额外的解释、注释或markdown标记：
format examples:
{
  "rootObject": {"summary":chain_agenda},{"welcomeMessage":ModelInstance}
}
<!-- component end: Fatal_Output02 -->

<!-- component start: Chain_draft -->
``` txt
<<chain_draft>>
```
<!-- component end: Chain_draft -->
<!-- component start: entity_of_model -->
``` json
<<entity_yaml_of_model>>
```
<!-- component end: entity_of_model -->
<!-- component start: GenModelInstanceRule -->
<<component:HowtoMakeChain>>
#### 根据Chain_draft的内容对entity_yaml_of_model的内容进行实例化，生成ModelInstance的内容：
1、分析chain_draft：
* 判断chain_draft想解决的问题涉及的领域，得出chain_draft.domain，这个领域应具备一定的抽象性；
* 推测使用这个思路思考时，用户的输入变量是什么，也就是用户在用这个思路思考时，提出的具体要解决的问题是什么，这个问题被称为ThinkPoint，作为思考的起始条件。
* 推测用户希望得出的思考结果的类型是什么。思考结果的类型分为如下几种，结果为：chain_draft.ThoughtResultType
-解决方案与策略：解决问题，达成目标
-决策与选择：从多项中选一
-理解与洞察：深度认知，看透本质
-创造与构想：产生新事物
-评估与判断：评定价值或真伪
-澄清与整合：化繁为简，理清思绪
-预测与假设：推断未知或未来
* 推测用户希望为哪些entities确定具体的值
2、深入理解Chain_draft中的内容，并根据如下规则，实例化entity_yaml_of_model中的entites,为这些属性赋值
* define_baseset为[primitive]的entity是最关键的实体，请根据chian_draft中的domain，ThoughtResultType和ThinkPoint，来选出最合适的entity作为构建整个思路的核心。
* 从primitive的entity开始，按照define_baseset的顺序，逐个具象化entites
  * id：在原entity的id的基础上增加一个可以表达该entity的实体的词，用_分割开
  * name：能表达该entity的实体的词
  * prototype：原prototype和domain融合而成的一个词，既能继承原prototype所表达的关系，又能体现domain的具体领域
  * define_baseset：按照原entity的规定，修改为实例化后的对应的entity的ID，如果原值为promitive，则为空
  * define_prompt：定义如何用baseset中的entity来生成entity的value。例如：找出axis_a和axis_b的相同之处，作为这个entity的value的值。
  * occur：和原entity一致
  * inherits：原entity的id
  * value：将define_baseset的值代入define_prompt中，得出的结果
3、分析实例化完成后的ModelInstance，再根据chain_draft的内容，找出这些entity中，所有需要和thinkpoint交互的，形成actual_entity。可以通过如下方法，判断entity是否存在和thinkpoint的交互关系：
* chain_draft中显性说明的；
* chain_draft中提出的要解决的问题中，解答问题明显需要的；
* define_prompt中明显缺乏输入变量，无法直接得出结果的；
#### 重构ModelInstance中的actual_entity
* 将ThinkPoint加入entity的define_baseset
* 根据chain_draft的内容和新的define_baseset，重新构建entity的define_prompt
* 构建prompt的一些示例：
 * 将thinkpoint中符合baseset条件的内容筛选出，构建成列表，作为entity的value
 * 将thinkpoint和原baseset以某种形式进行结合，综合形成一个新的内容，作为entity的value
 * thinkpoint是待加工内容，baseset是加工方法，加工结果存入entity的value

#### 生成模型实例（ModelInstance）
将上面生成的结果形成一个json格式的ModelInstance

<!-- component end: GenModelInstanceRule -->

<!-- component start: GenChainAgenda -->
#### GenChainAgenda
通过理解ModelInstance中的内容，生成思路概述(chain_agenda)，这个思路概述(chain_agenda)的格式是：
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
运用合适的思维模式（思路）进行思考，是一个将输入的观点（ThinkPoint），通过设计好的思考步骤（step），将ThinkPoint和各种思考步骤中包含的变量（var）处理成最终结果的过程。整个过程可以理解为一个main函数的执行过程，而思路就是这个main函数中的函数体部分，构建思路就是构建其中的函数体，而构建函数体的语句，则是思考步骤（step）。
思考步骤本质是个prompt，在这个prompt中可能包含ThinkPoint或其他变量，这些变量都是这个思考步骤的输入变量，每个prompt的处理结果将会生成一个新的输出变量。思考的最终结果就是这些输入和输出变量的组合。
构建思路是可以参考模型定义的。模型定义是一组entity实体的定义，这些实体之间有着相互的关联关系，这些关联关系由define_baseset和define_prompt定义。
构建思路的最重要的工作是编写思路构思（chain_draft）和选择合适的模型定义（entity_yaml_of_model）：
思路构思起到了定义这个思路的作用，这个定义越清晰，自动生成的思路效果就越好，需要定义的内容有：
1、定义这个思路想解决的问题所涉及的领域
2、定义这个思路想解决的问题，也就是用户在使用这个思路思考的时候，用什么来作为输入条件，启动这个思考
3、定义这个思路的输出结果类型，也就是用户在使用这个思路完成思考的时候，会得到一个什么类型的答案。
4、定义这个思路的适用范围，也就是定义这个思路所沿用的模型的entities。entities的value可以在思路构建时指定，也可以在思考时动态指定。在思路构建时指定的entities越多，思路适用范围越窄，在思考时动态指定的entities越多，思路适用范围越广。
通过对思路构思的分析，加上选择的模型定义，会生成一个比模型定义更加具体的模型实例（ModelInstance），这个模型实例确定的内容就是思路的基础数据。
将模型实例（ModelInstance）组成一个从ThinkPoint开始的思考步骤链条（StepList），就完成了整个思路（chain）的构建工作。


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
* 最后一个步骤，其类型应该为10，这个步骤的目的是建立Model中的各个entity和chain中使用的变量的对应关系，应该形成modeVarMap中的ModelVar和变量的对应关系，映射方式应参考模型中的描述和变量的真正作用，modelVarMap中的ModelVarName，请根据ModelInstance所继承的Model中的entity的ID来确定。


#### Step 4：以符合schema的 JSON 输出结果**

* 输出为一个整体思路级 JSON 对象，字段必须按照ChainSchema的定义，所有变量的值来自于前面的赋值过程。

  * 依赖关系不作为 JSON 内容输出。
  * 检查所有 step 中的 `preID` 和 `nextID`，如果出现不一致的情况，请参照依赖关系重新调整，确保 step 的顺序描述的一致性。
* 最后做一次格式检查，要求输出的结果严格符合json的格式要求。

<!-- component end: GenChainRule -->
<!-- component start: ChainSchema -->
### ChainSchema
<<chain_schema>>
<!-- component end: ChainSchema -->