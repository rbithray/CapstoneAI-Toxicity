# **Conclusion**

## **Research Question 1**
_**How prone are Mistral 8x7B, LLaMA3, Gemma, and BLOOM to generating toxic outputs when prompted?**_

---

### **MUST: Quantitative Validation**
- We compared the models (Mistral 8x7B, LLaMA3, Gemma, and BLOOM) using the same set of prompts and the Perspective API for scoring.  
- **Key Finding:** All four models demonstrated the potential to generate toxic content, though the frequency and severity varied.  

---

### **SHOULD: Review Toxic Outputs**
- We reviewed the top 50 most toxic outputs from each model, examining not only the language used but also how the **nature and style of the prompt** influenced the model’s response. Our analysis revealed frequent instances of profanity, hate speech, and identity-based attacks—often mirroring or escalating the negativity implied by the prompt itself.  
- **Key Observation:** Automated tools like the Perspective API do not always capture the nuances of a prompt or its context (e.g., negation, sarcasm, or rhetorical framing), which can lead to mislabeling or overlooking certain toxic outputs. Even small variations in how a prompt is phrased can trigger notable shifts in toxicity.  
- **Implication:** Human oversight remains crucial to understanding the **connection between the prompt and the generated content**. By recognizing how prompts can elicit different types or degrees of toxicity, moderators and developers can better anticipate problematic responses and apply strategies—such as rephrasing prompts or content filtering—to mitigate harmful language.

---

### **COULD: Guidelines for Humans**
- We initially planned to create a comprehensive guideline for human evaluators and content moderators.  
- **Limitations:** Time and scope constraints prevented us from completing this step.  
- **Next Steps:** Developing practical strategies for preventing and reducing toxic outputs—such as identifying specific triggers and reframing prompts—could further refine moderation practices in the future.

---
