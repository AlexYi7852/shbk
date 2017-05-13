/**
 * Created by ALEX on 2017/5/11.
 */
(function ($) {

    getUsersInfo()

    getUserArticles()

    function getUsersInfo(){
        var id = window.location.href.split("/")[4];
        $.ajax({
            url: '/api/users/' + id,
            type: 'GET',
            data: {},
            dataType: 'json',
            success: function (data) {
                console.log(data);
                var users = data.body;
                var usersHtml = template('template-users', users)
                $("#users-top").html(usersHtml)
            },
            error: function (data) {
                console.log('错误：', data)
            }
        })
    }

    function getUserArticles(){
        var id = window.location.href.split("/")[4];
        $.ajax({
            url: '/api/users_articles/' + id,
            type: 'GET',
            data: {},
            dataType: 'json',
            success: function(data){
                console.log(data);
                var articles = data.body;
                var usersHtml = template('template-articles', articles)
                $("#users-top-bottom").html(usersHtml)
            },
            error: function(data){
                console.log('错误：', data)
            }
        })
    }
})(jQuery);