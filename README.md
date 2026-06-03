# 攻略及机位大全 🌍

一个集成江浙沪旅游攻略、打卡机位和实时餐厅排号的综合性旅游服务平台。

## 🌟 核心特性

- ✅ **攻略聚合** - 汇总小红书、抖音、携程、马蜂窝等平台的旅游攻略
- 📍 **打卡机位** - 展示景点周边的最佳摄影位置  
- 🗺️ **交互式地图** - 展示景点、餐厅和打卡机位
- 🍽️ **餐厅信息** - 聚合周边餐厅和实时排号数据
- 🔄 **实时更新** - 定时爬取各平台最新内容
- 📱 **响应式设计** - 完美适配各类设备

## 🛠️ 技术栈

### 后端
- Python 3.9+
- Flask 2.3 - Web 框架
- SQLAlchemy 2.0 - ORM
- PostgreSQL 13+ - 数据库
- Redis 6+ - 缓存和消息队列
- Celery - 异步任务处理
- BeautifulSoup4 / Scrapy - 网页爬虫

### 前端
- Vue 3 - 现代前端框架
- TypeScript - 类型安全
- Vite - 构建工具
- Pinia - 状态管理
- Vue Router - 路由
- Axios - HTTP 客户端
- Element Plus - UI 组件库

## 📁 项目结构

```
gongluejijieweiqu/
├── backend/
│   ├── app/
│   │   ├── models/           # 数据模型
│   │   ├── routes/           # API 路由
│   │   ├── services/         # 业务逻辑
│   │   └── config.py
│   ├── requirements.txt
│   ├── .env.example
│   └── wsgi.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── stores/
│   │   ├── api/
│   │   └── styles/
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml
└── Dockerfile.backend/frontend
```

## 🚀 快速开始

### 使用 Docker Compose（推荐）

```bash
git clone https://github.com/LILINWEI666/gongluejijieweiqu.git
cd gongluejijieweiqu

docker-compose up -d
```

访问：http://localhost:5173

### 本地开发

**后端：**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python wsgi.py
```

**前端：**
```bash
cd frontend
npm install
npm run dev
```

## 📚 主要 API 端点

| 功能 | 方法 | 端点 |
|------|------|------|
| 获取景点列表 | GET | `/api/attractions` |
| 获取景点详情 | GET | `/api/attractions/:id` |
| 搜索景点 | GET | `/api/attractions/search` |
| 获取餐厅列表 | GET | `/api/restaurants` |
| 获取实时排号 | GET | `/api/restaurants/:id/queue` |
| 获取攻略列表 | GET | `/api/guides` |
| 地图数据 | GET | `/api/map/all` |

## 🌐 支持城市

上海、杭州、宁波、绍兴、嘉兴等江浙沪地区

## 📝 环境配置

复制 `backend/.env.example` 为 `.env` 并修改相关配置。

## 🤝 贡献

欢迎 Fork 和 PR！

## 📄 许可证

MIT License

## 📧 联系方式

- GitHub: [@LILINWEI666](https://github.com/LILINWEI666)
- Issue: [GitHub Issues](https://github.com/LILINWEI666/gongluejijieweiqu/issues)

---

**Happy Traveling! 🚀✈️🏖️**
