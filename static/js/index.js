/**
 * Created by ALEX on 2017/4/25.
 */
(function ($){
    function article(){
        var params = {
            article_id: $("#article_id"),
            content: $("#content")
        };
        $.ajax({
            url: 'api/comment',
            type: 'POST',
            data: params,
            dataType: 'json',
            success: function(data){
                console.log('提交成功：', data);
            }
        })
    }
})