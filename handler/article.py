#coding:utf8

import tornado.web
import torndb

class SubmissionHandler(tornado.web.RequestHandler):
    def get(self):
        user_id = self.get_cookie('id')
        self.render("submission.html", user_id = user_id)

class ApiSubmissionHandler(tornado.web.RequestHandler):
    def post(self):
        uid = self.get_cookie('uid')
        if uid is None or uid == '':
            self.write('你还没登录')
            return
        db = torndb.Connection(host="localhost", database="alex", user="root", password="11111111", time_zone='+8:00')
        user = db.get("select id from user where id=%s", uid)
        if user is None:
            db.close()
            self.write('登录已经过期，请重新登录')
            return
        title = self.get_argument('title')
        content = self.get_argument('content')
        data = db.insert("insert into article value (%s,%s,%s,%s,%s)", None,title,content,None,uid)
        db.close()
        self.write('插入成功!文章ID是' + str(data))

class CommentHandler(tornado.web.RequestHandler):
    def get(self, article_id):
        db = torndb.Connection(host="localhost", database="alex", user="root", password="11111111", time_zone='+8:00')
        article = db.get('select * from article where id=%s',article_id)
        user = db.get('select * from user where id=%s', article.uid)
        comments = db.query('select * from comment where article_id=%s', article_id)
        for comment in comments:
            uid = comment.uid
            user_info = db.get('select * from user where id=%s', uid)
            comment['user_info'] = user_info
        db.close()
        self.render('comment.html', comments=comments, article=article, user=user)

class ApiCommentHandler(tornado.web.RequestHandler):
    def post(self):
        article_id = self.get_argument('article_id')
        content = self.get_argument('content')
        uid = self.get_cookie('uid')
        db = torndb.Connection(host='localhost', database='alex', user='root', password="11111111", time_zone='+8:00')
        data = db.insert('insert into comment values (%S,%s,%s,%s,%s)', None, content, None, article_id, uid)
        db.close()
        self.redirect('/')