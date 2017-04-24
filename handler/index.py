#coding: utf8

import tornado.web
import torndb

class HotHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hot.html")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")


class ApiLoginHandler(tornado.web.RequestHandler):

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = torndb.Connection(host="localhost", database="alex", user="root", password="11111111", time_zone='+8:00')
        data = db.get("select last_login_at from user where username=%s",username)
        data2 = db.update("update user set last_login_at = Null where username=%s",username)
        data3 = db.get("select id from user where username=%s and password=%s",username,password)
        db.close()
        if data3 is not None:
            self.set_cookie('username', username)
            self.set_cookie('uid', str(data3.id))
            data4 = db.update("update user set user.last_login_at=Null where username=%s and password=%s",username,password)
            self.write({"code": 1, "last_login_at": str(data.last_login_at)})
            # self.write('登陆成功!您上次登录时间是' + str(data.last_login_at))
        else:
            self.write({"code": 0, "msg": '用戶名或密碼錯誤'})
            # self.write('登陆失败!请核对用户名和密码！')


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")


class ApiRegisterHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = torndb.Connection(host="localhost", database="alex", user="root", password="11111111", time_zone='+8:00')
        data = db.insert("insert into user value(%s,%s,%s,%s,%s)",None,username,password,None,None)
        db.close()
        username = self.get_cookie("username")
        self.write("注册成功!您的ID是" + str(data))