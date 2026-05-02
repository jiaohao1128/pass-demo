from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>云服务PaaS部署演示</h1>
    <p>这是一个部署在云服务上的简单Web应用</p>
    <p>开发者：焦昊</p>
    <p>平台类型：PaaS（平台即服务）</p>
    '''

@app.route('/info')
def info():
    return '''
    <h2>应用信息</h2>
    <p>开发语言：Python + Flask</p>
    <p>开发者：焦昊</p>
    <p>部署方式：PaaS自动部署，无需配置服务器</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)