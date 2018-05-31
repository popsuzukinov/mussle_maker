# mussle_maker
## 筋トレ管理アプリケーション
#### 筋トレを管理し、効率よく筋トレライフを送りたい筋肉エンジニアに捧げたいアプリ
### やりたいこと一覧
* 筋トレメニュー管理
* 食事メニュー提案
* 筋トレの時間にスマホにプッシュ通知
* 

### マイグレーション実施
```
$ python manage.py makemigrations mussle_core --settings=mussle_maker.local_setting
```
```
$ python jdv_sats_web/manage.py makemigrations sats_core --settings=jdv_sats_web.local_settings
```