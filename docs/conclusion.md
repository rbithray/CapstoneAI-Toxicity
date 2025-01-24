# **Conclusion**

## **Research Question 1**

_**How prone are Mistral 7B, LLaMA3, Gemma, and BLOOM to generating toxic outputs when prompted?**_

---

### **MUST: Quantitative Validation**

- We compared the models (Mistral 7B, LLaMA3, Gemma, and BLOOM) using the same set of prompts and the Perspective API
  for scoring.
- **Key Finding:** All four models demonstrated the capacity to generate toxic content, although the results suggest
  that **only around 5%** of their responses were toxic based on our dataset.

---

### **SHOULD: Review Toxic Outputs**

- We reviewed the top 50 most toxic outputs from each model, paying close attention to **the toxicity of the prompts
  themselves** as well as the generated responses. Often, prompts containing explicit hate speech, profanity, or
  derogatory language significantly increased the likelihood of toxic outputs.
- **Key Observation:** Automated tools like the Perspective API do not always capture the nuances of prompts or their
  context (e.g., negation, sarcasm, or rhetorical framing), which can lead to mislabeling or overlooking certain toxic
  outputs. Even subtle variations in prompt wording can cause notable changes in toxicity levels.
- **Implication:** Human oversight remains crucial for interpreting the **connection between a prompt’s inherent
  toxicity and the model’s generated content**. Recognizing that toxicity can arise from both prompt design and model
  biases highlights the importance of carefully crafting prompts—or employing filtering mechanisms—to reduce harmful
  responses.

---

### **COULD: Guidelines for Humans**

- We initially planned to create a comprehensive guideline for human evaluators and content moderators.
- **Limitations:** Time and scope constraints prevented us from completing this step.
- **Next Steps:** Developing practical strategies for preventing and reducing toxic outputs—such as identifying specific
  prompts or phrases that frequently trigger toxicity—could help refine moderation practices in the future.

---

### **Answering the Research Question**

In summary, **all four models—Mistral 7B, LLaMA3, Gemma, and BLOOM—are capable of producing toxic outputs**. However,
our analysis indicates that **the overall incidence of toxic responses was around 4%**. Importantly, prompts containing
offensive or hateful language strongly influenced the resulting toxicity. These insights underscore the need for
continued research into **prompt design**, toxicity detection, and human-in-the-loop moderation to effectively identify
and mitigate harmful content.
