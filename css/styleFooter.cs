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

/* Footer 하단  */
footer {
    width:100%;
    height:100px;
    display:flex;
    justify-content:space-between;
    background: #222328;
  }
  /* 하단 공통 */
  footer div{display: flex; justify-content: center; align-items: center;}
  /* 로고 */
  footer div:nth-child(1){width: 20%; opacity: 0.2;}
  /* copyright */
  footer div:nth-child(2){width: 60%; color: #777777;}
  /* SNS */
  footer div:nth-child(3){width: 20%; justify-content: space-around;}
  footer div:nth-child(3) img{border-radius: 50%;}
  