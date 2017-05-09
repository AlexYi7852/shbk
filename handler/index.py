# coding: utf8

import tornado.web

from tornado.escape import json_encode
from util.database import get_db

#解决js跨域请求问题
class BaseHandler(tornado.web.RequestHandler):
     def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ApiArticlesHandler(BaseHandler):
    # def get(self):
    #     db = torndb.Connection(host="localhost", database="alex", user="root", password="11111111", time_zone="+8:00")
    #     articles = db.query('select * from article order by created_at ASC')
    #     for article in articles:
    #         uid = article.user_id
    #         user_info = db.get('select id,username from user where id=%s', uid)
    #         article['user_info'] = user_info

    def get(self):
        db = get_db()
        articles = db.query('select a.*,  (select count(*) from comment where comment.article_id=a.id) as count from article as a')
        result = {}
        content = []

        for article in articles:
            tempData = {}
            uid = article.user_id
            user = db.get('select username from user where id=%s', uid)
            tempData['username'] = user.username
            tempData['id'] = article.id
            tempData['title'] = article.title
            tempData['content'] = article.content
            tempData['count'] = article.count
            tempData['created_at'] = article.created_at.strftime("%Y-%m-%d %H:%M:%S")
            content.append(tempData)
        result['Code'] = '0'
        result["body"] = {'articles': content}
        result["message"] = "成功"
        print json_encode(result)
        self.write(json_encode(result))



class HotHandler(tornado.web.RequestHandler):
    def get(self):
        db = get_db()
        articles = db.query('select * from article order by created_at ASC')
        for article in articles:
            uid = article.user_id
            user_info = db.get('select id,username from user where id=%s', uid)
            article['user_info'] = user_info
        db.close()
        self.render("hot.html", articles = articles)


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")


class ApiLoginHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = get_db()
        data = db.get("select last_login_at from user where username=%s", username)
        data2 = db.update("update user set last_login_at = Null where username=%s", username)
        data3 = db.get("select id from user where username=%s and password=%s", username, password)
        db.close()
        if data3 is not None:
            self.set_cookie('username', username)
            self.set_cookie('uid', str(data3.id))
            data4 = db.update("update user set user.last_login_at=Null where username=%s and password=%s", username, password)
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
        db = get_db()
        data = db.insert("insert into user value(%s,%s,%s,%s,%s)", None, username, password, None, None)
        db.close()
        username = self.get_cookie("username")
        self.write("注册成功!您的ID是" + str(data))
