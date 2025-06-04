@charset "utf-8";

/*초기 설정*/
*{
  margin: 0;
  padding: 0;
  list-style:none;
  box-sizing: border-box;
}
body{
  background: #ffffff;
  color:#222328;
}
a{
  text-decoration:none;
  display:block;
}

/********본문시작*********/
/* 모든 컨텐츠를 감싸는 main */
main {
  width: 1200px;
  margin:0 auto;
}

/* 메뉴와 로고가 들어가는 header */
header {
    width:100%;
    height:100px;
    background: #723ffb;
    display:flex;
    justify-content: space-between;
    align-items: center;
  }
  
  /*로고*/
  .logo {
    width:20%;
    display: flex; /*로고 이미지를 중앙에 위치 시키기 위해 flex로 지정하여 수평, 수직 정렬이 되도록 하기 위해.*/
    justify-content: center; /* 수평 가운데 정렬 */
    align-items: center; /* 수직 가운데 정렬 */
  }
  /*로고이미지*/
  .logo > img{
    width:200px; /*지시사항에 적힌대로 width값 */
    height:40px; /*지시사항에 적힌대로 height값 */
  }
  
  /*메인메뉴*/
  .mainMenu {
    width:800px; /*서브메뉴랑 동일하게*/
    height:100%; /*header의 높이 그대로 */
    display: flex;
    justify-content: space-between;
    align-items:center;
    position:relative; /*subMenu때문에 반드시 필요*/
  }
  .mainMenu > a{
    width:25%;
    padding:20px 0;
    text-align: center;
    color:#ffffff;
  }
  .mainMenu > a:hover{
    background: rgba(255,255,255, 0.1);
  }
  
  .subMenu{
    width:800px; /*메인메뉴 위치랑 동일하게*/
    display:flex;
    justify-content: space-between;
    background: #222328;
    position:absolute;
    right:0;
    top:100px; /*header 높이 만큼 내려옴*/
    z-index:1;
  }
  .subMenu > ul{
    width:25%;
  }
  .subMenu > ul > li > a{
    text-align: center;
    padding:10px 0;
    color:#723ffb;
  }
  .subMenu > ul > li > a:hover{
    background: rgba(255,255,255, 0.1);
    color:#ffffff;
  }