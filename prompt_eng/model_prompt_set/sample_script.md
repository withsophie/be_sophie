prompt_name: "Goal Pursuit Analysis Prompt"
description: "根据用户的问题判断其属于哪一个目标追求象限（时间取向 vs 权力来源）并进行分析"
input:

- user_question: string  # 用户的问题或描述
  output:
- quadrant: enum[quadrant_I, quadrant_II, quadrant_III, quadrant_IV]
- reasoning: string  # 归类的理由
- quadrant_description: string  # 对该象限内行为模式的简要描述
- possible_actions: string  # 针对该象限的推荐行为策略
  task_steps:

1. 从用户描述中识别其在“时间取向”（future or past）和“权力来源”（internal or external）上的偏好；
2. 确定对应的象限；
3. 给出归类的逻辑说明；
4. 补充该象限下常见人物特征与推荐的行动策略。
