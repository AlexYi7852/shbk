/**
 * Created by ALEX on 2017/5/12.
 */

$(document).ready(function(){
    $('#mini-login').click(function(){
        $('.main-x').css('display', 'block');
        $('.about').css('display', 'block');
    })

    $('.about').click(function() {
        $('.main-x').css('display', 'none');
        $('.about').css('display', 'none');
    })
})