# これは何？

ルーター（Aterm WG1200HS4）を再起動するスクリプトです。
seleniumを使って管理画面にログインし再起動操作を行います。

# どうやって使う？

本スクリプトはpython 3.8.12で動作します。

`pip install -r requirements.txt`で必要なパッケージをインストールしてください。

本スクリプトはchromeを使って動作するため、chromiumとchromedriverをインストールしてください。
```
sudo apt install chromium chromium-chromedriver
```

環境によってはrustや以下のライブラリを追加でインストールする必要があるかもしれません。
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
sudo apt install -y libssl-dev libreadline-dev libsqlite3-dev
```

aterm-resetter.pyと同じディレクトリにsecrets.yamlファイルを作成し、以下の情報を記載してください。

```
username: "username"
password: "password"
url = "http://192.168.10.1/"
```

以下のようにcronを使って定期実行することができます。aterm-resetter.shのユーザー名やパスは環境に合わせて修正してください。
```
12 3 * * * $HOME/aterm-resetter/aterm-resetter.sh >> /tmp/cron.log 2>&1
```
