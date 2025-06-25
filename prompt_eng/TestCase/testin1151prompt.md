# Generate-Chain-withModel Prompt
## 综述
这是一个通过预先设计好的思路模型，来辅助用户生成思路的prompt。在这个生成的过程中，需要用到的概念和定义有下面几种：
### 思路构思（chain_draft）
``` txt
你需要帮助一个团队分析他们在“创新能力”和“执行力”两个维度上的表现。请将团队成员按照这两个维度分布到四个象限中：




- X轴代表“创新能力”，右侧为高创新，左侧为低创新；

- Y轴代表“执行力”，上方为高执行，下方为低执行。




请根据以下团队成员的描述，将他们分配到合适的象限，并说明每个象限的典型特征：




1. 张三：善于提出新想法，但执行力一般；

2. 李四：创新能力一般，但执行力很强；

3. 王五：既有创新能力，也能很好地推动落地；

4. 赵六：创新和执行都比较弱。




请进一步分析：

- 哪些成员之间存在“X轴对称关系”（即创新能力相反但执行力相同）？

- 哪些成员之间存在“Y轴对称关系”（即执行力相反但创新能力相同）？

- 哪些成员之间属于“对角线反转关系”？

- 如果要提升团队整体表现，建议优先关注哪个象限的成员？为什么？




请用“二元正交象限模型”对上述问题进行结构化分析，并给出每个象限的名称、代表成员、典型特征和改进建议。
```
### 模型定义 （entity_of_model）
``` json
 {
    "model": {
      "index": "G1",
      "id": "binary_orthogonal",
      "name": "Binary Orthogonal",
      "ref_domain": "geometry",
      "visual": "quadrant",
      "visual_prompt": "",
      "description": "A quadrant model using two conceptual axes (X and Y) to form four composite quadrant entities.",
      "inherits": "base_model",
      "entities": [
        {
          "id": "{{axis_x}}",
          "name": "{{axis_x}}",
          "prototype": "axis",
          "define_baseset": ["primitive"],
          "define_prompt": "The X-axis representing opposing conceptual vectors.",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{axis_y}}",
          "name": "{{axis_y}}",
          "prototype": "axis",
          "define_baseset": ["primitive"],
          "define_prompt": "The Y-axis representing another set of conceptual vectors.",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{x_positive}}",
          "name": "{{x_positive}}",
          "prototype": "vector",
          "define_baseset": ["{{axis_x}}"],
          "define_prompt": "Positive direction on X-axis. (e.g., future on a time axis, advantage in a competition)",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{x_negative}}",
          "name": "{{x_negative}}",
          "prototype": "vector",
          "define_baseset": ["{{axis_x}}"],
          "define_prompt": "Negative direction on X-axis. (e.g., past on a time axis, disadvantage in a competition)",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{y_positive}}",
          "name": "{{y_positive}}",
          "prototype": "vector",
          "define_baseset": ["{{axis_y}}"],
          "define_prompt": "Positive direction on Y-axis. (e.g., growth, opportunity)",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{y_negative}}",
          "name": "{{y_negative}}",
          "prototype": "vector",
          "define_baseset": ["{{axis_y}}"],
          "define_prompt": "Negative direction on Y-axis. (e.g., decline, threat)",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{quadrant_I}}",
          "name": "{{quadrant_I}}",
          "prototype": "quadrant",
          "define_baseset": ["{{x_positive}}", "{{y_positive}}"],
          "define_prompt": "First quadrant (X positive, Y positive).",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{quadrant_II}}",
          "name": "{{quadrant_II}}",
          "prototype": "quadrant",
          "define_baseset": ["{{x_negative}}", "{{y_positive}}"],
          "define_prompt": "Second quadrant (X negative, Y positive).",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{quadrant_III}}",
          "name": "{{quadrant_III}}",
          "prototype": "quadrant",
          "define_baseset": ["{{x_negative}}", "{{y_negative}}"],
          "define_prompt": "Third quadrant (X negative, Y negative).",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{quadrant_IV}}",
          "name": "{{quadrant_IV}}",
          "prototype": "quadrant",
          "define_baseset": ["{{x_positive}}", "{{y_negative}}"],
          "define_prompt": "Fourth quadrant (X positive, Y negative).",
          "occur": 1,
          "inherits": "base_entity"
        },
        {
          "id": "{{x_flip}}",
          "name": "{{x_flip}}",
          "prototype": "symmetry",
          "define_baseset": ["axis_x"],
          "define_prompt": "Horizontal axis symmetry—conversion between positive and negative X (e.g., Quadrant I <-> IV, II <-> III).",
          "occur": "1+",
          "inherits": "base_relation"
        },
        {
          "id": "{{y_flip}}",
          "name": "{{y_flip}}",
          "prototype": "symmetry",
          "define_baseset": ["axis_y"],
          "define_prompt": "Vertical axis symmetry—conversion between positive and negative Y (e.g., Quadrant I <-> II, IV <-> III).",
          "occur": "1+",
          "inherits": "base_relation"
        },
        {
          "id": "{{diagonal_reverse}}",
          "name": "{{diagonal_reverse}}",
          "prototype": "symmetry",
          "define_baseset": ["x_flip", "y_flip"],
          "define_prompt": "Diagonal reverse—equivalent to applying both x_flip and y_flip in sequence. Maps Quadrant I (++) to Quadrant III (--), i.e., both axes flipped.",
          "occur": "1+",
          "inherits": "base_relation"
        },
        {
          "id": "{{diagonal_swap}}",
          "name": "{{diagonal_swap}}",
          "prototype": "symmetry",
          "define_baseset": ["x_flip", "y_flip"],
          "define_prompt": "Diagonal swap—equivalent to applying both x_flip and y_flip in sequence. Maps Quadrant II (-+) to Quadrant IV (+-), i.e., both axes flipped but swaps the off-diagonal quadrants.",
          "occur": "1+",
          "inherits": "base_relation"
        }
      ]
    }
  }
```
### 思路概述 （chain_agenda)
#### GenChainAgenda
通过理解ModelInstance中的内容，生成思路概述(chain_agenda)，这个思路概述(chain_agenda)的格式是：
通过对您构思的理解，我们会帮您创建一个解决这类问题的思路，并展现在画布中，您可以在这个基本思路的基础之上，进行进一步的修改。
思路名称： testin1151 
思路领域：ModelInstance中的domain
思路所采用的模型：Binary Orthogonal Model，并介绍一下这个模型的特点
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
### 模型实例生成规则(GenModelInstance)
运用合适的思维模式（思路）进行思考，是一个将抽象的Model和具体要解决的问题相结合，经过逐步的具象化，形成一个具体的关于这个问题的entity组，并将这些entity里面的value，组合成一个合适的答案的过程。整个过程可以理解为一个main函数的执行过程，而思路就是这个main函数中的函数体部分，构建思路就是构建其中的函数体。其中entity的值，则是这个main函数在执行过程中需要调用的常量和变量，而赋值的过程则是entity函数。main函数的返回值就是这次思考的最终结果，思考时的背景信息被称作ThinkPoint，是main函数执行的输入参数。
构建思路的过程是这样的：
1、根据Model的框架设计，实现所有的entity函数，这个具体实现的entity函数库，被称为ModelInstance
2、选择在思路中需要使用的entity，设计这些entity的value是如何通过对thinkpoint的计算来最终实现问题答案的。（设计main函数的函数体）
3、构建返回值，也就是针对计算后的entity的value，选择合适的显示方案。
#### 根据Chain_draft的内容对entity_yaml_of_model的内容进行实例化，生成ModelInstance的内容：
1、判断其涉及的领域，生成domain，这个领域应具备一定的抽象性；
2、深入理解Chain_draft中的内容，并根据如下规则，实例化entity_yaml_of_model中的entites,为这些属性赋值
* 顺序先从define_baseset为[primitive]的entity开始
* id：在原entity的id的基础上增加一个可以表达该entity的实体的词，用_分割开
* name：能表达该entity的实体的词
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
#### 重构ModelInstance中的actual_entity
* 将ThinkPoint加入entity的define_baseset
* 根据chain_draft的内容和新的define_baseset，重新构建entity的define_prompt
* 构建prompt的一些示例：
 * 将thinkpoint中符合baseset条件的内容筛选出，构建成列表，作为entity的value
 * 将thinkpoint和原baseset以某种形式进行结合，综合形成一个新的内容，作为entity的value
 * thinkpoint是待加工内容，baseset是加工方法，加工结果存入entity的value

#### 生成模型实例（ModelInstance）
将上面生成的结果形成一个json格式的ModelInstance
### 思路生成规则(GenChain)
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
### 思路格式规约
## ChainSchema
 {
  "rootObject": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "description": "思路 ID，唯一标识一个思路",
        "example": "思路 ID"
      },
      "trainName": {
        "type": "string",
        "description": "思路名，根据 prompt 的作用设计简短易记的名称",
        "example": "内容总结助手"
      },
      "trainDesc": {
        "type": "string",
        "description": "思路描述，描述其具体功能和应用场景",
        "example": "此思路用于快速总结长文本的主要内容。"
      },
      "welcomeMessage": {
        "type": "string",
        "description": "思路欢迎语，向用户表达输入内容或如何开始使用该思路",
        "example": "请输入您想总结的文本内容："
      },
      "summary": {
        "type": "string",
        "description": "对整个思路的功能或成果的总结性描述"
      },
      "modelId": {
        "type": "string",
        "description": "模式 ID，基于特定模式创建时记录模式的 ID",
        "example": "模式 ID"
      },
      "stepList": {
        "type": "array",
        "items": {
          "$ref": "#/definitions/Step Object"
        },
        "description": "思路过程中的步骤列表",
        "default": []
      },
      "varList": {
        "type": "array",
        "items": {
          "$ref": "#/definitions/Variable Object"
        },
        "description": "实体变量列表，存储步骤间传递和使用的变量",
        "default": []
      },
      "termList": {
        "type": "array",
        "items": {
          "$ref": "#/definitions/Term Object"
        },
        "description": "术语列表，定义在当前思路的 prompt 或步骤中明确使用的术语",
        "default": []
      }
    }
  },
  "definitions": {
    "Step Object": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "步骤 ID，唯一标识一个步骤",
          "example": "步骤 ID"
        },
        "preId": {
          "type": "string",
          "description": "前步骤 ID，多个用逗号分隔",
          "default": "",
          "example": "stepId_A,stepId_B"
        },
        "nextId": {
          "type": "string",
          "description": "后步骤 ID，多个用逗号分隔; stepType != 10 时必须有有效的下一步步骤ID ",
          "default": "",
          "example": "stepId_C,stepId_D"
        },
        "trainId": {
          "type": "string",
          "description": "所属思路的 ID",
          "example": "思路 ID"
        },
        "stepType": {
          "type": "integer",
          "description": "步骤类型（1-思考步骤,  9-起始节点, 10-结束节点,12-if-else步骤）",
		  "example": 1,
          "enum": [1, 9, 10, 12]
        },
        "stepName": {
          "type": "string",
          "description": "步骤名称",
          "example": "提取关键信息"
        },
        "stepDesc": {
          "type": "string",
          "description": "步骤描述，对步骤功能的详细描述",
          "example": "此步骤用于从输入文本中提取关键信息点。"
        },
        "stepInVars": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "输入变量数组，步骤执行所需的输入变量名称列表",
          "default": [],
          "example": ["inputText"]
        },
        "stepOutVars": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "输出变量数组，步骤执行后产生的输出变量名称列表,但每个步骤只有1个输出变量",
          "default": [],
          "example": ["keyInfo"]
        },
        "stepTerms": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "步骤用到的术语数组",
          "default": [],
          "example": ["核心观点", "主要论据"]
        } 
      },
      "anyOf": [
		  {
		   "if": {
				"properties": {
				  "stepType": {
					"const": 1
				  }
				}
			  },
			  "then": {
				"properties": {
				  "stepPrompt": {
					"type": "string",
					"description": "步骤 prompt，用于指导大模型生成内容的具体提示文本",
                    "example": "请总结以下文本的主要观点：{{inputText}}"
				  }
				}
			  }
			},
         { 
		   "if": {
				"properties": {
				  "stepType": {
					"const": 12
				  }
				}
           },
          "then": {
				"properties": {
				  "cases": {
					"type": "array",
					"items": {
					  "$ref": "#/definitions/Case Object"
					},
					"description": "条件列表（if-else 步骤类型的条件列表）",
					"default": []
				  }
				}
          }
        },
        {
          "if": {
            "properties": {
              "stepType": {
                "const": 10
              }
            }
          },
          "then": {
            "properties": {
              "modelVarMap": {
                "type": "array",
                "items": {
                  "$ref": "#/definitions/Mode Variable Map Object"
                },
                "description": "变量映射关系（结束节点时适用）"
              },
              "trainModelGraphPrompt": {
                "type": "string",
                "description": "使用模式的 graphprompt（结束节点时适用）"
              },
              "generationPrompts": {
                "type": "array",
                "items": {
                  "$ref": "#/definitions/Generation Prompt Object"
                },
                "description": "多种 graphprompt（结束节点时适用）",
                "default": []
              }
            }
          }
        }
      ]
    },
    "Case Object": {
      "type": "object",
      "properties": {
        "nextId": {
          "type": "string",
          "description": "指向步骤 ID，条件分支满足后流程应跳转到的下一步骤 ID",
          "example": "stepId_TrueBranch"
        },
        "logicalOperator": {
          "type": "string",
          "description": "逻辑类型 (and | or)",
		  "enum": ["and","or"],
          "default": "and",
          "example": "and"
        },
        "id": {
          "type": "string",
          "description": "if-else case 的唯一 ID",
          "example": "ifElse_688adffe-4d8d-4d16-8f20-20f2880f2587"
        },
        "conditions": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Condition Object"
          },
          "description": "条件数组，定义当前 case 的具体条件",
          "default": []
        },
        "caseType": {
          "type": "integer",
          "description": "Case 类型（0 - if, 1 - else_if, 2 - else）",
          "example": 0
        }
      }
    },
    "Condition Object": {
      "type": "object",
      "properties": {
        "varType": {
          "type": "string",
          "description": "变量类型",
          "example": "1"
        },
        "varName": {
          "type": "string",
          "description": "变量名称",
          "example": "ThinkPoint"
        },
        "comparisonOperator": {
          "type": "string",
          "description": "比较操作符",
          "enum": ["is","isNot","contains","notContains","startWith","endWith","isEmpty","isNotEmpty"],
          "example": "contains"
        },
        "value": {
          "type": "string",
          "description": "用于比较的值",
          "default": ""
        }
      }
    },
    "Mode Variable Map Object": {
      "type": "object",
      "properties": {
        "varName": {
          "type": "string",
          "description": "实体变量名",
          "example": "总结结果"
        },
        "modelVarId": {
          "type": "integer",
          "description": "模式变量 ID，对应模式中定义的变量 ID",
          "example": 123
        },
        "modelVarName": {
          "type": "string",
          "description": "模式变量名称",
          "example": "模式输出变量 1"
        },
        "varId": {
          "type": "integer",
          "description": "实体变量 ID",
          "example": 123
        }
      }
    },
    "Generation Prompt Object": {
      "type": "object",
      "properties": {
        "VarId": {
          "type": "integer",
          "description": "唯一 ID",
          "example": 123
        },
        "trainId": {
          "type": "integer",
          "description": "思路标识",
          "example": 417
        },
        "stepId": {
          "type": "string",
          "description": "步骤 ID",
          "example": "1919683135748886528"
        },
        "generationType": {
          "type": "string",
          "description": "生成类型",
          "example": "Chat"
        },
        "stepInVars": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "此提示的输入变量",
          "default": [],
          "example": ["sourceText"]
        },
        "stepTerms": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "此提示中使用的术语",
          "default": [],
          "example": ["AI", "机器学习"]
        },
        "stepPrompt": {
          "type": "string",
          "description": "提示文本",
          "example": "请根据以下内容生成一张 SVG 图：{{sourceText}}"
        }
      }
    },
    "Variable Object": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "唯一 ID",
          "example": 15104
        },
        "trainId": {
          "type": "integer",
          "description": "思路标识",
          "example": 417
        },
        "parentId": {
          "type": "string",
          "nullable": true,
          "description": "父 ID，变量具有层级关系时记录父变量 ID"
        },
        "stepId": {
          "type": "string",
          "description": "与此变量关联的步骤 ID",
          "example": "1909528709373546496"
        },
        "varType": {
          "type": "integer",
          "description": "变量类型",
          "example": 1
        },
        "varLevel": {
          "type": "integer",
          "description": "变量级别",
          "default": 0,
          "example": 0
        },
        "varName": {
          "type": "string",
          "description": "变量名称，在 prompt 中通常用 {{varName}} 的形式引用",
          "example": "ThinkPoint"
        },
        "varDesc": {
          "type": "string",
          "description": "变量描述",
          "example": "Anything you wish to think about using a chain of thought."
        },
        "varFormat": {
          "type": "string",
          "description": "变量格式",
          "default": "",
          "example": "YYYY-MM-DD"
        },
        "defaultValue": {
          "type": "string",
          "nullable": true,
          "description": "默认值"
        },
        "childs": {
          "type": "array",
          "nullable": true,
          "description": "子变量（用于层级数据）",
          "items": {
            "$ref": "#/definitions/Variable Object"
          }
        }
      }
    },
    "Term Object": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "唯一 ID",
          "example": 767
        },
        "trainId": {
          "type": "integer",
          "description": "思路标识",
          "example": 417
        },
        "name": {
          "type": "string",
          "description": "术语名称",
          "example": "terrrrrr"
        },
        "description": {
          "type": "string",
          "description": "术语描述",
          "default": "",
          "example": "人工智能的简称"
        }
      }
    }
  }
}
### 思路文件（chain_json）
思路文件是一个严格符合思路格式规约schema的json文件。

## 生成步骤
生成思路的具体步骤是：
1、用户为该思路命名为： testin1151 
2、用户选择合适的模型定义：Binary Orthogonal Model
3、用户输入自己对这个思路的思路构思
4、深入理解用户的思路构思，套用模型定义，将思路构思中的内容形成模型实例，具体的套用方法需要遵循模型实例生成规则
5、将模型实例根据思路概述的方法，形成思路概述（chain_agenda）
6、将模型实例按照思路格式规约的要求，生成思路文件（chain_json）
7、请将思路文件（chain_json）严格按照以下JSON格式返回结果，不要添加任何额外的解释、注释或markdown标记：
format examples:
{
  "rootObject": value is chain_json
}