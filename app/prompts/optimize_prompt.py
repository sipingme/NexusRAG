from langchain.prompts import ChatPromptTemplate

class OptimizePrompt:
   def __init__(self, data):
      self.data = data

   def from_template(self):
      return ChatPromptTemplate.from_template(
      """
      根据上下文优化问题以提高回答准确性：
        
      ---
        
      **上下文**：{context}
        
      **原始问题**：{question}
        
      ---
        
      **优化策略**：
        
      1. **补充缺失的关键信息**：
         - 确认问题中是否遗漏了与上下文相关的重要细节。
         - 添加具体的背景信息，使问题更具针对性和深度。
         
      2. **明确模糊指代**：
         - 识别问题中的不明确指代词。
         - 使用明确的术语或具体名称替换模糊指代，以提高问题的清晰度。

      3. **保持专业术语**：
         - 确保使用适当的专业术语，以符合领域内的标准。
         - 保持问题的专业性和准确性。

      4. **考虑受众**：
         - 根据受众的知识水平、兴趣和需求调整问题的复杂度。
         - 确保语言风格适合目标受众，便于理解。

      5. **增强问题结构**：
         - 使用逻辑顺序和分段结构使问题更易于理解。
         - 如果问题复杂，考虑分解为多个部分以提高可读性。

      6. **引导深度思考**：
         - 设计问题以激发深入探讨和分析。
         - 使回答更详尽并具有意义。
         
      ---

      **优化后的问题**：
      """
   )