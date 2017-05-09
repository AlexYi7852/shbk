/**
 * Created by ALEX on 2017/4/25.
 */
(function ($) {

    getArticles();

    $(document).on('click', '.btn-comment', function (e) {
        postComment(e);
    });

    document.onkeydown = function (event) {
        var e = event || window.event || arguments.callee.caller.arguments[0];
        if (e && e.keyCode == 13) {
            postComment(e);
        }
    };

    function getArticles() {
        $.ajax({
            url: '/api/articles',
            type: 'GET',
            data: {},
            dataType: 'json',
            success: function (data) {
                console.log(data);
                var articles = data.body;
                var articleHtml = template('from-article', articles);
                $("#articles").html(articleHtml);
            },
            error: function (data) {
                console.log(data);
            }
        })
    }

    function postComment(e) {
        var $target = $(e.target),
            $form = $target.parent('.comment-from'),
            content = $form.find(".content").val(),
            article_id = $form.find(".article_id").val();
        if(content == ''){
            return;
        }
        var params = {
            article_id: article_id,
            content: content
        };
        $.ajax({
            url: '/api/comment',
            type: 'POST',
            data: params,
            dataType: 'json',
            success: function (data) {
                if (data.code == 0) {
                    alert('提交评论成功!');
                    $('.content').val("");
                } else if (data.code == 1) {
                    alert('你還沒登錄，請新登錄');
                    window.location = '/login'
                }
            },
            error: function (data) {
                console.log('错误：', data);
            }
        })
    }

})(jQuery);

