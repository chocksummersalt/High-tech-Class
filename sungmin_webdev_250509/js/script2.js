$(document).ready(function(){
    //**** 마우스오버  ****//
    //서브메뉴 숨기고 시작
    $(".mSub").hide();
    // 마우스 오버
    $(".menu").mouseover(function(){
      $(".mSub").stop().slideDown(300);
     }).mouseout(function(){
      $(".mSub").stop().slideUp(300);
    });
});