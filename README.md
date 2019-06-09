# Stage1 Onliner

一个没什么用的挂Stage1论坛在线时间的python脚本。

只支持Windows，Linux请自行修改相关windows依赖项（如`os.system("cls")`到`os.system("clear")`）。

## 声明

自用，不保证有效性，截至2019-06-10是有效的。

我没有发现s1有无禁止刷在线时间的规定，对于任何使用本脚本出现的后果与本人无关。如果s1禁止相关行为，我将删掉repo。

## 依赖

1. Selenium for python

   ```
   pip install selenium
   ```

2. Chrome

3. Chrome WebDriver

   下载[适合自己Chrome版本的webdriver](https://npm.taobao.org/mirrors/chromedriver)到python安装目录下(或者任何环境变量路径下)

## 使用

1. 编辑`config.py`，填写自己的用户名/密码，保存并关闭
2. 双击`app.bat`，或者执行`python -u app.py`即可

## 协议

MIT

