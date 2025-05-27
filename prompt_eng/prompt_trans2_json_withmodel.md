## 生成规则

**术语：**

* 思路构思：{{Chain_draft}}
* 数据字典：{{Datadic}}
* Model说明：用户选择的Model的原始定义文件{{Model}}
* ModelInstance：{{ModelInstance}}

**Step 1：通过Model说明，理解所选择的 Model**

* 通过它的ref_domain确定这个思路的问题域
* name作为这个思路的名称，modeId使用Model说明的ID

**Step 2：确认变量**

* 根据{{Chain_draft}}，结合{{Model}}的结构，对这个思路构思进行深入理解，将所有可能用到的元素生成entity和relation，
* 将所有entity和relation都生成为变量，
* 变量的命名方法：名称为entity/relations的ID，ID由Model说明中的entity/relations的ID和Modelid共同组成，Modelid在后面，以:分割
* 所有变量必须依次记录进 `varList`（即变量清单）。
* 用户提供的第一个变量固定命名为 `ThinkPoint`。

**Step 3：理清变量生成的因果顺序**

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

**Step 4：构建分步逻辑链**

* 将整个 Prompt 拆解为多个步骤（step）。
* 根据依赖关系来构建步骤和步骤之间的关系。
* 每一步能使用多个输入变量，只能生成一个输出变量，输入变量和输出变量在 prompt 里面的使用需要符合格式规定，用 `{{}}` 扩起来。
* 每一步的 Prompt 指令应根据输入/输出逻辑改写。
* 每一步必须产出一个明确的结果，且这个结果需要赋值给输出变量，这个赋值动作需要在步骤的 prompt 写出来。
* 每个变量生成完毕后写入 `varList`。
* step中的最后一个步骤，其类型应该为10，且应该形成modeVarMap中对变量的映射，映射方式应参考模型中的描述，只选最必需的变量映射，无需将所有变量映射进去，modeVarMap中的ModeVarName，请根据变量名称中的:后面的Modelid定义。

**Step 5：去除格式相关的规约**

* 只保留内容相关的生成规则。
* 每一步只描述思维转换、生成机制。

**Step 6：以符合数据字典的 JSON 输出结果**

* 输出为一个整体思路级 JSON 对象，字段必须参考数据字典，只为必填字段赋值。

  * 依赖关系不作为 JSON 内容输出。
  * 检查所有 step 中的 `preID` 和 `nextID`，如果出现不一致的情况，请参照依赖关系重新调整，确保 step 的顺序描述的一致性。
