# python-pdf2image

pdf2image (https://pdf2image.readthedocs.io/en/latest/reference.html) の使い方を確認するために作成したコードです.

## PC 上で 実行する

Poppler をインストールします.

```sh
$ brew install poppler
```

依存パッケージの管理のために pip-tools を使用するので、インストールしてください.

```sh
(.venv)$ pip install pip-tools
```

以下でこのプロジェクトで必要なパッケージをインストールします.

```sh
(.venv)$ pip-compile requirements.in
(.venv)$ pip-sync
```

```sh
(.venv)$ python ./src/pdf2image
```

## Lambda 上で 実行する

localstack を起動します

```sh
$ docker network create localstack
$ docker-compose up -d
```

localstack の s3 に pdf をアップロードします

```sh
$ aws s3 mb s3://bucket/ --endpoint-url=http://localhost:4566
$ aws s3 cp ./pdf/Catalogue.pdf s3://bucket/Catalogue.pdf --endpoint-url=http://localhost:4566
```

ビルドします

```sh
$ sam build --use-container -c -t ./template.yaml
```

以下で実行します

```sh
sam local invoke Image2PdfFunc --docker-network localstack
```
