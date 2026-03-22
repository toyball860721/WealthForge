# App Store Connect 订阅配置详细指南

## ⚠️ 重要提示

在提交 App 审核之前，必须先完成以下步骤：
1. 在 App Store Connect 中创建订阅产品
2. 在 App 版本页面关联这些订阅
3. 然后才能上传构建版本并提交审核

---

## 📱 第一步：创建 App

1. 访问 https://appstoreconnect.apple.com
2. 点击"我的 App"
3. 点击左上角的"+"按钮
4. 选择"新建 App"
5. 填写信息：
   ```
   平台: iOS
   名称: Milestone
   主要语言: 英语（美国）
   Bundle ID: com.wealthforge.milestone
   SKU: milestone-ios-001
   用户访问权限: 完全访问权限
   ```
6. 点击"创建"

---

## 💰 第二步：创建订阅组

1. 在 App 页面，点击左侧菜单的"订阅"
2. 点击"创建订阅组"
3. 填写信息：
   ```
   组参考名称: milestone_premium_group
   组显示名称: Milestone Premium
   ```
4. 点击"创建"

---

## 📅 第三步：创建月度订阅

1. 在订阅组页面，点击"创建订阅"
2. 填写基本信息：
   ```
   产品 ID: milestone_monthly
   参考名称: Milestone Premium Monthly
   ```
3. 点击"创建"
4. 配置订阅详情：
   - **订阅时长**: 1 个月
   - **订阅价格**:
     - 点击"添加订阅价格"
     - 选择 $2.99 USD
     - 点击"下一步"
     - 确认所有地区的价格
     - 点击"创建"

5. 添加本地化信息（英文）：
   - 点击"订阅本地化"
   - 点击"添加语言"
   - 选择"英语（美国）"
   - 填写：
     ```
     显示名称: Premium Monthly
     描述: Unlock unlimited events, all themes, custom backgrounds, and iCloud sync
     ```
   - 点击"保存"

6. 配置免费试用：
   - 点击"订阅价格"
   - 找到 $2.99 的价格
   - 点击"添加优惠"
   - 选择"免费试用"
   - 时长：3 天
   - 点击"创建"

7. 点击右上角"保存"

---

## 📆 第四步：创建年度订阅

1. 返回订阅组页面
2. 点击"创建订阅"
3. 填写基本信息：
   ```
   产品 ID: milestone_yearly
   参考名称: Milestone Premium Yearly
   ```
4. 点击"创建"
5. 配置订阅详情：
   - **订阅时长**: 1 年
   - **订阅价格**:
     - 点击"添加订阅价格"
     - 选择 $19.99 USD
     - 点击"下一步"
     - 确认所有地区的价格
     - 点击"创建"

6. 添加本地化信息（英文）：
   - 点击"订阅本地化"
   - 点击"添加语言"
   - 选择"英语（美国）"
   - 填写：
     ```
     显示名称: Premium Yearly
     描述: Best value! Unlock all premium features and save 33%
     ```
   - 点击"保存"

7. 配置免费试用：
   - 点击"订阅价格"
   - 找到 $19.99 的价格
   - 点击"添加优惠"
   - 选择"免费试用"
   - 时长：7 天
   - 点击"创建"

8. 点击右上角"保存"

---

## ☕ 第五步：创建 Tip Jar 产品（消耗型）

### 产品 1: Small Tip

1. 在 App 页面，点击左侧菜单的"App 内购买项目"
2. 点击"创建 App 内购买项目"
3. 选择"消耗型"
4. 填写信息：
   ```
   产品 ID: tip_small
   参考名称: Small Tip
   ```
5. 点击"创建"
6. 配置价格：
   - 点击"价格"
   - 选择 $0.99 USD
   - 点击"下一步"
   - 确认所有地区的价格
   - 点击"创建"

7. 添加本地化信息（英文）：
   - 点击"App 内购买项目本地化"
   - 点击"添加语言"
   - 选择"英语（美国）"
   - 填写：
     ```
     显示名称: Buy me a coffee ☕
     描述: Support the developer with a small tip
     ```
   - 点击"保存"

8. 点击右上角"保存"

### 产品 2: Medium Tip

重复上述步骤，使用以下信息：
```
产品 ID: tip_medium
参考名称: Medium Tip
价格: $2.99 USD
显示名称: Buy me lunch 🍱
描述: Support the developer with a medium tip
```

### 产品 3: Large Tip

重复上述步骤，使用以下信息：
```
产品 ID: tip_large
参考名称: Large Tip
价格: $4.99 USD
显示名称: Buy me dinner 🍽️
描述: Support the developer with a large tip
```

---

## 🔗 第六步：关联订阅到 App 版本

1. 在 App 页面，点击左侧菜单的"App Store"
2. 在"iOS App"部分，点击"准备提交"（或你的版本号）
3. 向下滚动到"App 内购买项目和订阅"部分
4. 点击"+"按钮
5. 在弹出的列表中，选择：
   - ✅ Milestone Premium Monthly (milestone_monthly)
   - ✅ Milestone Premium Yearly (milestone_yearly)
   - ✅ Small Tip (tip_small)
   - ✅ Medium Tip (tip_medium)
   - ✅ Large Tip (tip_large)
6. 点击"完成"
7. 点击右上角"保存"

---

## ✅ 第七步：验证配置

确保所有产品状态为"准备提交"：

1. 检查订阅：
   - 进入"订阅"页面
   - 确认两个订阅都显示"准备提交"状态
   - 如果显示"缺少元数据"，点击进入补充信息

2. 检查 App 内购买项目：
   - 进入"App 内购买项目"页面
   - 确认三个 Tip Jar 产品都显示"准备提交"状态

3. 检查 App 版本关联：
   - 进入"App Store" > 你的版本
   - 确认"App 内购买项目和订阅"部分显示了 5 个产品

---

## 🚀 第八步：上传构建版本

现在你可以上传构建版本了：

1. 在 Xcode 中打开项目
2. 选择"Any iOS Device"作为目标
3. 点击菜单 Product > Archive
4. 等待 Archive 完成
5. 在 Organizer 窗口中，点击"Distribute App"
6. 选择"App Store Connect"
7. 选择"Upload"
8. 按照向导完成上传

---

## 📝 第九步：填写 App Store 信息

上传完成后，返回 App Store Connect：

1. 在 App 版本页面，选择刚上传的构建版本
2. 填写所有必需信息（使用 APP_STORE_CONTENT.md 中的内容）：
   - App 名称
   - 副标题
   - 描述
   - 关键词
   - 支持 URL
   - 营销 URL
   - 隐私政策 URL
   - 分类
   - 年龄分级
   - 审核信息

3. 上传截图（至少 3 张）

4. 点击"提交以供审核"

---

## ⚠️ 常见问题

### Q: 订阅显示"缺少元数据"
A: 确保已添加本地化信息（至少英文）和订阅价格

### Q: 无法关联订阅到 App 版本
A: 确保订阅状态为"准备提交"，不是"草稿"

### Q: 提交时提示"缺少订阅"
A: 确保在 App 版本页面的"App 内购买项目和订阅"部分已添加订阅

### Q: 免费试用如何配置？
A: 在订阅价格页面，点击"添加优惠"，选择"免费试用"

---

## 📞 需要帮助？

如果在配置过程中遇到问题，可以：
1. 查看 Apple 官方文档：https://developer.apple.com/app-store/subscriptions/
2. 联系 Apple 开发者支持
3. 告诉我具体的错误信息，我会帮你分析

---

## ✅ 配置完成检查清单

- [ ] App 已创建
- [ ] 订阅组已创建
- [ ] 月度订阅已创建并配置（$2.99，3天试用）
- [ ] 年度订阅已创建并配置（$19.99，7天试用）
- [ ] 3 个 Tip Jar 产品已创建
- [ ] 所有产品状态为"准备提交"
- [ ] 订阅已关联到 App 版本
- [ ] 构建版本已上传
- [ ] App Store 信息已填写完整
- [ ] 截图已上传
- [ ] 准备提交审核

完成所有步骤后，你就可以点击"提交以供审核"了！
