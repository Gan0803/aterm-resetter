# これは何？

ルーター（Aterm WG1200HS4）を再起動するスクリプトです。

# どうやって使う？

本スクリプトはpython 3.8.12で動作します。

`pip install -r requirements.txt`で必要なパッケージをインストールしてください。

aterm-resetter.pyと同じディレクトリにsecrets.yamlファイルを作成し、以下の情報を記載してください。

```
username: "username"
password: "password"
url = "http://192.168.10.1/"
```
