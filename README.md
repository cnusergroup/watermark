# 图片水印工具 - CDK 部署

纯前端单页应用，使用 AWS CDK 部署到 S3 + CloudFront（OAC）。

## 架构

- S3 Bucket：存储静态文件，禁止公共访问
- CloudFront Distribution：通过 OAC 访问 S3，强制 HTTPS
- BucketDeployment：自动上传 `index.html` 到 S3

## 部署步骤

### 1. 安装依赖

```bash
# 安装 AWS CDK CLI（如未安装）
npm install -g aws-cdk

# 创建虚拟环境并安装 Python 依赖
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. 配置 AWS 凭证

确保已配置 AWS CLI 凭证：

```bash
aws configure
```

### 3. Bootstrap CDK（首次使用 CDK 时需要）

```bash
cdk bootstrap
```

### 4. 部署

```bash
cdk deploy
```

部署完成后，终端会输出 CloudFront URL，即可通过该 URL 访问应用。

### 5. 销毁资源（可选）

```bash
cdk destroy
```
