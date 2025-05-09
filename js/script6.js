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
  
    //**** 이미지슬라이드  ****//
    //a태그 2번,3번 숨기고 시작
    $(".slide > a:gt(0)").hide();
  
    setInterval(function(){
      $('.slide a:first-child').fadeOut()
      .next('a').fadeIn()
      .end().appendTo('.slide');
    }, 3000);
  
    // ******  탭 메뉴 공지사항 갤러리  ****** //
    $(function(){
        $('.c1c2 > h3').click(function(){
            $('.c1c2 > h3').removeClass('on');
            $(this).addClass('on');
            $('.c1c2 ul').removeClass('on');
            $(this).next("ul").addClass("on");
     
      });
    });
  
    // ******  레이어팝업  ****** //
    $('.notice li:first').click(function(){
      $('#modalWrap').addClass("active");
    });
    $('.btn').click(function(){
      $('#modalWrap').removeClass("active");
    });
  
  });