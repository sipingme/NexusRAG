# Git 提交规范
feat: 新功能
fix: 修复 bug
docs: 文档更新
style: 代码格式调整（不影响代码运行）
refactor: 代码重构（既不是新功能也不是 bug 修复）
perf: 性能优化
test: 测试相关
build: 构建系统或外部依赖变更
ci: CI 配置变更
chore: 其他不修改源代码或测试的变更
revert: 回滚提交

## 提交消息格式
<类型>[可选的作用域]: <描述>

[可选的正文]

[可选的脚注]

## 示例
### feat(auth): 添加 JWT 认证支持
- 添加 jwt 依赖
- 实现 JWT 认证中间件
- 更新认证文档

Closes #123

### fix(db): 修复连接池内存泄漏
当连接异常时未正确释放连接导致内存泄漏，
现在在 finally 块中确保连接释放。

Fixes #45

### 版本兼容性变更
feat: 添加 Python 3.10 支持

放弃对 Python 3.6 的支持

### 依赖变更：添加/移除依赖时明确说明
chore(deps): 添加 requests 2.25.0 依赖

### 类型提示
refactor(types): 为 utils 模块添加类型提示