# Power to the Left, Knowledge to the Right
> Alex Sudo @ Aug 2024

The notion of Prompt Cache, as eloquently posited by its originators, is to precompute and cache the attention states of text segments that frequently emerge within the discourse on inference servers. This strategic foresight allows for the swift redeployment of these segments upon their recurrence in user prompts, thereby markedly enhancing operational efficiency.

The seminal contribution of this paper may well rival the historical impact of the Chain of Thought (CoT) framework, propelling the discipline of prompt engineering towards a more systematic and architecturally robust methodology. CoT logically delineates the necessity for a step-by-step analytical approach to complex problem-solving. Prompt Cache builds upon this by illustrating that such a systematic progression not only refines the efficacy of problem resolution but also streamlines processing velocity and mitigates computational expenditure.

For an extended period, my comprehension of prompt engineering within the realm of large language models (LLMs) has been akin to programming. In my perspective, prompts are tantamount to code; they represent a computer language with a more relaxed syntax, with the LLM assuming the dual role of compiler and runtime environment. This permissive syntax, while democratizing access through a lower learning threshold, concurrently engenders precision and operational velocity challenges. A retrospective on the evolution of programming languages reveals a trajectory from the stringent syntax of C to the almost conversational flexibility of Python. Computing's trajectory from specialized to generalized applications mirrors the development of programming languages, which oscillate between stringent and permissive paradigms.

The industry's predilection is to entrust tasks demanding rigor and reproducibility to computational prowess, as underscored in "The Bitter Lesson": "The most potent methodologies are those predicated on generalized computation." Nonetheless, this methodology, while effective, is not immune to the introduction of bugs and inefficiencies stemming from ambiguity. In the quest to unravel intricate problems, humanity must either harness knowledge to augment performance or escalate computational resources. Essentially, computational science endeavors are inherently about discovering equilibrium between these dichotomous factors, customized to the exigencies of the issue at hand.

A considerable faction within OpenAI harbors a radical perspective on AI, echoing the views of Rich Sutton:

1. AI researchers frequently endeavor to inculcate knowledge into their agents,
2. This approach is invariably beneficial in the short term and gratifying to the researchers,
3. Yet, over the long haul, it might reach a plateau or even impede advancement,
4. Innovations are more likely to emerge from methodologies that expand computational horizons through exploration and learning, albeit with a tinge of bittersweet success that is not universally celebrated due to its departure from a human-centric methodology.

When viewed through the lens of technological progression, entities like OpenAI, with their pronounced reliance on computational power, could be characterized as "left-leaning," in contrast to those favoring human expertise and knowledge, embodying a more conservative "right-leaning" stance. OpenAI's principal rival, Anthropic, has unmistakably opted for a path more congruent with the right-leaning ideology. Anthropic’s CEO, Dario Amodei, formerly oversaw safety at OpenAI, where the quintessential concern with large models is their enigmatic black-box character. This tenure has indubitably influenced his worldview, prompting a divergence from OpenAI's trajectory upon his departure. Claude Bisson, in stark contrast, appears to prioritize integration with established knowledge, diminished reliance on sheer data volume, and an accentuated focus on trustworthiness.

As an individual unaffiliated with AI science and model development, is it incumbent upon us to grapple with the dichotomous evolution of AI technology? Be it a black-box or white-box model, if it yields satisfactory responses, does it not qualify as a commendable model? Developers of agents might be predisposed to select the model that strikes the optimal balance between cost and efficacy, given the negligible cost of switching allegiances. However, I am persuaded that the bifurcation in AI technology will exert a profound influence on the intrinsic nature of AI applications. I have delineated several contentious issues within the industry, and the responses to these may diverge significantly between advocates of computation ("left-wing") and proponents of knowledge-based methodologies ("right-wing"). These queries may even foreshadow the archetypal form that AI products ought to assume.

| **Question**                                | **Left-wing Perspective** | **Right-wing Perspective** |
| ------------------------------------------ | ------------------------- | -------------------------- |
| Why do people distrust AI-generated content? | Degree of content-need alignment | Explainability of the response  |
| How should AI and humans coexist?           | AI replaces human tasks   | AI assists human tasks     |
| How should AIGC (AI-generated content) be constrained? | Avoid lying               | Avoid making things up     |
| What are the data requirements for further AI training? | More multimodal data      | Higher-quality data        |
| What impact will AI have on social structures? | Increased polarization    | General enhancement of capabilities |


The world is not strictly binary, and most AI professionals possess the cognitive capacity to entertain divergent viewpoints and seek equilibrium. While the actual solution may reside in the intermediate shades of gray, exploring the extremes—be it left or right—can provide invaluable insights through thought experiments. Thus, when introducing new technologies or crafting products, situating oneself along this spectrum can aid in guiding future refinements as one's approach matures.

