from langchain.prompts import ChatPromptTemplate

class AnswerPrompt:
    def from_template(self):
        return ChatPromptTemplate.from_template(
            """
            为确保提供准确、详尽且高质量的答案，请遵循以下步骤：

            1. **上下文分析**:
            - 仔细阅读并理解相关上下文。
            - 提取出其中的核心主题、数据和关键信息。

            2. **全面研究**:
            - 搜索来自多种可信来源的信息，包括学术文章、行业报告和新闻报道。
            - 确保信息的多样性和广泛性以覆盖不同角度。

            3. **信息验证**:
            - 对收集的信息进行验证，确保其来源可靠且内容准确。
            - 排除任何不实或偏颇的数据。

            4. **信息整合**:
            - 将上下文与补充信息进行整合，确保各方面内容的协调。
            - 进行深入的分析以形成一个全面的回答。

            5. **结构化答案**:
            - 清晰地组织答案内容，确保逻辑性和易于理解。
            - 使用分段和标号以提高可读性。

            6. **支持性示例**:
            - 提供具体示例来说明和增强你的分析。
            - 确保示例相关且能有效支持论点。

            7. **持续更新**:
            - 保持对相关领域的最新发展动态的关注，以便提供最新的信息。

            相关上下文：{context}

            问题：{question}
        
            答案：
            """
        )