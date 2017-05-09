/**
 * Created by ALEX on 2017/5/2.
 */
(function ($) {

    getArticle();

    getComments();

    function getArticle() {
        var id = window.location.href.split("/")[4];
        $.ajax({
            url: '/api/article/' + id,
            type: 'GET',
            data: {},
            dataType: 'json',
            success: function (data) {
                console.log('成功：', data);
                var article = data.body;
                var articleHtml = template('template-article', article)
                $("#article").html(articleHtml)
            }
        })
    }

    function getComments() {
        var id = window.location.href.split("/")[4];
        $.ajax({
            url: '/api/comments/' + id,
            type: 'GET',
            data: {},
            dataType: 'json',
            success: function (data) {
                console.log('成功：', data);
                var comments = data.body;
                var commentsHtml = template('template-comments', comments)
                $("#comments").html(commentsHtml);
            },
            error: function (data) {
                console.log('错误：', data)
            }
        })
    }

})(jQuery);