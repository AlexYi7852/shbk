/**
 * Created by ALEX on 2017/4/24.
 */
(function ($) {
    $("#btn-login").on("click", function () {
        login();
    });
    document.onkeydown = function (event) {
        var e = event || window.event || arguments.callee.caller.arguments[0]
        if(e && e.keyCode == 13){
            login()
        }
    }
    function login() {
        var params = {
            username: $("#username").val(),
            password: $("#password").val()
        };
        $.ajax({
            url: '/api/login',
            type: 'POST',
            data: params,
            dataType: 'json',
            success: function (data) {
                console.log('成功：', data);
                if (data.code == 1) {
                    alert('登錄成功，上次登錄時間 ' + data.last_login_at)
                } else {
                    alert('登錄失敗' + data.msg)
                }
            },
            error: function (data) {//fail
                console.log('错误:', data);
            }
        });
    }
})(jQuery);