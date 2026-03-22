# In-App Purchase 配置指南

## 在 App Store Connect 中配置 IAP

### 1. 订阅产品

#### 订阅组
- 名称: Milestone Premium
- 参考名称: milestone_premium_group

#### 月度订阅
- 产品 ID: `milestone_monthly`
- 参考名称: Milestone Premium Monthly
- 订阅时长: 1 个月
- 价格: $2.99 USD
- 免费试用: 3 天
- 介绍性优惠: 可选（首月 $0.99）

#### 年度订阅
- 产品 ID: `milestone_yearly`
- 参考名称: Milestone Premium Yearly
- 订阅时长: 1 年
- 价格: $19.99 USD（节省 33%）
- 免费试用: 7 天
- 介绍性优惠: 可选（首年 $14.99）

### 2. Tip Jar（消耗型产品）

#### 小额打赏
- 产品 ID: `tip_small`
- 参考名称: Small Tip
- 类型: 消耗型
- 价格: $0.99 USD

#### 中额打赏
- 产品 ID: `tip_medium`
- 参考名称: Medium Tip
- 类型: 消耗型
- 价格: $2.99 USD

#### 大额打赏
- 产品 ID: `tip_large`
- 参考名称: Large Tip
- 类型: 消耗型
- 价格: $4.99 USD

## 本地化信息

### 订阅显示名称和描述

**英文 (en-US):**
- 月度订阅名称: Premium Monthly
- 月度订阅描述: Unlock unlimited events, all themes, custom backgrounds, and iCloud sync
- 年度订阅名称: Premium Yearly
- 年度订阅描述: Best value! Unlock all premium features and save 33%

**中文 (zh-CN):**
- 月度订阅名称: 高级版（月度）
- 月度订阅描述: 解锁无限事件、所有主题、自定义背景和 iCloud 同步
- 年度订阅名称: 高级版（年度）
- 年度订阅描述: 最超值！解锁所有高级功能，节省 33%

### Tip Jar 显示名称

**英文:**
- Small Tip: Buy me a coffee ☕
- Medium Tip: Buy me lunch 🍱
- Large Tip: Buy me dinner 🍽️

**中文:**
- Small Tip: 请我喝杯咖啡 ☕
- Medium Tip: 请我吃顿午餐 🍱
- Large Tip: 请我吃顿晚餐 🍽️

## 审核信息

### 订阅审核信息
- 截图: 显示订阅页面的截图
- 审核说明:
  - 免费版限制: 最多 3 个倒计时事件
  - 订阅后解锁: 无限事件、所有主题、自定义背景、iCloud 同步
  - 可以通过 Settings > Restore Purchases 恢复购买

### 隐私信息
- 订阅数据收集: 仅用于验证购买，不收集个人信息
- 使用 RevenueCat SDK 管理订阅（匿名数据）

## 测试

### 沙盒测试账号
在 App Store Connect 中创建沙盒测试账号用于测试 IAP

### 测试清单
- [ ] 月度订阅购买流程
- [ ] 年度订阅购买流程
- [ ] 免费试用期验证
- [ ] 订阅自动续费
- [ ] 取消订阅
- [ ] 恢复购买功能
- [ ] Tip Jar 购买流程
- [ ] 订阅状态在多设备间同步

## 注意事项

1. **RevenueCat 集成**
   - 需要在 RevenueCat 中配置相同的产品 ID
   - 获取 RevenueCat API Key
   - 在 App 中集成 RevenueCat SDK

2. **App Store Connect 配置**
   - 确保所有产品状态为"准备提交"
   - 上传订阅页面截图
   - 填写订阅审核信息

3. **税务和银行信息**
   - 确保已在 App Store Connect 中完成税务表格
   - 配置银行账户信息以接收付款

4. **定价策略**
   - 月度 $2.99 × 12 = $35.88/年
   - 年度 $19.99 = 节省 $15.89 (44%)
   - 这个定价策略鼓励用户选择年度订阅
