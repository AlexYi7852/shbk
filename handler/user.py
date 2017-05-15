#coding: utf8

import tornado.web
from util.database import get_db
from tornado.escape import json_encode

class UsersHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        self.render('users.html')

class ApiUserInfoHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        db = get_db()
        user = db.get('select id, username, last_login_at, created_at from user where id=%s', user_id)
        user['last_login_at'] = str(user['last_login_at'])
        user['created_at'] = str(user['created_at'])
        db.close()
        result = {}
        result['code'] = '0'
        result['body'] = {'user' : user}
        result['message'] = '成功'
        print json_encode(result)
        self.write(json_encode(result))

class ApiUserArticlesHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        db = get_db()
        articles = db.query('select * from article where user_id=%s', user_id)
        for article in articles:
            username = db.get('select username from user where id=%s', article.user_id)
            article['username'] = username.username
            article['created_at'] = str(article['created_at'])
        db.close()
        result = {}
        result['code'] = '0'
        result['body'] = {'articles' : articles}
        result['message'] = '成功'
        print json_encode(result)
        self.write(json_encode(result))

class ApiUserCommentsHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        db = get_db()
        articles = db.get('select * from article where user_id=%s', user_id)
        comments = db.query('select * from comment where article_id=%s', articles.id)
        for comment in comments:
            username = db.get('select username from user where id=%s', comment.uid)
            comment['username'] = username.username
            comment['created_at'] = str(comment['created_at'])
        db.close()
        result = {}
        result['code'] = '0'
        result['body'] = {'comments' : comments}
        result['message'] = '成功'
        print json_encode(result)
        self.write(json_encode(result))