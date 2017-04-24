/**
 * Created by ALEX on 2017/4/24.
 */

(function ($) {
    function submission() {
        var params = {
            title: $("#title").val(),
            content: $("#content").val()
        };
        /**
         * 通用写法
         */
        // $.ajax({
        //     url: '/api/register',
        //     type: 'POST',
        //     data: params,
        //     dataType: 'json',
        //     success: function (data) {
        //         console.log('成功：',data);
        //         alert('恭喜你，注册成功！')
        //     },
        //     error: function (data) {//fail
        //         console.log('错误:',data);
        //     }
        // });

        /**
         * POST写法
         */
        $.post({
            url: '/api/submission',
            data: params,
            dataType: 'json',
            success: function (data) {
                console.log('成功：',data);
                alert('恭喜你，投稿成功！')
            },
            error: function (data) {//fail
                console.log('错误:',data);
            }
        });

        /**
         * GET 写法
         */
        // $.get({
        //     url: '/api/register',
        //     data: params,
        //     dataType: 'json',
        //     success: function (data) {
        //         console.log('成功：',data);
        //         alert('恭喜你，注册成功！')
        //     },
        //     error: function (data) {//fail
        //         console.log('错误:',data);
        //     }
        // });
    }

    $("#btn-submission").on("click",function () {
        submission();
    });


})(jQuery);