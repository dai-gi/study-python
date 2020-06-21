# パッケージでモジュールを管理
# パッケージ = モジュール(モジュールファイル)を入れるフォルダのこと
# パッケージをpythonで認識させる方法 = __init__.py のファイルを作成する( ※ ファイルの中は何もなくてもOK)

# パッケージに入れたモジュールの使用方法 = 「フォルダがモジュール化されたもの」と考えると分かりやすいかも
# import パッケージ名.モジュールファイル名
# import mypackage.user
# importする名前が長い場合、「as」を使えば省略または、名前を変えて使用できる
# import mypackage.user as mymodule
# AdminUserクラスだけを使う方法
from mypackage.user import AdminUser

# bob = mypackage.user.AdminUser("bob", 23)
# bob = mymodule.AdminUser("bob", 23)
bob = AdminUser("bob", 23)

print(bob.name)
bob.say_hi()
bob.say_hello()


