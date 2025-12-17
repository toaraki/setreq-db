# setreq-db

## local のpodman環境での起動

### Networkの作成
アプリの内部通信で使用するネットワークが必要となります。my-app-network (名称は任意の名称で問題ありません。) が無い場合は、以下のコマンドで作成します。

#### 作成
```
$ podman network create my-app-network
```

#### 確認
```
$ podman network list
...
...
```

### コンテナの起動
"registry.redhat.io/rhel9/postgresql-15" コンテナイメージを元として、postgresqlコンテナを起動します。

####
* --name : コンテナの識別子。podman の内部ネットワーク(ここでは、my-app-network) 無いで名前解決される名称も兼ねる
* --network : コンテナが接続する podmanの内部ネットワーク名称
* -e : 環境変数 postgresql に環境変数
  * POSTGRESQL_USER=djuser データベース接続時のユーザー名
  * POSTGRESQL_PASSWORD=XXXXXX データベース接続時のパスワード
  * POSTGRESQL_DATABASE=djdb データベース名

#### 起動
```
$ podman run -d \
    --name db \
    --network my-app-network \
    -e POSTGRES_USER=djuser \
    -e POSTGRES_PASSWORD=<任意の文字列に置き換えてください> \
    -e POSTGRES_DB=djdb \
    registry.redhat.io/rhel9/postgresql-15
```



起動方法のメモ


## postgresql 接続用のシークレットの作成
```
oc create secret generic dj-db-secret \
    --from-literal=POSTGRESQL_USER=djuser \
    --from-literal=POSTGRESQL_PASSWORD=<ここに本番DBのパスワードを記述> \
    --from-literal=POSTGRESQL_DATABASE=djdb
```
