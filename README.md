# パスワード管理システム

## 機能一覧
| ログイン画面 |
| ---- |
| ![ログイン画面](/docs/login.png) |

| データ登録画面(パスワード自動生成) |
| ---- |
| ![データ一覧画面](/docs/data-list.png) |

| ログイン画面 |
| ---- | ---- |
| ![ログイン画面](/docs/login.png) |

| データ登録画面(パスワード自動生成) |
| ---- |
| ![データ登録画面(パスワード自動生成)](/docs/autocreatepass.gif) |

<br />

## 使用技術

| Category          | Technology Stack                                     |
| ----------------- | --------------------------------------------------   |
| Frontend          | javascript, py-script, html, css, bootstrap4         |
| Backend           | python, Django                                       |
| Database          | SQLite                                               |
| CI/CD             | GitHub                                               |

<br />

#### users テーブル

| Column       | Type     | Options               |
| -------------| ---------| ----------------------|
| id           | integer  | primary key, not null |
| password     | varchar  | null: false           |
| username     | varchar  | not null, unique      |
| first_name   | varchar  | not null              |
| last_name    | varchar  | not null              |
| email        | varchar  | not null              |
| last_login   | datetime |                       |
| is_superuser | bool     | not null              |
| is_staff     | bool     | not null              |
| is_active    | bool     | not null              |
| date_joined  | datetime | not null              |


#### pw_recorder テーブル

| Column     | Type     | Options               |
| -----------| ---------| ----------------------|
| id         | integer  | primary key, not null |
| site_name  | varchar  | not null              |
| password   | varchar  | not null              |
| created_at | datetime | not null              |
| updated_at | datetime | not null              |
| user_id    | integer  | foreign key, not null |

<br />

## 実装予定機能

* ユーザー顔認証機能
    * webRTCを使用