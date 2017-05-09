#coding:utf8

import tornado.web
from tornado.escape import json_encode
from util.database import get_db

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
        db = get_db()
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

class ArticleHandler(tornado.web.RequestHandler):
    def get(self, article_id):
        self.render('article.html')

class ApiCommentsHandler(tornado.web.RequestHandler):
    def get(self, article_id):
        db = get_db()
        comments = db.query('select * from comment where article_id=%s',article_id)
        for comment in comments:
            user_info = db.get('select id, username from user where id=%s', comment.uid)
            comment['user_info'] = user_info
            comment['created_at'] = str(comment['created_at'])
        db.close()
        result = {}
        result['code'] = '0'
        result['body'] = {'comments' : comments}
        result['message'] = '成功'
        self.write(json_encode(result))

class ApiArticleHandler(tornado.web.RequestHandler):
    def get(self, article_id):
        db = get_db()
        article = db.get('select content, user_id from article where id=%s', article_id)
        username = db.get('select username from user where id=%s', article.user_id)
        db.close()
        article['username'] = username.username
        result = {}
        result['code'] = '0'
        result['body'] = article
        result['message'] = '成功'
        self.write(json_encode(result))

class ApiArticleDetailHandler(tornado.web.RequestHandler):
    def get(self, article_id):
        db = get_db()
        article_content = db.get('select content from article where id=%s',article_id)
        article_username = db.get('select username from user where id=%s', article_id)
        comments = db.query('select * from comment where article_id=%s', article_id)
        comment_content = db.query('select content from comment where article_id=%s', article_id)
        result = {}
        content = []
        for comment in comments:
            tempData = {}
            uid = comment.uid
            comment_username = db.query('select username from user where id=%s', uid)
            tempData['article_username'] = article_username
            tempData['comment_username'] = comment_username
            tempData['article_content'] = article_content
            tempData['comment_content'] = comment_content
            content.append(tempData)
        result['Code'] = '0'
        result['body'] = {'comments' : content}
        result['message'] = '成功'
        print json_encode(result)
        db.close()
        self.write(json_encode(result))

class ApiCommentHandler(tornado.web.RequestHandler):
    def post(self):
        article_id = self.get_argument('article_id')
        content = self.get_argument('content')
        uid = self.get_cookie('uid')
        if not uid:
            self.write({"code": 1, "msg": "你還沒登錄，請新登錄"})
            return
        db = get_db()
        db.insert('insert into comment value (%s,%s,%s,%s,%s)', None, content, None, article_id, uid)
        db.close()
        self.write({"code": 0, "msg": '提交评论成功！'})
        #self.redirect('/')




