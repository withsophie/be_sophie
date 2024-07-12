# Studio Specification of View/Edit/Debug Mode 

## Terms Table

- **Chain**:
  - Node
  - Entity
  - Entity Graph
  - Entity Model
  - Thought Graph
  - Thought Model
- Studio **Mode**: 
  - View mode
  - Edit mode
  - Debug mode
  - Lock mode：extra features for Edit / Debug Mode
- Flow **Commands**：
  - Debug：点击进入Debug Mode，功能改为：Exit
  - Debug **History**
  - Publish：只在View Mode可用；
  - **Issues**：只在Debug Mode不可用；点击选择某个Issue后，Selection切换到该Node；
- **Entity**: Old Variable
  - In Entity, Out Entity: in chain flow
  - Knowledge Entity
  - ViewPoint Entity
  - Entity Types: Text(Tx), List(Ls), Dict(Dt)
- Flow **Node** & **Edge**：
  - **Control Node**：If-Else，Start，Concurrent
  - **Step Node**(Predicate): Think **Step**, **Tool**, Knowledge **Retriver**
  - **Edge**：Edge Start，Edge End
  - Node's Edge **Slot**：In Slot，Out Slot
  - **Bar**：
- Node **Floater**
  - Edit tab
  - **Test** tab: One-Step Node Executor
- Canvas **Toolbar**:
  - Hand Tool
  - Zoom Tool
  - New Node
- Canvas **Selection**: 
  - Node Selection
  - Edge Selection
- New Node List
- Debug Panel 
- Difine Entity Dialog

## Edge Actions
- Edge的hover状态下，显示Insert Node按钮，点击后显示New Node List对话框
- 无In Slot或无Out Slot的节点不允许插入
- 插入后，原Edge拆成两个，分别连接到新Node的第一个In/Out Slot
- 点击进入Selected状态（取消其他Canvas Selection），Delete和Backspace删除Edge

## Edge Vertify
- 存在Edge循环时，则非法
- 一个Node的Slot只能连接最多一个Edge
- 如新Edge合法，则删除两端Slot的原有Edge保证Slot合法

## Node Actions
- Click Node后，Node进入Selected状态
- 在Floater的修改，及时在Node中更新
- Drag Node时，Node当前Selected状态保持不变
- Double Click Node，进入Edit Lock Mode
- Right Click Node，弹出Node Menu

## Node Slot Actions
- Click Slot，弹出Node List，新建Node
- Drag一个新Edge到其他Node Slot，如果校验合法则新建Edge，否则取消新建Edge操作
- Drag一个新Edge到Canvas空白区域，释放后弹出Node List并新建Node并连接Edge

## Node Menus
- Test this Step：进入Edit Lock Mode，切换到Floater Test Tab
- Change Node：弹出Node List，选择后改变当前Node类型，数据情况，原Edge保持不变，不能保持的Edge则断开
- Copy：不做
- Delete：删除节点，原有Edge连接断开

## Node Bar
- Hover时临时显示Bar
- Selected状态时总显示Bar
- 所有Step Node都支持Bar，Control Node不支持
- Layout:
  - Test：进入Edit Lock Mode，自动切换到Floater Test Tab
  - Edit：进入Edit Lock Mode，当Node存在Issue时，按钮为红色底色
  - Menu：打开Node Menu

## Canvas Selection
- Canvas同时只能有一个Edge或Node处于Selected状态
- 如果Selection是Step Node，则Studio进入Edit Mode
- 点击Canvas空白区域，取消Selection
- Lock Mode下，只有特定控件允许点击
  
## Canvas Actions
- 鼠标滚轮，退出Edit Mode取消Selection后执行缩放；Debug Mode暂时禁用缩放；
- Drag拖动整个画布空白，退出Edit Mode取消Selection后执行缩放。Debug Mode暂时禁用此功能；
- Node和Edge随Canvas比例缩放，Floater不随比例缩放；
- Toolbar New Node点击后，弹出Node List，选择后，在New Node按钮上方放置新Node，不改变Selection；
- Right Click Canvas空白区域：Add Node（在鼠标位置弹窗并新建），Debug（进入Debug Mode）；
- Double Click Canvas，在鼠标位置弹窗Node List并新建；

## Canvas Lock Mode
- Debug Mode必须时Lock Mode，Edit Mode在明确指令下进入Lock Mode
- Lock Mode的Floater的右上角显示x按钮，必须点击x按钮退出Debug或Edit Mode
- Canvas的Stop等按钮，也退出Lock Debug/Edit Mode
- Lock Mode下，Canvas被半透明灰色蒙层遮盖，只有Selected Node，Floater，Flow Commands在蒙层之上可用
  
## Canvas Edit Mode
- 打开Selected Node的Floater，根据指令切换Edit或Test Tab；
- Floater编辑表单字段失去焦点时，更新Node数据；
- Edit tab和Test tab可随时切换 

## Canvas Debug Mode
- 注意：单节点Test功能是Edit Mode，只有Debug Chain才进入Debug Mode；
- Debug Mode必须时Lock Mode；
- 启动Flow Debug时，从Start Node开始，手动输入或调用历史初始化ViewPoint
- 从Start Node开始，按顺序执行；
- 当前Debug Node为Selected状态；
- Floater Test Tab有两个按钮：Test（参考Test Floater），Next；
- Click Next，重新执行当前步骤（或复用最新有效结果），Selection切换到下一个节点；
- End Node的Next按钮为Done按钮，点击后，清空Selection，退出Debug Mode；
- Debug Mode下，Debug Panel始终显示；

## Issues Check
- 所有Node必填字段缺失，记录一条Issue（Node ID，Field ID，Error Message）；
- Canvas的Issues List显示当前Issue总数，点击列出Issue List；
- Node标题右侧（右对齐）显示：Issue count+Issue Icon；

## Node Layout Schema
- Layout
``` Layout
TITLE      -> (slot)In Slot | (ico)Node Type | (title)Node Name | (txt)issue | (slot)Out Slot
IN-ENTITY  -> (slot)In Entity | (ico)Entify Type | (item)In Entity Name
OUT-ENTITY -> (ico)Entify Type | (item)Out Entify Name | (slot)Out Entity
PARAM      -> (ico)Parameter Icon | (txt)Parameter Name | (txt)Parameter Value | (slot)Out Slot
DESC       -> (desc)description
```
- 各种特定Node描述，会以行来作为组织单位，来定义Node或Floater的具体布局；
- 每个行中的组件，应该在具体Node的定义中，明确是否可选（隐藏）；
- Layout中只定义了内容组成，具体颜色，字号，对齐等，都在其他设计图中提供；
- 因为某些Node的布局可能是用户后续编辑的，所以布局存在设计时无法确定，需要规则辅助，如下：
  - 当一个布局的没有任何PARAM拥有Out Slot，则TITLE行添加Out Slot作为Node唯一Slot；

## Edit Floater Layout Schema
- Layout
``` Layout
TITLE      -> (title)Node Name | (tab)Edit/Test Switcher | (ico)close
IN-ENTITY  -> (category)In Entity
              (ico)Entify Type | (item)In Entity Name
OUT-ENTITY -> (category)In Entity
              (ico)Entify Type | (item)Out Entify Name
PARAM      -> (category)Item Name
              (txt)Item Value
DESC       -> (description)
```
- Item Value在新行显示，类型根据不同的Item类型改变，比如多行文本，单行文本，字典框
  - test -> https://icon-sets.iconify.design/tabler/variable/
  - list -> https://icon-sets.iconify.design/tabler/variable/ 暂时用这个，未来做方括号x来表达。
  - dict -> https://icon-sets.iconify.design/fluent/braces-variable-24-filled/

- 必须变量，控件显示浅红色边框，当内容不为空时，消失；

## Test Floater Layout Schema
- Floater Layout
``` Layout
TITLE      -> (title)step name | Edit/Test Tab | x(close)
IN-ENTITY  -> (item) In Entity ｜ (btn)History
IN-VALUE   -> (txtbox) Entity 
OUT-ENTITY -> (item) Out Entity 1 name
OUT-VALUE  -> (tbl) Entity 1
OUT-ENTITY -> (item) Out Entity 2 name
OUT-VALUE  -> (tbl) Entity 2
BTN        -> (btn)Test | (btn)Next
``` 
- Out Entify只在点击Test后出现；
- Edit Tab中发生任何改变，Test Tab中的所有OUT ENTITY重置清空；
- Next按钮只在Debug Mode中显示；
- Next按钮只在所有Out Entity不为空时可用；
- History Layout
``` Layout
HSTY-ITEM -> (txt)Newer Histroy Preview | (ico, right)Item Type
HSTY-ITEM -> (txt)Older Histroy Preview | (ico, right)Item Type
``` 
- 用户每次点击Test，则将In Entify的数值加入该Node的Test History；
- 用户每次点击Next，同理；
- History从新到旧排列，Preview为等款字符串，超长截断；
- History Type的预览方式为：
  - text：xxx
  - list：[xxx, xxx, xxx]
  - dict: a:xx, b:xx, c:xx

# Node Specification
- 以下内容为所有具体用途的Node和Floater定义
- 每个用途的Node和Floater只定义一份：
  - 定义中引用Layout Schema的类型
  - 用NF标志区分该行是否出现在Node或Floater中

## Knowledge Retriever Step
- (NF)  TITLE: Knowledge Retriever
- (NFR) PARAM: Query
- (F)   PARAM: Rename
- (NF)  OUT-ENTITY
- https://icon-sets.iconify.design/material-symbols/menu-book-outline-rounded/

## LLM Think Step Node & Floater
- (NF)  TITLE: Think Step #1
- (FR)  PARAM: LLM Model
- (NF)  PARAM: Prompt
- 键入/字符时，列表显示可用变量，最后一项为New Output Entity，点击后打开Entity Dialog
- Entity显示：（ico）Type，Name，绿色背景为IN，蓝色背景为OUT
- Entity Action：不能在内部走光标，hover时出现：（ico）edit，（ico）删除
- https://icon-sets.iconify.design/mage/stars-b/

## Start Control Node & Floater
- （F）VIEWPOINT
- （NF）USER ENTITY
- https://icon-sets.iconify.design/material-symbols/house-outline-rounded/

## End Control
- https://icon-sets.iconify.design/material-symbols/flag-circle-outline-rounded/

## Concurrent Control
- https://icon-sets.iconify.design/octicon/repo-forked-24/

## If-Else Control
- https://icon-sets.iconify.design/fluent/branch-fork-16-regular/
  
## Tool Step




